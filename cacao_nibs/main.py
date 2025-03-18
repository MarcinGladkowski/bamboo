import numpy as np
import pandas as pd


df = pd.read_excel(
    io='./data/CMO-Historical-Data-Monthly.xlsx',
    sheet_name='Monthly Prices',
    header=4, # columns names from row 4
)

df = df.drop([0]) # remove column contains measures

df = df.rename(columns={'Unnamed: 0': 'Date'})
df = df.set_index('Date')
df = df.infer_objects(copy=False)
df = df.apply(lambda x: x.replace('...', 0))
df = df.apply(pd.to_numeric, errors='coerce') # replace ... with Nan
df = df.fillna(0)


