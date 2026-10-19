#!/usr/bin/env python3
# ponytail: reads CPHI xlsx, dedupes vs Notion CRM, creates new contacts
import json, subprocess, sys
from pathlib import Path

NOTION_DB = "3fd3119c-aff8-81bf-b16c-f53ceff38303"
EXISTING = ["Next Pharma", "Dexa Group", "Ferozsons", "Novamed", "SHAPHACO", 
            "Emerald Enterprises", "Synthetic Molecules", "Hema Pharma", 
            "Relco Pharma", "Ankit Pulps", "MetroAPI", "Afiq Pharma", 
            "Praveen", "Moosa", "Ali Moosa", "MOH Oman", "Khimji Ramdas", 
            "Lotus Shipping", "Project Covalence Oman", "Evident Lifesciences", 
            "Alaqsachem", "Grand Pharma", "Evertogen Life Sciences Ltd", 
            "Genepharm S.A.", "Olive PharmaScience Ltd."]

xlsx = Path("Claude_Work/files/CPHI_Milan_2026_Leads.xlsx")
if not xlsx.exists():
    print(f"✗ {xlsx} not found"); sys.exit(1)

# Extract via Python's zipfile (xlsx = zip of xml)
import zipfile, xml.etree.ElementTree as ET
with zipfile.ZipFile(xlsx) as zf:
    sheet_xml = zf.read("xl/worksheets/sheet2.xml")  # sheet2 = KAD leads
    strings_xml = zf.read("xl/sharedStrings.xml")
    
root = ET.fromstring(sheet_xml)
strings = [t.text for t in ET.fromstring(strings_xml).iter() if t.text]

rows = []
for row in root.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row"):
    cells = [c.find("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v") 
             for c in row]
    vals = [strings[int(c.text)] if c is not None and c.text.isdigit() else "" 
            for c in cells]
    if vals and any(vals): rows.append(vals)

new = [r for r in rows[1:] if len(r) > 1 and r[1] not in EXISTING][:10]  # first 10
print(f"✓ {len(rows)-1} leads, {len(new)} new contacts")

for r in new:
    company, country = r[1], r[2] if len(r) > 2 else "N/A"
    print(f"  → {company} ({country})")
    subprocess.run(["python3", "~/.hermes/agents/notion_helper.py", "create_page", 
                    json.dumps({"parent": {"database_id": NOTION_DB}, 
                               "properties": {"Name": {"title": [{"text": {"content": company}}]},
                                             "Country": {"rich_text": [{"text": {"content": country}}]}}})])
