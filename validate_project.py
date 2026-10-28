"""Load CSV into SQLite, run queries and compare delivered results."""
import csv, sqlite3, json
from pathlib import Path
from generate_data import generate, HEADERS
root=Path(__file__).resolve().parents[1]
with (root/'data/smartphone_sales.csv').open(newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==150000 and len({r['sale_id'] for r in rows})==150000
for r,g in zip(rows,generate()):
    assert [r[h] for h in HEADERS]==[str(x) for x in g]
    assert '2026-01-01'<=r['sale_date']<='2026-09-30'
    assert abs(float(r['net_revenue_usd'])-round(int(r['units'])*float(r['unit_price_usd'])*(1-float(r['discount_pct'])),2))<.001
db=sqlite3.connect(':memory:');db.executescript((root/'sql/01_schema.sql').read_text())
db.executemany('INSERT INTO sales VALUES (?,?,?,?,?,?,?,?,?,?,?)',[[r[h] for h in HEADERS] for r in rows])
expected=json.loads((root/'results/summary.json').read_text());checks=0
for statement in (root/'sql/02_analysis.sql').read_text().split(';'):
    if 'SELECT' not in statement: continue
    name=next(n for n in expected if '-- '+n in statement)
    cur=db.execute(statement); cols=[c[0] for c in cur.description]
    result=[dict(zip(cols,r)) for r in cur.fetchall()]
    assert result==expected[name]
    with (root/f'results/{name}.csv').open(newline='') as f: actual_csv=list(csv.DictReader(f))
    assert actual_csv==[{k:str(v) for k,v in r.items()} for r in result]
    checks+=1
assert checks==6
print('PASS: 150,000 records; unique IDs; reproducible data; revenue arithmetic; date bounds; 6 verified query outputs.')
