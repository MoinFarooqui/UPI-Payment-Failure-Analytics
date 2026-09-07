import pandas as pd
import numpy as np

# ============================================
# 1. LOAD DATA
# ============================================

file_path = "data/processed/upi_transactions_clean.csv"

df = pd.read_csv(file_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

print("Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")


# ============================================
# 2. CREATE HOURLY TRANSACTION VOLUME
# ============================================

hourly_volume = (
    df.groupby(df["timestamp"].dt.floor("h"))
    .size()
    .reset_index(name="transaction_count")
)

print("\n" + "=" * 60)
print("HOURLY TRANSACTION VOLUME")
print("=" * 60)

print(hourly_volume.head())


# ============================================
# 3. CALCULATE Z-SCORE
# ============================================

mean_volume = hourly_volume["transaction_count"].mean()

std_volume = hourly_volume["transaction_count"].std()

hourly_volume["z_score"] = (
    (hourly_volume["transaction_count"] - mean_volume)
    / std_volume
)


# ============================================
# 4. FLAG ANOMALIES
# ============================================

threshold = 3

hourly_volume["is_anomaly"] = (
    hourly_volume["z_score"].abs() > threshold
)


# ============================================
# 5. DISPLAY SUMMARY
# ============================================

print("\n" + "=" * 60)
print("ANOMALY DETECTION SUMMARY")
print("=" * 60)

print(f"Average hourly transactions : {mean_volume:.2f}")
print(f"Standard deviation          : {std_volume:.2f}")
print(f"Anomaly threshold           : ±{threshold}")
print(
    f"Anomalous hours             : "
    f"{hourly_volume['is_anomaly'].sum()}"
)


# ============================================
# 6. DISPLAY ANOMALOUS HOURS
# ============================================

anomalies = hourly_volume[
    hourly_volume["is_anomaly"]
].sort_values(
    "z_score",
    ascending=False
)

print("\n" + "=" * 60)
print("ANOMALOUS HOURS")
print("=" * 60)

if anomalies.empty:
    print("No anomalies detected using |Z| > 3.")
else:
    print(anomalies.to_string(index=False))


# ============================================
# 7. SAVE RESULTS
# ============================================

output_path = "data/processed/hourly_transaction_anomalies.csv"

hourly_volume.to_csv(
    output_path,
    index=False
)

print("\n" + "=" * 60)
print("RESULT SAVED")
print("=" * 60)

print(f"Saved to: {output_path}")
# ============================================
# 8. ANALYZE ANOMALOUS HOURS
# ============================================

if not anomalies.empty:

    anomaly_times = anomalies["timestamp"].tolist()

    anomaly_transactions = df[
        df["timestamp"].dt.floor("h").isin(anomaly_times)
    ]

    print("\n" + "=" * 60)
    print("ANOMALY CHARACTERISTICS")
    print("=" * 60)

    print("\nTransaction Types:")
    print(
        anomaly_transactions["transaction_type"]
        .value_counts()
    )

    print("\nBanks:")
    print(
        anomaly_transactions["sender_bank"]
        .value_counts()
    )

    print("\nNetworks:")
    print(
        anomaly_transactions["network_type"]
        .value_counts()
    )

    print("\nTransaction Status:")
    print(
        anomaly_transactions["transaction_status"]
        .value_counts()
    )

    print("\nAverage Transaction Amount:")
    print(
        f"₹{anomaly_transactions['amount_inr'].mean():,.2f}"
    )

else:
    print("\nNo anomaly characteristics to analyze.")