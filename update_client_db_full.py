import pandas as pd
import os

file_path = '/Users/moosaali/MacStorage/Moosa/06_CRM_and_Clients/client_database/AlWajer_KAD_Client_Database_Country_Client_Product.xlsx'

# Load the workbook
xl = pd.ExcelFile(file_path)
df_master = xl.parse('Client_Master')

# Data from agent research
research_data = [
    # PAKISTAN
    {'Client': 'AGP Limited', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generic Portfolio (PPIs), High Partnership Potential'},
    {'Client': 'Ferozsons Laboratories', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Specialized Generics / PPIs, High Partnership Potential'},
    {'Client': 'PharmEvo', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'High-end Generics / PPIs, High Partnership Potential'},
    {'Client': 'The Searle Company', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Portfolio / PPIs, High Partnership Potential'},
    {'Client': 'CCL Pharmaceuticals', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generic PPIs, High Partnership Potential'},
    {'Client': 'Highnoon Laboratories', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generic Range, High Partnership Potential'},
    {'Client': 'Tabros Pharma', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'PPIs / General Pharma, High Partnership Potential'},
    {'Client': 'Lucky Core Industries', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Basic Generics, Medium Partnership Potential'},
    {'Client': 'Medici Pakistan', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Agent', 'Importance': 'Medium', 'Key facts from files': 'Specializes in indenting/chemicals'},

    # KENYA
    {'Client': 'Beta Healthcare', 'Country': 'Kenya', 'Region': 'Africa', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generic / PPIs, High Partnership Potential'},
    {'Client': 'Regal Pharmaceuticals', 'Country': 'Kenya', 'Region': 'Africa', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Essential Generics / PPIs, High Partnership Potential'},
    {'Client': 'Zadchem Healthcare', 'Country': 'Kenya', 'Region': 'Africa', 'Role': 'Agent/Dist.', 'Importance': 'Medium', 'Key facts from files': 'EIPICO Agent (PPIs), Medium Partnership Potential'},
    {'Client': 'Prunus Pharma', 'Country': 'Kenya', 'Region': 'Africa', 'Role': 'Distributor', 'Importance': 'High', 'Key facts from files': 'Branded Generics / PPIs, Medium Partnership Potential'},
    {'Client': 'Sai Pharmaceuticals', 'Country': 'Kenya', 'Region': 'Africa', 'Role': 'Distributor', 'Importance': 'Medium', 'Key facts from files': 'Generic PPIs, Medium Partnership Potential'},
    {'Client': 'Transwide Pharma', 'Country': 'Kenya', 'Region': 'Africa', 'Role': 'Distributor', 'Importance': 'Medium', 'Key facts from files': 'Broad Range, Medium Partnership Potential'},

    # UAE
    {'Client': 'Julphar', 'Country': 'UAE', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generics / PPIs, High Partnership Potential'},
    {'Client': 'Neopharma', 'Country': 'UAE', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Specialized Generics, High Partnership Potential'},
    {'Client': 'LIFEPharma', 'Country': 'UAE', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Biosimilars/Generics, High Partnership Potential'},
    {'Client': 'Al Hayat Pharma', 'Country': 'UAE', 'Region': 'MENA', 'Role': 'Distributor', 'Importance': 'High', 'Key facts from files': 'MNC Agent / PPIs, Medium Partnership Potential'},
    {'Client': 'Arabian Ethicals', 'Country': 'UAE', 'Region': 'MENA', 'Role': 'Distributor', 'Importance': 'High', 'Key facts from files': 'Branded Generics, Medium Partnership Potential'},
    {'Client': 'Global Pharma', 'Country': 'UAE', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Generics, High Partnership Potential'},

    # UZBEKISTAN
    {'Client': 'Nobel Pharmsanoat', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generics / PPIs, High Partnership Potential'},
    {'Client': 'JV Novopharma Plus', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Generics / PPIs, High Partnership Potential'},
    {'Client': 'Serene Pharma', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generic PPIs, High Partnership Potential'},
    {'Client': 'Merrymed Farm', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generics, High Partnership Potential'},
    {'Client': 'Nika Pharm', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generics, High Partnership Potential'},
    {'Client': 'Jurabek Labs', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generic PPIs, High Partnership Potential'},
    {'Client': 'Anfa Pharma', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generics, High Partnership Potential'},
    {'Client': 'Meros Pharm', 'Country': 'Uzbekistan', 'Region': 'Central Asia', 'Role': 'Importer/Dist.', 'Importance': 'High', 'Key facts from files': 'Broad Portfolio, Medium Partnership Potential'},

    # ALGERIA
    {'Client': 'Groupe Saidal', 'Country': 'Algeria', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generic / PPIs, High Partnership Potential'},
    {'Client': 'Biopharm', 'Country': 'Algeria', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'High-end Generics, High Partnership Potential'},
    {'Client': 'Merinal', 'Country': 'Algeria', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Dry-form (Caps/Tabs), High Partnership Potential'},
    {'Client': 'Laboratoire Beker', 'Country': 'Algeria', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generic PPIs, High Partnership Potential'},
    {'Client': 'EL KENDI', 'Country': 'Algeria', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generics, High Partnership Potential'},

    # MOROCCO
    {'Client': 'Cooper Pharma', 'Country': 'Morocco', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Leading Generic / PPIs, High Partnership Potential'},
    {'Client': 'Sothema', 'Country': 'Morocco', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Broad Generics, High Partnership Potential'},
    {'Client': 'Hikma Morocco', 'Country': 'Morocco', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'High', 'Key facts from files': 'Branded Generics, Medium Partnership Potential'},

    # TUNISIA
    {'Client': 'Livealth Biopharma', 'Country': 'Tunisia', 'Region': 'MENA', 'Role': 'Manufacturer', 'Importance': 'Medium', 'Key facts from files': 'Generic PPIs, High Partnership Potential'},
    {'Client': 'OPPH', 'Country': 'Tunisia', 'Region': 'MENA', 'Role': 'State Dist.', 'Importance': 'High', 'Key facts from files': 'Essential PPIs, Medium Partnership Potential'},

    # LIBYA
    {'Client': 'Al-Basma Pharma', 'Country': 'Libya', 'Region': 'MENA', 'Role': 'Importer/Dist.', 'Importance': 'High', 'Key facts from files': 'Generic PPIs, Medium Partnership Potential'},
    {'Client': 'State Pharma', 'Country': 'Libya', 'Region': 'MENA', 'Role': 'State Org.', 'Importance': 'High', 'Key facts from files': 'Essential PPIs, Low Partnership Potential'},

    # ETHIOPIA
    {'Client': 'Ethiopian Pharma', 'Country': 'Ethiopia', 'Region': 'Africa', 'Role': 'State Manuf.', 'Importance': 'High', 'Key facts from files': 'Basic Generics, High Partnership Potential'},
    {'Client': 'Livealth Ethiopia', 'Country': 'Ethiopia', 'Region': 'Africa', 'Role': 'Importer/Dist.', 'Importance': 'Medium', 'Key facts from files': 'Generic PPIs, Medium Partnership Potential'},
]

# Convert new records to DataFrame
df_new = pd.DataFrame(research_data)

# Set defaults for missing columns to match df_master
for col in df_master.columns:
    if col not in df_new.columns:
        df_new[col] = None

# Order columns to match
df_new = df_new[df_master.columns]

# Avoid duplicates based on Client name
df_master = pd.concat([df_master, df_new], ignore_index=True).drop_duplicates(subset=['Client'], keep='last')

# IDs management
existing_ids = df_master['ID'].dropna().astype(str)
max_id = 0
for eid in existing_ids:
    try:
        max_id = max(max_id, int(eid[1:]))
    except:
        pass

current_id = max_id + 1
ids = []
for val in df_master['ID']:
    if pd.isna(val):
        ids.append(f"C{current_id:03d}")
        current_id += 1
    else:
        ids.append(val)
df_master['ID'] = ids

# Update the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_master.to_excel(writer, sheet_name='Client_Master', index=False)

print("Successfully updated Client_Master with full research data.")
