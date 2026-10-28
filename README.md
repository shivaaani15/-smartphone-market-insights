# Smartphone Market Insights

Independent, AI-assisted portfolio case study using **150,000 synthetic sales records**. SQL analysis is complete and reproducible. Power BI setup guide and DAX measures are provided; dashboard construction is pending.

## Business question
How do sales revenue, units, product mix and age-group purchasing patterns vary across brands, regions, channels and months in a fictional smartphone retailer?

## Dataset
One row is one sale record, not one unique customer. Jan-Sep 2026; USD assumed. Fictional brands Aster, Nova and Orion prevent confusion with actual market shares. Columns: sale_id, sale_date, brand, model, region, age_group, channel, units, unit_price_usd, discount_pct and net_revenue_usd.

Revenue = units x unit price x (1 - discount). Revenue per unit = total net revenue / total units. Age_group is synthetic and cannot identify customers. The dataset does not establish market-wide demand, unique customer behaviour, actual brand performance or causal effects. Seed 71 and full generation rules are in scripts/generate_data.py. Higher-price brands can lead revenue without leading unit share.

## Verified sample results
- Sales records: 150,000
- Units sold: 177,293
- Net revenue: USD 91,542,061.60
- Revenue per unit: USD 516.33
- Highest revenue brand in this simulation: Orion (USD 43,947,386.25).

These are properties of the simulated dataset, not actual market insights. Random demographic groups do not justify targeted campaign recommendations or a measured decision-making improvement.

## Files
- data/smartphone_sales.csv: all 150,000 records.
- sql/01_schema.sql: table structure.
- sql/02_analysis.sql: six portable queries for KPIs, brands, months, age groups, channels and regions.
- results/: verified CSV outputs and JSON summary.
- scripts/generate_data.py: reproducible data generation.
- scripts/validate_project.py: creates an in-memory SQLite database and validates the deliverables.
- powerbi/: four DAX measures and dashboard build guide. **No PBIX supplied.**

## Run
Requires Python 3, standard library only. From this repository folder:
```bash
python scripts/validate_project.py
```
The script loads all data, executes the SQL and compares the exported results. No database credentials or software installation beyond Python is required. To regenerate the same CSV: `python scripts/generate_data.py`.

For MySQL, create/select a dedicated database, run sql/01_schema.sql, import the CSV into sales with the header excluded and types matching the schema, then run sql/02_analysis.sql. SQLite execution is verified; MySQL execution is not tested here. A 150,000-row CSV may exceed online SQL editor limits, so use the Python validator locally or import into a local database.

## Attribution and resume wording
AI assisted with dataset generation, SQL and documentation. This is independent portfolio work, not employer/client work. Review and run the code before presenting it.

Suggested current bullet: Analysed 150,000 synthetic smartphone sales records using SQL to compare brand revenue, monthly trends and demographic purchasing patterns; documented reproducible checks and Power BI measures.

Add a dashboard bullet only after completing the Power BI guide. No measured 25% improvement or real customer impact is claimed.
