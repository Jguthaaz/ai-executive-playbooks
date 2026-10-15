from pathlib import Path
import os, json, hashlib, urllib.request, zipfile, platform
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

SOURCE_URL = 'https://archive.ics.uci.edu/static/public/352/online+retail.zip'
OUTPUT = Path('/kaggle/working/customer-growth-output') if Path('/kaggle').exists() else Path('output')
OUTPUT.mkdir(parents=True, exist_ok=True)
explicit = os.environ.get('DATA_PATH')
candidates = sorted(Path('/kaggle/input').rglob('Online Retail.xlsx')) if Path('/kaggle/input').exists() else []
if explicit:
    data_path = Path(explicit)
elif len(candidates) == 1:
    data_path = candidates[0]
elif len(candidates) > 1:
    raise ValueError('Multiple source files found. Set DATA_PATH explicitly.')
else:
    cache = Path('data'); cache.mkdir(exist_ok=True)
    data_path = cache / 'Online Retail.xlsx'
    if not data_path.exists():
        archive = cache / 'online-retail.zip'
        urllib.request.urlretrieve(SOURCE_URL, archive)
        with zipfile.ZipFile(archive) as z:
            with z.open('Online Retail.xlsx') as source, data_path.open('wb') as target:
                target.write(source.read())
source_hash = hashlib.sha256(data_path.read_bytes()).hexdigest()
raw = pd.read_excel(data_path, engine='openpyxl')
required = {'InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'}
assert required <= set(raw.columns), 'Unexpected source schema'
assert len(raw) == 541909, 'This analysis expects the original UCI Online Retail file'
print('Source rows:', len(raw), '\nSHA256:', source_hash)
print('Versions:', {'python':platform.python_version(), 'pandas':pd.__version__, 'numpy':np.__version__, 'matplotlib':matplotlib.__version__})


diagnostics = pd.DataFrame([
    ['raw_rows',len(raw)], ['exact_duplicate_rows',int(raw.duplicated().sum())],
    ['missing_customer_id',int(raw.CustomerID.isna().sum())],
    ['cancellation_lines',int(raw.InvoiceNo.astype(str).str.upper().str.startswith('C').sum())],
    ['nonpositive_quantity',int((raw.Quantity <= 0).sum())],
    ['nonpositive_price',int((raw.UnitPrice <= 0).sum())],
    ['missing_description',int(raw.Description.isna().sum())]
],columns=['diagnostic','rows'])
waterfall = []
d = raw.copy()
def keep(frame, mask, reason):
    waterfall.append({'step':reason,'removed':int((~mask).sum()),'remaining':int(mask.sum())})
    return frame.loc[mask].copy()
d = keep(d, ~d.duplicated(), 'exact duplicates')
d = keep(d, d.CustomerID.notna(), 'missing customer ID')
d = keep(d, ~d.InvoiceNo.astype(str).str.upper().str.startswith('C'), 'cancellation invoices')
d = keep(d, (d.Quantity > 0) & (d.UnitPrice > 0), 'nonpositive quantity or price')
d['InvoiceDate'] = pd.to_datetime(d.InvoiceDate, errors='coerce')
d = keep(d, d.InvoiceDate.notna(), 'invalid dates')
START, END = pd.Timestamp('2010-12-01'), pd.Timestamp('2011-12-01')
d = keep(d, (d.InvoiceDate >= START) & (d.InvoiceDate < END), 'outside complete-month window')
d['CustomerID'] = d.CustomerID.astype('int64').astype(str)
d['InvoiceNo'] = d.InvoiceNo.astype(str)
d['PurchaseValue'] = d.Quantity * d.UnitPrice
d['Month'] = d.InvoiceDate.dt.to_period('M')
waterfall = pd.DataFrame(waterfall)
assert len(raw) - waterfall.removed.sum() == len(d)
assert not d.duplicated(subset=list(raw.columns)).any()
assert d.CustomerID.notna().all() and (d.PurchaseValue > 0).all()
print(diagnostics.to_string(index=False))
print('\nSequential exclusions:\n'+waterfall.to_string(index=False))
diagnostics.to_csv(OUTPUT/'quality-diagnostics.csv',index=False)
waterfall.to_csv(OUTPUT/'cleaning-waterfall.csv',index=False)


monthly = d.groupby('Month').agg(customers=('CustomerID','nunique'), orders=('InvoiceNo','nunique'), purchase_value_gbp=('PurchaseValue','sum'))
print(monthly.round(2).to_string())
monthly.to_csv(OUTPUT/'monthly-summary.csv')
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(monthly.index.astype(str),monthly.purchase_value_gbp/1000,marker='o',color='#176b87')
ax.set(title='Positive purchase value by complete month',ylabel='GBP thousands',xlabel='Month')
ax.tick_params(axis='x',rotation=45); fig.tight_layout()
fig.savefig(OUTPUT/'monthly-purchases.svg'); fig.savefig(OUTPUT/'monthly-purchases.png',dpi=120)
plt.show()


def make_rfm(frame, snapshot, active_days=60, lapsed_days=90, value_quantile=.75):
    r = frame.groupby('CustomerID').agg(last_purchase=('InvoiceDate','max'),frequency=('InvoiceNo','nunique'),monetary=('PurchaseValue','sum'))
    r['recency'] = (snapshot.normalize()-r.last_purchase.dt.normalize()).dt.days
    for col, ascending in [('recency',False),('frequency',True),('monetary',True)]:
        r[col+'_score'] = np.ceil(r[col].rank(method='average',pct=True,ascending=ascending)*5).clip(1,5).astype(int)
    threshold = r.monetary.quantile(value_quantile)
    r['segment'] = np.select([
        (r.recency<=active_days)&(r.frequency>=3)&(r.monetary>=threshold),
        (r.recency>lapsed_days)&(r.monetary>=threshold),
        (r.frequency==1)&(r.recency<=30),
        (r.frequency>=2)&(r.recency<=active_days)
    ], ['Active high value','Lapsed high value','Recent single purchase','Active repeat'],default='Other')
    return r, float(threshold)
rfm, value_threshold = make_rfm(d, END)
segments = rfm.groupby('segment').agg(customers=('frequency','size'),purchase_value_gbp=('monetary','sum'),median_recency=('recency','median'),median_orders=('frequency','median'))
segments['customer_share'] = segments.customers / len(rfm)
segments['value_share'] = segments.purchase_value_gbp / rfm.monetary.sum()
assert segments.customers.sum() == d.CustomerID.nunique()
assert np.isclose(segments.purchase_value_gbp.sum(), d.PurchaseValue.sum())
print('High-value threshold (GBP):',round(value_threshold,2))
print(segments.round(4).to_string())
segments.to_csv(OUTPUT/'segment-summary.csv')
fig, axes = plt.subplots(1,2,figsize=(12,4))
segments.customer_share.sort_values().plot.barh(ax=axes[0],color='#176b87')
segments.value_share.sort_values().plot.barh(ax=axes[1],color='#d18b2c')
axes[0].set(title='Share of customers',xlabel='Proportion',ylabel='')
axes[1].set(title='Share of positive purchase value',xlabel='Proportion',ylabel='')
fig.tight_layout(); fig.savefig(OUTPUT/'segment-shares.svg'); fig.savefig(OUTPUT/'segment-shares.png',dpi=120)
plt.show()


activity = d[['CustomerID','Month']].drop_duplicates().copy()
activity['cohort'] = activity.groupby('CustomerID').Month.transform('min')
activity['age'] = (activity.Month.astype('int64')-activity.cohort.astype('int64')).astype(int)
counts = activity.groupby(['cohort','age']).CustomerID.nunique().unstack()
cohort = counts.div(counts[0],axis=0)
assert np.allclose(cohort[0],1)
observed_rates = cohort.stack().dropna()
assert ((observed_rates>=0)&(observed_rates<=1)).all()
cohort.to_csv(OUTPUT/'cohort-repeat-rates.csv')
print(cohort.round(3).to_string())
fig, ax = plt.subplots(figsize=(11,5))
image=ax.imshow(cohort.to_numpy(),vmin=0,vmax=1,cmap='Blues',aspect='auto')
ax.set_xticks(range(len(cohort.columns)),cohort.columns)
ax.set_yticks(range(len(cohort.index)),cohort.index.astype(str))
ax.set(title='Observed monthly repeat-purchase rates',xlabel='Months since first observed purchase',ylabel='First observed month')
fig.colorbar(image,ax=ax,label='Proportion'); fig.tight_layout()
fig.savefig(OUTPUT/'cohort-repeat.svg'); fig.savefig(OUTPUT/'cohort-repeat.png',dpi=120)
plt.show()


CUTOFF = pd.Timestamp('2011-09-01')
train, future = d[d.InvoiceDate<CUTOFF], d[d.InvoiceDate>=CUTOFF]
historical, historical_threshold = make_rfm(train,CUTOFF)
future_value = future.groupby('CustomerID').PurchaseValue.sum()
holdout = historical[['segment']].copy()
holdout['purchased_next_3_months'] = holdout.index.isin(future_value.index)
holdout['future_purchase_value_gbp'] = future_value.reindex(holdout.index).fillna(0)
evaluation = holdout.groupby('segment').agg(customers=('segment','size'),repeat_customers=('purchased_next_3_months','sum'),repeat_rate=('purchased_next_3_months','mean'),future_purchase_value_gbp=('future_purchase_value_gbp','sum'))
evaluation['value_per_historical_customer_gbp'] = evaluation.future_purchase_value_gbp / evaluation.customers
assert historical.last_purchase.max() < CUTOFF
assert evaluation.customers.sum() == len(historical)
assert evaluation.repeat_customers.sum() == len(set(train.CustomerID)&set(future.CustomerID))
print(evaluation.round(4).to_string())
evaluation.to_csv(OUTPUT/'temporal-holdout.csv')


sensitivity = []
for active_days,lapsed_days,q in [(60,90,.75),(45,75,.75),(90,120,.75),(60,90,.70),(60,90,.80)]:
    alternate,_ = make_rfm(d,END,active_days,lapsed_days,q)
    sensitivity.append({'active_days':active_days,'lapsed_days':lapsed_days,'value_quantile':q,'active_high_value':int((alternate.segment=='Active high value').sum()),'lapsed_high_value':int((alternate.segment=='Lapsed high value').sum()),'changed_labels':int((alternate.segment!=rfm.segment).sum())})
sensitivity = pd.DataFrame(sensitivity)
retained = raw[raw.CustomerID.notna() & ~raw.InvoiceNo.astype(str).str.upper().str.startswith('C') & (raw.Quantity>0) & (raw.UnitPrice>0) & (raw.InvoiceDate>=START) & (raw.InvoiceDate<END)]
value_with_duplicates = float((retained.Quantity*retained.UnitPrice).sum())
duplicate_effect = value_with_duplicates - float(d.PurchaseValue.sum())
print(sensitivity.to_string(index=False))
print('Additional positive value if duplicates retained (GBP):',round(duplicate_effect,2))
sensitivity.to_csv(OUTPUT/'segment-sensitivity.csv',index=False)
metrics = {'source_sha256':source_hash,'raw_rows':len(raw),'analysis_rows':len(d),'customers':len(rfm),'orders':int(d.InvoiceNo.nunique()),'positive_purchase_value_gbp':float(d.PurchaseValue.sum()),'value_threshold_gbp':value_threshold,'value_with_duplicates_gbp':value_with_duplicates,'start':str(START.date()),'end_exclusive':str(END.date()),'all_assertions_passed':True}
(OUTPUT/'run-metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
print('\nVerified metrics:\n',json.dumps(metrics,indent=2))
