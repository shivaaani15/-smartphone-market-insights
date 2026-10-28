-- 01_kpis
SELECT COUNT(*) AS sales_records, SUM(units) AS units_sold, ROUND(SUM(net_revenue_usd),2) AS net_revenue_usd, ROUND(SUM(net_revenue_usd)/SUM(units),2) AS revenue_per_unit_usd FROM sales;

-- 02_brand
SELECT brand, SUM(units) AS units_sold, ROUND(SUM(net_revenue_usd),2) AS net_revenue_usd FROM sales GROUP BY brand ORDER BY net_revenue_usd DESC;

-- 03_month
SELECT SUBSTR(sale_date,1,7) AS month, SUM(units) AS units_sold, ROUND(SUM(net_revenue_usd),2) AS net_revenue_usd FROM sales GROUP BY SUBSTR(sale_date,1,7) ORDER BY month;

-- 04_segment
SELECT age_group, brand, SUM(units) AS units_sold FROM sales GROUP BY age_group, brand ORDER BY age_group, units_sold DESC;

-- 05_channel
SELECT channel, COUNT(*) AS sales_records, SUM(units) AS units_sold, ROUND(SUM(net_revenue_usd),2) AS net_revenue_usd FROM sales GROUP BY channel ORDER BY channel;

-- 06_region
SELECT region, SUM(units) AS units_sold, ROUND(SUM(net_revenue_usd),2) AS net_revenue_usd FROM sales GROUP BY region ORDER BY net_revenue_usd DESC;
