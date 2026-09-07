import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================
# 1. LOAD PROCESSED DATA
# ============================================

file_path = "data/processed/upi_transactions_clean.csv"

df = pd.read_csv(file_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

print("Processed dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ============================================
# 2. BASIC BUSINESS KPIs
# ============================================

total_transactions = len(df)

successful_transactions = (df["transaction_status"] == "SUCCESS").sum()

failed_transactions = (df["transaction_status"] == "FAILED").sum()

success_rate = (successful_transactions / total_transactions) * 100

failure_rate = (failed_transactions / total_transactions) * 100

total_transaction_value = df["amount_inr"].sum()

average_transaction_value = df["amount_inr"].mean()


print("\n" + "=" * 60)
print("BUSINESS KPIs")
print("=" * 60)

print(f"Total Transactions       : {total_transactions:,}")
print(f"Successful Transactions  : {successful_transactions:,}")
print(f"Failed Transactions      : {failed_transactions:,}")
print(f"Success Rate             : {success_rate:.2f}%")
print(f"Failure Rate             : {failure_rate:.2f}%")
print(f"Total Transaction Value  : ₹{total_transaction_value:,.2f}")
print(f"Average Transaction Value: ₹{average_transaction_value:,.2f}")


# ============================================
# 3. FAILURE RATE BY TRANSACTION TYPE
# ============================================

transaction_type_analysis = (
    df.groupby("transaction_type")
    .agg(
        total_transactions=("transaction_id", "count"),
        failed_transactions=("transaction_status", lambda x: (x == "FAILED").sum())
    )
)

transaction_type_analysis["failure_rate"] = (
    transaction_type_analysis["failed_transactions"]
    / transaction_type_analysis["total_transactions"]
    * 100
)

transaction_type_analysis = transaction_type_analysis.sort_values(
    "failure_rate",
    ascending=False
)

print("\n" + "=" * 60)
print("FAILURE RATE BY TRANSACTION TYPE")
print("=" * 60)

print(transaction_type_analysis)


# ============================================
# 4. FAILURE RATE BY BANK
# ============================================

bank_analysis = (
    df.groupby("sender_bank")
    .agg(
        total_transactions=("transaction_id", "count"),
        failed_transactions=("transaction_status", lambda x: (x == "FAILED").sum())
    )
)

bank_analysis["failure_rate"] = (
    bank_analysis["failed_transactions"]
    / bank_analysis["total_transactions"]
    * 100
)

bank_analysis = bank_analysis.sort_values(
    "failure_rate",
    ascending=False
)

print("\n" + "=" * 60)
print("FAILURE RATE BY SENDER BANK")
print("=" * 60)

print(bank_analysis)


# ============================================
# 5. FAILURE RATE BY NETWORK
# ============================================

network_analysis = (
    df.groupby("network_type")
    .agg(
        total_transactions=("transaction_id", "count"),
        failed_transactions=("transaction_status", lambda x: (x == "FAILED").sum())
    )
)

network_analysis["failure_rate"] = (
    network_analysis["failed_transactions"]
    / network_analysis["total_transactions"]
    * 100
)

network_analysis = network_analysis.sort_values(
    "failure_rate",
    ascending=False
)

print("\n" + "=" * 60)
print("FAILURE RATE BY NETWORK")
print("=" * 60)

print(network_analysis)


# ============================================
# 6. FAILURE RATE BY DEVICE
# ============================================

device_analysis = (
    df.groupby("device_type")
    .agg(
        total_transactions=("transaction_id", "count"),
        failed_transactions=("transaction_status", lambda x: (x == "FAILED").sum())
    )
)

device_analysis["failure_rate"] = (
    device_analysis["failed_transactions"]
    / device_analysis["total_transactions"]
    * 100
)

device_analysis = device_analysis.sort_values(
    "failure_rate",
    ascending=False
)

print("\n" + "=" * 60)
print("FAILURE RATE BY DEVICE")
print("=" * 60)

print(device_analysis)


# ============================================
# 7. FAILURE RATE BY HOUR
# ============================================

hour_analysis = (
    df.groupby("hour_of_day")
    .agg(
        total_transactions=("transaction_id", "count"),
        failed_transactions=("transaction_status", lambda x: (x == "FAILED").sum())
    )
)

hour_analysis["failure_rate"] = (
    hour_analysis["failed_transactions"]
    / hour_analysis["total_transactions"]
    * 100
)

print("\n" + "=" * 60)
print("FAILURE RATE BY HOUR")
print("=" * 60)

print(hour_analysis)


# ============================================
# 8. FAILURE RATE BY WEEKEND
# ============================================

weekend_analysis = (
    df.groupby("is_weekend")
    .agg(
        total_transactions=("transaction_id", "count"),
        failed_transactions=("transaction_status", lambda x: (x == "FAILED").sum())
    )
)

weekend_analysis["failure_rate"] = (
    weekend_analysis["failed_transactions"]
    / weekend_analysis["total_transactions"]
    * 100
)

print("\n" + "=" * 60)
print("WEEKDAY VS WEEKEND")
print("=" * 60)

print(weekend_analysis)


# ============================================
# 9. TRANSACTION STATUS DISTRIBUTION
# ============================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="transaction_status"
)

plt.title("Transaction Status Distribution")
plt.xlabel("Transaction Status")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.show()


# ============================================
# 10. FAILURE RATE BY TRANSACTION TYPE
# ============================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=transaction_type_analysis.reset_index(),
    x="transaction_type",
    y="failure_rate"
)

plt.title("Failure Rate by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Failure Rate (%)")

plt.xticks(rotation=20)

plt.tight_layout()

plt.show()


# ============================================
# 11. FAILURE RATE BY HOUR
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(
    hour_analysis.index,
    hour_analysis["failure_rate"],
    marker="o"
)

plt.title("UPI Failure Rate by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Failure Rate (%)")

plt.xticks(range(24))

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()