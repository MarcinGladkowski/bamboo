import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



df = pd.read_excel(
    io='./data/CMO-Historical-Data-Monthly.xlsx',
    sheet_name='Monthly Prices',
    header=4, # columns names from row 4
)

df = df.drop([0]) # remove column contains measures

df = df.rename(columns={'Unnamed: 0': 'Date'})

df['Date'] = pd.to_datetime(df['Date'], format='%YM%m').dt.strftime('%Y-%m')
df = df.set_index('Date')

df = df.apply(pd.to_numeric, errors='coerce') # replace ... with Nan
df = df.fillna(0)

to_plot = df['Cocoa']

ax = to_plot.plot(kind='line')
plt.tight_layout()

plt.show()



