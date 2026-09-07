# UPI Payment Failure Analytics & Anomaly Detection

An end-to-end data analytics project evaluating 250,000 UPI transactions to analyze transaction behaviors, investigate payment failures, detect statistical anomalies, test feature relationships, and evaluate predictive failure modeling.

---

## Dashboard Preview

An interactive Microsoft Excel dashboard leveraging PivotTables, PivotCharts, and cross-filtering Slicers to analyze volume by bank, hour, network type, and geographical distribution.

---

## Executive Summary

Digital payment systems process massive transactional volumes daily, making real-time performance monitoring and failure detection crucial for operational efficiency. This project covers a complete end-to-end data analytics pipeline—transitioning from raw transactional data to data quality auditing, exploratory analysis, hypothesis testing, anomaly detection, machine learning, SQL queries, and an interactive executive Excel dashboard.

| Metric | Value |
| --- | --- |
| **Total Transactions** | 250,000 |
| **Successful Transactions** | 237,624 |
| **Failed Transactions** | 12,376 |
| **Baseline Failure Rate** | 4.95% |
| **Chi-Square Test (Network vs. Status)** | Not Statistically Significant ($p > 0.05$) |
| **Chi-Square Test (Type vs. Status)** | Not Statistically Significant ($p > 0.05$) |
| **Logistic Regression ROC-AUC** | 0.50 (Random Guessing Baseline) |

---

## Key Technical Insights

Chi-Square independence tests revealed no statistically significant association between network types (or transaction types) and transaction failures. This proves that visual variations in raw volume do not always indicate true underlying operational bias.

A Logistic Regression model trained on high-level transaction metadata yielded a ROC-AUC score of 0.50, performing no better than random guessing. This highlights severe class imbalance issues and demonstrates that metadata alone is insufficient; operational telemetries such as gateway server load, latency, and response codes are necessary for actionable failure forecasting.

Z-score analysis successfully flagged extreme transaction amounts and localized behavioral deviations for deeper fraud and failure investigation.

---

## Analytical Workflow

```text
  ┌──────────────────────┐
  │  Raw Data Extraction │ (250,000 Records, 17 Features)
  └──────────┬───────────┘
             │
             ▼
  ┌──────────────────────┐
  │ Data Quality Audit   │ (Zero missing values, duplicates, or ID collisions)
  └──────────┬───────────┘
             │
             ▼
  ┌──────────────────────┐
  │  Exploratory Analysis│ (Bank, State, Hourly, & Network distribution)
  └──────────┬───────────┘
             │
             ▼
  ┌──────────────────────┐
  │ Statistical Testing  │ (Chi-Square Tests for feature independence)
  └──────────┬───────────┘
             │
             ▼
  ┌──────────────────────┐
  │  Anomaly Detection   │ (Z-Score calculation for outlier volume/amounts)
  └──────────┬───────────┘
             │
             ▼
  ┌──────────────────────┐
  │ Predictive Modeling  │ (Logistic Regression & ROC-AUC Evaluation)
  └──────────┬───────────┘
             │
             ▼
  ┌──────────────────────┐
  │   SQL & Dashboard    │ (MySQL aggregation & Interactive Excel Dashboard)
  └──────────────────────┘

```

---

## Repository Structure

```text
UPI-Payment-Failure-Analytics/
│
├── data/
│   ├── raw/
│   │   └── upi_transactions.csv
│   └── processed/
│       └── upi_transactions_clean.csv
│
├── python/
│   ├── 01_data_quality_check.py
│   ├── 02_eda.py
│   ├── 03_statistical_analysis.py
│   ├── 04_anomaly_detection.py
│   └── 05_failure_prediction.py
│
├── sql/
│   └── upi_analysis.sql
│
├── dashboard/
│   └── UPI_Payment_Failure_Analytics.xlsx
│
├── images/
│   └── dashboard.png
│
├── requirements.txt
└── README.md

```

---

## Tech Stack

| Domain | Tools & Technologies |
| --- | --- |
| **Programming & Libraries** | Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy, Scikit-learn) |
| **Database & Querying** | MySQL |
| **Business Intelligence** | Microsoft Excel (PivotTables, PivotCharts, Slicers) |
| **Version Control** | Git, GitHub |

---

## Author & Connect

**Moin Farooqui**

*Data Analytics | Python | SQL | Data Visualization*
