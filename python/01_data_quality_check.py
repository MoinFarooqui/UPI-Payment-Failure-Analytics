import pandas as pd

# ============================================
# 1. LOAD RAW DATA
# ============================================

file_path = "data/raw/upi_transactions.csv"

df = pd.read_csv(file_path)

print("Raw dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ============================================
# 2. DATA TYPE CONVERSION
# ============================================

df["timestamp"] = pd.to_datetime(df["timestamp"])


# ============================================
# 3. CREATE DERIVED TIME FEATURES
# ============================================

df["hour_of_day"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.day_name()

df["is_weekend"] = df["timestamp"].dt.dayofweek >= 5
df["is_weekend"] = df["is_weekend"].astype(int)


# ============================================
# 4. STANDARDIZE COLUMN NAMES
# ============================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(inr)", "inr", regex=False)
)


# ============================================
# 5. SAVE PROCESSED DATA
# ============================================

output_path = "data/processed/upi_transactions_clean.csv"

df.to_csv(output_path, index=False)

print("\nProcessed dataset created successfully!")
print(f"Saved to: {output_path}")

print("\nFinal columns:")
print(df.columns.tolist())