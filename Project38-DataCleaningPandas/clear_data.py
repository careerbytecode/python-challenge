import pandas as pd

try:
    df = pd.read_csv("raw_data.csv", dtype=str)
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit(1)

print(f"Raw data shape: {df.shape}")

df['status'] = df['status'].fillna('UNKNOWN')

df = df.dropna(subset=['ip_address'])

df['created'] = pd.to_datetime(df['created'], errors='coerce')
df = df.dropna(subset=['created'])

df['ram_MB'] = pd.to_numeric(df['ram_MB'], errors='coerce')
df = df.dropna(subset=['ram_MB'])

Q1 = df['ram_MB'].quantile(0.25)
Q3 = df['ram_MB'].quantile(0.75)
IQR = Q3 - Q1
mask = (df['ram_MB'] >= Q1 - 1.5 * IQR) & (df['ram_MB'] <= Q3 + 1.5 * IQR)
df = df[mask]

for col in ['name', 'flavor', 'image']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
if 'name' in df.columns:
    df['name'] = df['name'].str.lower()
if 'flavor' in df.columns:
    df['flavor'] = df['flavor'].str.lower()
if 'image' in df.columns:
    df['image'] = df['image'].str.title()

df.to_csv("cleaned_instance_data.csv", index=False)
print("Cleaned data saved as 'cleaned_instance_data.csv'")
print(f"Cleaned data shape: {df.shape}")