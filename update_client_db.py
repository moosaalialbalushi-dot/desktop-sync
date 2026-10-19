import pandas as pd
import os

file_path = '/Users/moosaali/MacStorage/Moosa/06_CRM_and_Clients/client_database/AlWajer_KAD_Client_Database_Country_Client_Product.xlsx'

# Load the workbook
xl = pd.ExcelFile(file_path)
df_master = xl.parse('Client_Master')

# New records to add
new_records = [
    # Pakistan
    {'Client': 'Emerald Enterprises', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Agent', 'Relationship stage': 'Stage 9', 'Channel / agent': 'Exclusive Agreement', 'Contact person': 'Khizer Khalid', 'Next action / owner': 'Finalize Exclusive Agreement', 'Key facts from files': 'Requested exclusive agreement for export 2% for high value'},
    {'Client': 'Mansoor Chemicals', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Prospect', 'Contact person': 'Sarfaraz Yar Khan', 'Next action / owner': 'Review Portfolio'},
    {'Client': 'Ferozsons', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Next Pharma', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Wilsons', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Macter', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Tagoor', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Medisure', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Amson', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Samipharma', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Sinopak', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    {'Client': 'Searle', 'Country': 'Pakistan', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Key PPI buyer'},
    
    # Bangladesh
    {'Client': 'SKYRUN Corp', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Agent', 'Channel / agent': 'Indenter Agreement', 'Contact person': 'Robin / Kamrul', 'Next action / owner': 'Verify volume'},
    {'Client': 'Al Bion Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Ibn Sina', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Al Madina Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Team Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Salton Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Silco Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Labaid Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Euro Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Popular Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Rangs Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Bio Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Silva Pharma', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Prospect', 'Key facts from files': 'Target account from Dhaka trip'},
    {'Client': 'Opsonin', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Tier-1 buyer'},
    {'Client': 'Navana', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Tier-1 buyer'},
    {'Client': 'Square', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Tier-1 buyer'},
    {'Client': 'Acme', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Tier-1 buyer'},
    {'Client': 'Incepta', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Tier-1 buyer'},
    {'Client': 'Beximco', 'Country': 'Bangladesh', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Tier-1 buyer'},
    
    # Indonesia
    {'Client': 'SSN Chemicals / PT Novell', 'Country': 'Indonesia', 'Region': 'Asia', 'Role': 'Agent'},
    {'Client': 'SKA Trading', 'Country': 'Indonesia', 'Region': 'Asia', 'Role': 'Agent', 'Contact person': 'Sita'},
    {'Client': 'Dexa Group', 'Country': 'Indonesia', 'Region': 'Asia', 'Role': 'Customer'},
    {'Client': 'PT Satia', 'Country': 'Indonesia', 'Region': 'Asia', 'Role': 'Customer', 'Key facts from files': 'Shipping live - 3,150 kg Jakarta'},
    
    # Lebanon
    {'Client': 'UBSA Pharma', 'Country': 'Lebanon', 'Region': 'MENA', 'Role': 'Customer', 'Contact person': 'Omar Sayed / Siham Charmand / Reina Ardati', 'Key facts from files': 'Best-quality account, repeat orders'},
    {'Client': 'Pharmaline S.A.L.', 'Country': 'Lebanon', 'Region': 'MENA', 'Role': 'Prospect'},
    
    # Yemen
    {'Client': 'MAF Pharma', 'Country': 'Yemen', 'Region': 'MENA', 'Role': 'Prospect', 'Key facts from files': 'Payment-delay prone'},
    {'Client': 'Raidah', 'Country': 'Yemen', 'Region': 'MENA', 'Role': 'Prospect', 'Key facts from files': 'Payment-delay prone'},
    {'Client': 'Shaphaco', 'Country': 'Yemen', 'Region': 'MENA', 'Role': 'Prospect', 'Key facts from files': 'Payment-delay prone'},
    {'Client': 'Pharma Care', 'Country': 'Yemen', 'Region': 'MENA', 'Role': 'Prospect', 'Key facts from files': 'Payment-delay prone'},
    
    # Palestine
    {'Client': 'Actico.net / Beit Jala', 'Country': 'Palestine', 'Region': 'MENA', 'Role': 'Agent', 'Contact person': 'Dr. Shatha al Jayyousi'},
    
    # Malaysia
    {'Client': 'Afiq Pharma', 'Country': 'Malaysia', 'Region': 'Asia', 'Role': 'Agent'},
    
    # Egypt
    {'Client': 'AlaqsaChem', 'Country': 'Egypt', 'Region': 'MENA', 'Role': 'Prospect', 'Contact person': 'Amr Salah', 'Key facts from files': 'CPHI lead, agency proposal for Egypt'},
    
    # Others
    {'Client': 'Grand Pharma', 'Country': 'Global/CPHI', 'Region': 'Global', 'Role': 'Prospect', 'Contact person': 'Michael', 'Key facts from files': 'CPHI lead, Ophthalmology and Cardiology'},
]

# Convert new records to DataFrame
df_new = pd.DataFrame(new_records)

# Avoid duplicates based on Client name
df_master = pd.concat([df_master, df_new], ignore_index=True).drop_duplicates(subset=['Client'], keep='last')

# Generate IDs for new clients (C001, C002...)
# We only update IDs for rows that don't have one
df_master['ID'] = df_master['ID'].fillna(lambda x: f"C{len(df_master)+1:03d}") # This is a bit naive, let's fix it
# Correct ID generation
existing_ids = df_master['ID'].dropna().astype(str)
max_id = 0
for eid in existing_ids:
    try:
        max_id = max(max_id, int(eid[1:]))
    except:
        pass

current_id = max_id + 1
def fill_id(row):
    if pd.isna(row['ID']):
        return f"C{current_id:03d}"
    return row['ID']

# This doesn't work inside apply because current_id needs to increment
ids = []
for val in df_master['ID']:
    if pd.isna(val):
        ids.append(f"C{current_id:03d}")
        current_id += 1
    else:
        ids.append(val)
df_master['ID'] = ids

# Update the Excel file
# Since we can't easily write back to specific sheets in an existing file without overwriting,
# we'll use ExcelWriter.
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_master.to_excel(writer, sheet_name='Client_Master', index=False)

print("Successfully updated Client_Master sheet in Excel file.")
