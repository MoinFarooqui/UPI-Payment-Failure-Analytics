UPI Payment Failure Analytics – Project Report
1. Project Overview

This project analyzes UPI transaction data to identify transaction patterns, failure trends, and factors that may influence payment failures. The analysis combines Python, SQL, and Microsoft Excel to perform data quality checks, exploratory data analysis, statistical testing, anomaly detection, and transaction failure prediction.

2. Dataset Overview

The dataset contains 250,000 UPI transactions with information related to:

Transaction ID
Timestamp
Transaction Type
Merchant Category
Transaction Amount
Transaction Status
Sender and Receiver Age Groups
Sender State
Sender and Receiver Banks
Device Type
Network Type
Fraud Flag
Hour of Transaction
Day of Week
Weekend Indicator
3. Data Quality Analysis

The dataset was examined for data quality issues before performing further analysis.

Key findings:

Total Records: 250,000
Total Columns: 17
Missing Values: 0
Duplicate Rows: 0
Duplicate Transaction IDs: 0

The dataset was found to be clean and suitable for analysis.

4. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand transaction patterns and distributions.

The analysis explored:

Transaction status distribution
Transaction type distribution
Network usage patterns
Transaction amounts
Hourly transaction volume
Transaction volume by sender bank
Transaction value by state
5. Statistical Analysis

Chi-square tests were performed to investigate potential relationships between categorical variables and transaction status.

Network Type vs Transaction Status

The analysis produced a p-value greater than 0.05.

Conclusion: There was insufficient statistical evidence to conclude that network type and transaction status were significantly associated in this dataset.

Transaction Type vs Transaction Status

The analysis also produced a p-value greater than 0.05.

Conclusion: There was insufficient statistical evidence to conclude that transaction type and transaction status were significantly associated.

6. Anomaly Detection

Anomaly detection techniques were applied to identify unusual transaction patterns based on the available transaction data.

This analysis helps identify transactions that differ significantly from typical transaction behavior and can support further investigation.

7. Transaction Failure Prediction

A Logistic Regression model was developed to predict whether a UPI transaction would fail.

The dataset contained:

Successful Transactions: 237,624
Failed Transactions: 12,376
Overall Failure Rate: 4.95%

The initial model achieved a ROC-AUC score close to 0.50, indicating that the available features did not provide strong predictive power for transaction failures.

This finding is important because it demonstrates that high overall accuracy can be misleading when dealing with an imbalanced dataset. The model predicted the majority class effectively but struggled to identify failed transactions.

8. SQL Analysis

SQL queries were used to analyze transaction data and answer business-related questions.

Key areas included:

Transaction filtering
Aggregate analysis
Transaction failure analysis
Bank-wise transaction analysis
State-wise transaction analysis
Transaction type analysis
GROUP BY and HAVING operations
9. Excel Dashboard

An interactive Excel dashboard was developed to visualize key transaction insights.

The dashboard includes:

Total Transactions
Successful Transactions
Failed Transactions
Failure Rate
Transaction Volume by Sender Bank
Hourly Transaction Trends
Transaction Type Distribution
Transaction Volume by Network
Transaction Value by State

Interactive slicers were added for:

Sender State
Network Type
Transaction Type
10. Key Findings
The overall transaction failure rate was 4.95%.
Most transactions in the dataset were successful.
Transaction volume varied across different banks, states, networks, and transaction types.
Network type and transaction type did not demonstrate a statistically significant association with transaction status.
The failure prediction model showed limited predictive performance, suggesting that additional relevant features would be required for accurate failure prediction.
11. Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
SciPy
MySQL
Microsoft Excel
GitHub
12. Conclusion

The UPI Payment Failure Analytics project demonstrates an end-to-end data analytics workflow, beginning with data quality assessment and progressing through exploratory analysis, statistical testing, anomaly detection, predictive modeling, SQL analysis, and interactive dashboard development.

The project highlights both analytical insights and practical limitations. In particular, the failure prediction results demonstrate the challenges of class imbalance and the importance of evaluating machine learning models beyond accuracy alone.