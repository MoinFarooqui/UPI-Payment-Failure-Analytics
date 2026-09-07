USE upi_payment_analytics ;

SELECT *
FROM upi_transactions
LIMIT 10;

SELECT transaction_id , amount_inr , device_type
FROM upi_transactions; 


SELECT transaction_id , receiver_bank , sender_bank, device_type , network_type 
FROM upi_transactions 
LIMIT 10 ;

SELECT transaction_id as Total_Transaction
FROM upi_transactions 
LIMIT 15 ;

SELECT DISTINCT device_type 
FROM upi_transactions ;

SELECT COUNT(*) AS total_number_of_transactions 
FROM upi_transactions ; 

SELECT MAX(amount_inr) AS big 
FROM upi_transactions ;

SELECT  *
FROM upi_transactions 
WHERE transaction_type = "P2P" ;


SELECT *
FROM upi_transactions 
WHERE merchant_category = "Fuel"
AND amount_inr<1000 ;

SELECT *
FROM upi_transactions
WHERE sender_state LIKE "M%";

SELECT *
FROM upi_transactions
WHERE sender_bank = "SBI"
OR "HDFC" ;


SELECT *
FROM upi_transactions 
WHERE sender_state IN ("Delhi","Gujarat","Rajasthan");


SELECT *
FROM upi_transactions
WHERE amount_inr BETWEEN 500 AND 1000 ;

SELECT sender_state , COUNT(*) As NUMBER_OF_Transactions
FROM upi_transactions
GROUP BY sender_state ;

SELECT sender_state , COUNT(*) AS NumOfTransAbove30000
FROM upi_transactions
GROUP BY sender_state 
HAVING COUNT(*)>30000 ;



#Q1Find all transactions where the amount is greater than ₹5,000.

select amount_inr as AmountGreaterThan5000
FROM upi_transactions
where amount_inr>5000 ;


#Q2Find all failed transactions made using a 4G network.

select transaction_status ,network_type
FROM upi_transactions 
where transaction_status="FAILED" And network_type = "4G";

#Q3Find all successful transactions where the amount is greater than ₹10,000.

select transaction_status , amount_inr
FROM upi_transactions 
where transaction_status = "SUCCESS" and amount_inr>10000;

#Q4Find transactions where the network is either 3G or WiFi.

select transaction_id , network_type
FROM upi_transactions
where network_type = "3G" OR 
network_type= "WiFi" ;

#Q5Find transactions from SBI, HDFC, or ICICI.

select sender_bank, transaction_id
FROM upi_transactions 
where sender_bank in ("SBI","HDFC","ICICI");

#Q6Find transactions with an amount between ₹1,000 and ₹5,000.

select transaction_id ,amount_inr
FROM upi_transactions
where amount_inr between 1000 and 5000 ;


#Q8Find banks whose names start with the letter I.

select sender_bank as bankname 
FROM upi_transactions
where sender_bank like "I%" ;


#Q10Find the highest transaction amount.

select max(amount_inr) as BIG
from upi_transactions ;

#Q11Find the lowest transaction amount.
#same just replace max with min 


#Q12Find the average transaction amount.

select avg(amount_inr)
FROM upi_transactions ;

#Q13Find the total value of all transactions.

select sum(amount_inr)
FROM upi_transactions ;

#Q14Count the total number of failed transactions.

SELECT COUNT(*) AS failed_transactions
FROM upi_transactions
WHERE transaction_status = 'FAILED';


#Q15Count the total number of successful transactions.

SELECT COUNT(*) AS success_transactions
FROM upi_transactions
WHERE transaction_status = 'SUCCESS';


#Q16Find the total number of transactions for each sender bank.

SELECT sender_bank , count(*) as TotalTransByEachBank
FROM upi_transactions 
group by sender_bank ;

#Q17Find the average transaction amount for each transaction type.

select transaction_type, avg(amount_inr) 
from upi_transactions 
group by transaction_type;

#Q18Find the total transaction value for each sender state.

select sender_state, sum(amount_inr) as state_total
from upi_transactions 
group by sender_state ;



#Q19Find sender banks that have more than 30,000 transactions.

select sender_bank , count(*) as morethan30000transactions 
from upi_transactions 
group by sender_bank 
having count(*) > 30000 ; 

#Q20 Find transaction types where the average transaction amount is greater than ₹1,500.

SELECT transaction_type,
       AVG(amount_inr) AS average_transaction_amount
FROM upi_transactions
GROUP BY transaction_type
HAVING AVG(amount_inr) > 1500; 



####################



SELECT
    transaction_id,
    amount_inr,
    CASE
        WHEN amount_inr < 500 THEN 'Low Value'
        WHEN amount_inr BETWEEN 500 AND 2000 THEN 'Medium Value'
        ELSE 'High Value'
    END as transaction_category 
FROM upi_transactions
LIMIT 10;



select fraud_flag , transaction_id ,
CASE  
when fraud_flag = 1
 then 'FRAUD'
else 'GENINUNE' 
end as FRAUD_CATEGORY  
from upi_transactions ;



SELECT
    SUM(CASE
        WHEN transaction_status = 'SUCCESS' THEN 1
        ELSE 0
    END) AS successful_transactions,

    SUM(CASE
        WHEN transaction_status = 'FAILED' THEN 1
        ELSE 0
    END) AS failed_transactions
FROM upi_transactions ;



select 
count(case when transaction_status = 'SUCCESS' then 1 end  ) as transaction_completedd ,
count(case when transaction_status = 'FAILED' then 1 end ) as transaction_failedd
from upi_transactions ;


SELECT
    transaction_id,
    amount_inr,
    CASE
        WHEN amount_inr < 1000 THEN 'Low Value'
        WHEN amount_inr BETWEEN 1000 AND 5000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS transaction_category
FROM upi_transactions;



create table bank_details(
bank_name varchar (50) primary key, 
bank_category varchar (30));


insert into bank_details (bank_name , bank_category)
values 
('SBI', 'Public Sector'),
('HDFC', 'Private Sector'),
('ICICI', 'Private Sector'),
('Axis', 'Private Sector'),
('PNB', 'Public Sector'),
('Kotak', 'Private Sector'),
('IndusInd', 'Private Sector'),
('Yes Bank', 'Private Sector');


SELECT
    t.transaction_id,
    t.sender_bank,
    b.bank_category,
    t.amount_inr,
    t.transaction_status
FROM upi_transactions AS t
INNER JOIN bank_details AS b
    ON t.sender_bank = b.bank_name
LIMIT 10;



SELECT
    t.transaction_id,
    t.sender_bank,
    b.bank_category,
    t.amount_inr
FROM upi_transactions AS t
LEFT JOIN bank_details AS b
    ON t.sender_bank = b.bank_name
LIMIT 10;




SELECT
    b.bank_category,
    COUNT(t.transaction_id) AS total_transactions,
    ROUND(AVG(t.amount_inr), 2) AS average_transaction_amount,
    SUM(
        CASE
            WHEN t.transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failed_transactions
FROM bank_details AS b
LEFT JOIN upi_transactions AS t
    ON b.bank_name = t.sender_bank
GROUP BY b.bank_category
ORDER BY total_transactions DESC;



WITH bank_transactions AS (
    SELECT
        sender_bank,
        COUNT(*) AS total_transactions
    FROM upi_transactions
    GROUP BY sender_bank
)

SELECT *
FROM bank_transactions
WHERE total_transactions > (
    SELECT AVG(total_transactions)
    FROM bank_transactions
);




SELECT
    sender_bank,
    COUNT(*) AS total_transactions,
    RANK() OVER (
        ORDER BY COUNT(*) DESC
    ) AS bank_rank
FROM upi_transactions
GROUP BY sender_bank;




#1: Overall KPIs

SELECT 
    COUNT(*) AS total_transactions,
    SUM(CASE
        WHEN transaction_status = 'SUCCESS' THEN 1
        ELSE 0
    END) AS successful_transactions,
    SUM(CASE
        WHEN transaction_status = 'FAILED' THEN 1
        ELSE 0
    END) AS failed_transactions,
    ROUND(100.0 * SUM(CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END) / COUNT(*),
            2) AS failure_rate_percentage,
    ROUND(SUM(amount_inr), 2) AS total_transaction_value,
    ROUND(AVG(amount_inr), 2) AS average_transaction_value
FROM
    upi_transactions;
    
    
    
    
    #2: Failure Rate by Sender Bank
    
    
    SELECT
    sender_bank,
    COUNT(*) AS total_transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failed_transactions,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS failure_rate_percentage

FROM upi_transactions
GROUP BY sender_bank
ORDER BY failure_rate_percentage DESC;


#3:Transaction Performance by Network

SELECT
    network_type,
    COUNT(*) AS total_transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failed_transactions,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS failure_rate_percentage

FROM upi_transactions
GROUP BY network_type
ORDER BY failure_rate_percentage DESC;


#4:Peak Transaction Hours

SELECT
    hour_of_day,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS transaction_value
FROM upi_transactions
GROUP BY hour_of_day
ORDER BY total_transactions DESC;

#5: Transaction Type Analysis

SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(AVG(amount_inr), 2) AS average_transaction_amount,
    ROUND(SUM(amount_inr), 2) AS total_transaction_value
FROM upi_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

#6:State-Wise Transaction Analysis

SELECT
    sender_state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_transaction_value,
    ROUND(AVG(amount_inr), 2) AS average_transaction_amount
FROM upi_transactions
GROUP BY sender_state
ORDER BY total_transaction_value DESC;


