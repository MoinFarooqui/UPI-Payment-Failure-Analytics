import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)


# ============================================
# 1. LOAD DATA
# ============================================

file_path = "data/processed/upi_transactions_clean.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ============================================
# 2. CREATE TARGET VARIABLE
# ============================================

df["failure_flag"] = (
    df["transaction_status"] == "FAILED"
).astype(int)


print("\n" + "=" * 60)
print("TARGET DISTRIBUTION")
print("=" * 60)

print(df["failure_flag"].value_counts())

print("\nFailure rate:")
print(f"{df['failure_flag'].mean() * 100:.2f}%")


# ============================================
# 3. SELECT FEATURES
# ============================================

features = [
    "amount_inr",
    "hour_of_day",
    "is_weekend",
    "transaction_type",
    "merchant_category",
    "sender_age_group",
    "receiver_age_group",
    "sender_state",
    "sender_bank",
    "receiver_bank",
    "device_type",
    "network_type",
    "fraud_flag"
]

X = df[features]

y = df["failure_flag"]


# ============================================
# 4. DEFINE FEATURE TYPES
# ============================================

numeric_features = [
    "amount_inr",
    "hour_of_day",
    "is_weekend",
    "fraud_flag"
]

categorical_features = [
    "transaction_type",
    "merchant_category",
    "sender_age_group",
    "receiver_age_group",
    "sender_state",
    "sender_bank",
    "receiver_bank",
    "device_type",
    "network_type"
]


# ============================================
# 5. PREPROCESSING
# ============================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# ============================================
# 6. CREATE LOGISTIC REGRESSION MODEL
# ============================================

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),

        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ]
)


# ============================================
# 7. TRAIN / TEST SPLIT
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 60)
print("TRAIN / TEST SPLIT")
print("=" * 60)

print(f"Training rows: {len(X_train):,}")
print(f"Testing rows : {len(X_test):,}")


# ============================================
# 8. TRAIN MODEL
# ============================================

print("\nTraining Logistic Regression...")

model.fit(
    X_train,
    y_train
)

print("Model training completed.")


# ============================================
# 9. PREDICTIONS
# ============================================

y_pred = model.predict(X_test)

y_probability = model.predict_proba(
    X_test
)[:, 1]


# ============================================
# 10. MODEL EVALUATION
# ============================================

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

print(
    classification_report(
        y_test,
        y_pred
    )
)


print("\n" + "=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


print("\n" + "=" * 60)
print("ROC-AUC SCORE")
print("=" * 60)

roc_auc = roc_auc_score(
    y_test,
    y_probability
)

print(f"ROC-AUC: {roc_auc:.4f}")
# ============================================
# 11. FAILURE VS SUCCESS FEATURE COMPARISON
# ============================================

print("\n" + "=" * 60)
print("SUCCESS vs FAILURE COMPARISON")
print("=" * 60)

comparison = df.groupby("transaction_status").agg(
    average_amount=("amount_inr", "mean"),
    average_hour=("hour_of_day", "mean"),
    fraud_rate=("fraud_flag", "mean")
)

print(comparison)


print("\n" + "=" * 60)
print("NETWORK DISTRIBUTION")
print("=" * 60)

network_comparison = pd.crosstab(
    df["network_type"],
    df["transaction_status"],
    normalize="columns"
) * 100

print(network_comparison)


print("\n" + "=" * 60)
print("DEVICE DISTRIBUTION")
print("=" * 60)

device_comparison = pd.crosstab(
    df["device_type"],
    df["transaction_status"],
    normalize="columns"
) * 100

print(device_comparison)