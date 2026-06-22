import pandas as pd

df = pd.read_excel(r"D:\DATA-ANALSI\Final_Project\Superstore Sales Dataset.xlsx")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Handle missing postal codes
df["Postal_Code"] = df["Postal_Code"].fillna("UNKNOWN").astype(str)

# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["Order_Date", "Ship_Date"])

# Keep only valid shipping records
df = df[df["Ship_Date"] >= df["Order_Date"]]

# Remove duplicates
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

# Feature engineering
df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month
df["Ship_Days"] = (df["Ship_Date"] - df["Order_Date"]).dt.days

# Export cleaned file
df.to_csv(r"D:\DATA-ANALSI\Final_Project\Superstore_Cleaned.csv", index=False)

print("Cleaning Complete!")
print(f"Rows: {df.shape[0]}")
print(f"Duplicates Removed: {duplicates}")
