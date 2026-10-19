#!/usr/bin/env python3
print("HEARTBEAT: Script started and executing...")
import argparse
import os
import sys
import subprocess
import time
import cv2
import numpy as np
from pathlib import Path

print("DEBUG: Loaded basic libs (cv2, numpy)")

# Ensure ffmpeg is findable
_hb = "/opt/homebrew/bin"
if os.path.isdir(_hb) and _hb not in os.environ.get("PATH", ""):
    os.environ["PATH"] = _hb + os.pathsep + os.environ.get("PATH", "")

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("DEBUG: Importing modules.globals...")
import modules.globals
print("DEBUG: modules.globals loaded")

print("DEBUG: Importing face_analyser...")
from modules.face_analyser import get_one_face, get_many_faces, detect_many_faces_fast
print("DEBUG: face_analyser loaded")

PRESETS = {
    "speed": {
        "resolution": 720,
        "fps": 30,
        "model": "inswapper_128_fp16",
        "det_size": (640, 640),
        "color_correction": True,
        "chin_blend_weight": 0.5,
        "crf": 18,
        "preset": "medium",
    },
    "balanced": {
        "resolution": 1080,
        "fps": 30,
        "model": "inswapper_128_fp16",
        "det_size": (640, 640),
        "color_correction": True,
        "chin_blend_weight": 0.5,
        "crf": 16,
        "preset": "slow",
    },
}

def setup_globals(preset: dict):
    print("DEBUG: Setting up globals...")
    modules.globals.headless = True
    modules.globals.execution_providers = ["CoreMLExecutionProvider", "CPUExecutionProvider"]
    modules.globals.execution_threads = 8
    modules.globals.swapper_model = preset.get("model", "inswapper_128_fp16")
    modules.globals.color_correction = preset.get("color_correction", True)
    modules.globals.chin_blend_weight = preset.get("chin_blend_weight", 0.5)
    print("DEBUG: Globals setup done")

def is_redhead(frame, bbox):
    x_min, y_min, x_max, y_max = map(int, bbox)
    hair_h = int((y_max - y_min) * 0.3)
    hair_y_min = max(0, y_min - hair_h)
    hair_roi = frame[hair_y_min:y_min, x_min:x_max]
    if hair_roi.size == 0: return False
    hsv = cv2.cvtColor(hair_roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([0, 50, 50]), np.array([25, 255, 255]))
    return (np.sum(mask) / (hair_roi.shape[0] * hair_roi.shape[1])) > 0.1

def process_video(source_face_objs, target_path, output_path, preset: dict):
    """Turbo Sequential processing with fast-path detection."""
    setup_globals(preset)

    print("DEBUG: Importing face_swapper...")
    from modules.processors.frame.face_swapper import swap_face, get_face_swapper
    print("DEBUG: face_swapper imported")

    print("DEBUG: Loading Turbo Models (this is the slow part)...")
    swapper = get_face_swapper()
    print("DEBUG: Model loaded successfully")

    cap = cv2.VideoCapture(target_path)
    orig_fps = cap.get(cv2.CAP_PROP_FPS)
    orig_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    orig_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    target_res = preset["resolution"]
    if target_res is None:
        out_width, out_height = orig_width, orig_height
        out_fps = orig_fps
    else:
        scale = target_res / max(orig_width, orig_height)
        out_width, out_height = int(orig_width * scale), int(orig_height * scale)
        out_fps = min(preset["fps"], orig_fps)

    print(f"🚀 TURBO START: {orig_width}x{orig_height} -> {out_width}x{out_height}")

    audio_path = f"/tmp/turbo_audio_{os.path.basename(target_path)}.m4a"
    subprocess.run(["ffmpeg", "-y", "-i", target_path, "-vn", "-acodec", "aac", "-b:a", "128k", audio_path], capture_output=True)

    temp_video = f"/tmp/turbo_temp_{os.path.basename(target_path)}.mp4"
    out = cv2.VideoWriter(temp_video, cv2.VideoWriter_fourcc(*'mp4v'), out_fps, (out_width, out_height))

    start_time = time.time()
    frame_num = 0
    processed = 0

    while True:
        ret, frame = cap.read()
        if not ret: break
        frame_num += 1

        if out_width != orig_width or out_height != orig_height:
            frame = cv2.resize(frame, (out_width, out_height), interpolation=cv2.INTER_LINEAR)

        target_faces = detect_many_faces_fast(frame)
        if target_faces:
            for face in target_faces:
                if is_redhead(frame, face.bbox):
                    source_obj = source_face_objs[0]
                else:
                    source_obj = source_face_objs[1]

                result = swap_face(source_obj, face, frame)
                if result is not None:
                    frame = result
                    processed += 1

        out.write(frame)
        if frame_num % 50 == 0:
            elapsed = time.time() - start_time
            fps = frame_num / elapsed
            print(f"  Frame {frame_num}/{total_frames} - {fps:.1f} fps - {processed} faces swapped")

    cap.release()
    out.release()

    print("Finalizing video with ultrafast encoding...")
    subprocess.run(["ffmpeg", "-y", "-i", temp_video, "-i", audio_path,
                    "-c:v", "libx264", "-preset", "ultrafast", "-crf", str(preset['crf']),
                    "-c:a", "aac", "-shortest", output_path], capture_output=True)

    os.remove(audio_path)
    os.remove(temp_video)
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source1", required=True)
    parser.add_argument("--source2", required=True)
    parser.add_argument("--video", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--preset", default="balanced")
    args = parser.parse_args()

    preset = PRESETS.get(args.preset, PRESETS["balanced"])

    from modules.face_analyser import get_one_face
    s1_face = get_one_face(cv2.imread(args.source1))
    s2_face = get_one_face(cv2.imread(args.source2))
    source_face_objs = [s1_face, s2_face]

    success = process_video(source_face_objs, args.video, args.output, preset)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
