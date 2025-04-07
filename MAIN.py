import pandas as pd

# Step 2: Load Data
df = pd.read_csv('marketing_campaign.csv')  # Replace with your actual file name

# Step 3: Check Data
print(df.info())
print(df.describe())
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Step 4: Clean the Data

# Handle missing values (use dropna() or fillna() as needed)
df.fillna(method='ffill', inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize text (example: Gender column)
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].astype(str).str.strip().str.lower()

# Convert date columns (example: 'Date' column) to datetime format
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%d-%m-%Y')

# Rename columns to lowercase with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Fix data types (example: age to int if exists)
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)

# Step 5: Save Cleaned Data
df.to_csv('cleaned_dataset.csv', index=False)

print("Data cleaning complete. Saved as 'cleaned_dataset.csv'.")
