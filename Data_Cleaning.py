import pandas as pd
import re

def parse_price(price_str):
    price_str = str(price_str).lower().replace(',', '').replace('\n', ' ').strip()
    match = re.search(r'([\d\.]+)\s*(crore|lakh)', price_str)
    if match:
        value = float(match.group(1))
        unit = match.group(2)
        if unit == 'crore':
            return int(value * 10000000)
        elif unit == 'lakh':
            return int(value * 100000)
    num_match = re.search(r'([\d]+)', price_str)
    if num_match:
        return int(num_match.group(1))
    return 0

def parse_area_to_sqft(area_str):
    area_str = str(area_str).lower().strip()
    match = re.search(r'([\d\.]+)\s*(kanal|marla)', area_str)
    if match:
        value = float(match.group(1))
        unit = match.group(2)
        if unit == 'kanal':
            return value * 4500
        elif unit == 'marla':
            return value * 225
    return 0

def clean_built_year(year_str):

    year_str = str(year_str).strip()
    if year_str == 'nan' or year_str == '' or year_str == 'N/A':
        return 0
    try:
        year_val = float(year_str)
        if 1980 <= year_val <= 2027:
            return int(year_val)
        else:
            return 0
    except:
        return 0

# --- MAIN CLEANING PIPELINE ---
print("Loading raw scraped data...")
df = pd.read_csv('zameen_data.csv')

print("Applying data conversions...")
df['Price_PKR'] = df['price'].apply(parse_price)
df['Area_SqFt'] = df['area'].apply(parse_area_to_sqft)

df['Beds_Num'] = df['beds'].astype(str).str.extract(r'(\d+)').fillna(0).astype(int)
df['Baths_Num'] = df['baths'].astype(str).str.extract(r'(\d+)').fillna(0).astype(int)

df['Built_Year_Clean'] = df['built_year'].apply(clean_built_year)

df_clean = df[(df['Price_PKR'] > 0) & (df['Area_SqFt'] > 0)].copy()
df_clean = df_clean[df_clean['Built_Year_Clean'] > 0]


df_clean = df_clean.drop(columns=['price', 'area', 'beds', 'baths', 'built_year'])


print(f"\nRows before cleaning: {len(df)}")
print(f"Rows after cleaning: {len(df_clean)}")
print(f"Rows removed: {len(df) - len(df_clean)}")

print("\n=== CLEAN DATASET PREVIEW ===")
print(df_clean.head())

# Save the cleaned dataset
df_clean.to_csv('zameen_data(2).csv', index=False)
print("\nSaved to 'zameen_data(2).csv'!")