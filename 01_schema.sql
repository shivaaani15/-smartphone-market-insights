CREATE TABLE sales (
 sale_id INT PRIMARY KEY, sale_date DATE NOT NULL,
 brand VARCHAR(20), model VARCHAR(20), region VARCHAR(20),
 age_group VARCHAR(10), channel VARCHAR(10), units INT,
 unit_price_usd DECIMAL(10,2), discount_pct DECIMAL(5,2),
 net_revenue_usd DECIMAL(14,2)
);
