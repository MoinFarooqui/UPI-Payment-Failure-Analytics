import pandas as pd
from scipy.stats import chi2_contingency

# ============================================
# 1. LOAD DATA
# ============================================

file_path = "data/processed/upi_transactions_clean.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")


# ============================================
# 2. CREATE CONTINGENCY TABLE
# ============================================

contingency_table = pd.crosstab(
    df["network_type"],
    df["transaction_status"]
)

print("\n" + "=" * 60)
print("CONTINGENCY TABLE")
print("=" * 60)

print(contingency_table)


# ============================================
# 3. CHI-SQUARE TEST
# ============================================

chi2, p_value, degrees_of_freedom, expected = chi2_contingency(
    contingency_table
)


# ============================================
# 4. DISPLAY RESULTS
# ============================================

print("\n" + "=" * 60)
print("CHI-SQUARE TEST RESULTS")
print("=" * 60)

print(f"Chi-Square Statistic : {chi2:.4f}")
print(f"P-Value              : {p_value:.10f}")
print(f"Degrees of Freedom   : {degrees_of_freedom}")


# ============================================
# 5. INTERPRETATION
# ============================================

alpha = 0.05

print("\n" + "=" * 60)
print("STATISTICAL CONCLUSION")
print("=" * 60)

if p_value < alpha:
    print("Result: Reject the null hypothesis.")
    print(
        "There is statistically significant evidence "
        "of an association between network type "
        "and transaction status."
    )
else:
    print("Result: Fail to reject the null hypothesis.")
    print(
        "There is not enough statistical evidence "
        "to conclude that network type and "
        "transaction status are associated."
    )
# ============================================
# 6. CHI-SQUARE TEST:
# TRANSACTION TYPE VS TRANSACTION STATUS
# ============================================

transaction_type_table = pd.crosstab(
    df["transaction_type"],
    df["transaction_status"]
)

print("\n" + "=" * 60)
print("TRANSACTION TYPE vs TRANSACTION STATUS")
print("=" * 60)

print(transaction_type_table)


chi2_type, p_value_type, dof_type, expected_type = chi2_contingency(
    transaction_type_table
)


print("\n" + "=" * 60)
print("CHI-SQUARE RESULTS")
print("=" * 60)

print(f"Chi-Square Statistic : {chi2_type:.4f}")
print(f"P-Value              : {p_value_type:.10f}")
print(f"Degrees of Freedom   : {dof_type}")


print("\n" + "=" * 60)
print("STATISTICAL CONCLUSION")
print("=" * 60)

if p_value_type < alpha:
    print("Result: Reject the null hypothesis.")
    print(
        "There is statistically significant evidence "
        "of an association between transaction type "
        "and transaction status."
    )
else:
    print("Result: Fail to reject the null hypothesis.")
    print(
        "There is not enough statistical evidence "
        "to conclude that transaction type and "
        "transaction status are associated."
    )
# ============================================
# 7. CRAMER'S V EFFECT SIZE
# ============================================

def cramers_v(table, chi2):
    n = table.to_numpy().sum()
    rows, columns = table.shape

    minimum_dimension = min(rows - 1, columns - 1)

    return np.sqrt(
        chi2 / (n * minimum_dimension)
    )


# Network Type Effect Size

network_cramers_v = cramers_v(
    contingency_table,
    chi2
)


# Transaction Type Effect Size

transaction_type_cramers_v = cramers_v(
    transaction_type_table,
    chi2_type
)


print("\n" + "=" * 60)
print("EFFECT SIZE — CRAMÉR'S V")
print("=" * 60)

print(
    f"Network Type vs Transaction Status : "
    f"{network_cramers_v:.4f}"
)

print(
    f"Transaction Type vs Transaction Status : "
    f"{transaction_type_cramers_v:.4f}"
)