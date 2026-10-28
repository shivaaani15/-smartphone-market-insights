"""Generate fictional sales for portfolio practice. Python 3, no dependencies."""
import csv, random
from datetime import date,timedelta
from pathlib import Path
HEADERS=['sale_id','sale_date','brand','model','region','age_group','channel','units','unit_price_usd','discount_pct','net_revenue_usd']
def generate():
    rng=random.Random(71)
    catalog=[('Aster','A1',249),('Aster','A2',449),('Nova','N1',349),('Nova','N2',699),('Orion','O1',599),('Orion','O2',999)]
    for i in range(1,150001):
        brand,model,price=rng.choice(catalog)
        dt=(date(2026,1,1)+timedelta(days=rng.randrange(273))).isoformat()
        region=rng.choice(['North','South','East','West'])
        age=rng.choice(['18-24','25-34','35-44','45-54','55+'])
        channel=rng.choice(['Online','Retail'])
        units=rng.choices([1,2,3],[.85,.12,.03])[0]
        discount=rng.choice([0,.05,.10,.15])
        revenue=round(units*price*(1-discount),2)
        yield [i,dt,brand,model,region,age,channel,units,price,discount,revenue]
if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]
    with (root/'data/smartphone_sales.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(HEADERS);w.writerows(generate())
    print('150,000 synthetic sale records generated, seed 71.')
