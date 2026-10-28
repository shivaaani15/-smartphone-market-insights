# Power BI setup (not a delivered PBIX)

1. Import data/smartphone_sales.csv using Get Data > Text/CSV. Name the table sales.
2. Set sale_date to Date, sale_id and units to Whole Number, price and revenue to Fixed Decimal Number, discount_pct to Decimal Number. Set its display format to Percentage without multiplying the values.
3. Create the four measures from measures.dax. USD is an illustrative currency assumption.
4. Add cards for net revenue, units sold and revenue per unit. Add a brand revenue bar chart, monthly revenue line chart and region/age/channel slicers. Use sale_date grouped by year/month in chronological order.
5. Compare unfiltered cards to results/01_kpis.csv. Compare brand and month charts to their exported CSVs. Save as smartphone_market_insights.pbix and upload it after verification.

This guide and DAX measures are supplied; a Power BI dashboard has not been built or tested. No PBIX is included. Do not claim a completed Power BI dashboard until you build and verify it.
