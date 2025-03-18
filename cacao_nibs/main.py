import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel(
    io='./data/CMO-Historical-Data-Monthly.xlsx',
    sheet_name='Monthly Prices',
    header=4, # columns names from row 4
    na_values=['…', '...'],
    parse_dates=[0],
    date_format='%YM%m'
)

df = df.drop([0]) # remove column contains measures
df = df.rename(columns={'Unnamed: 0': 'Date'})
df = df.set_index('Date')
to_plot = df['Cocoa']

# ax = to_plot.plot(kind='line')
# plt.tight_layout()
# plt.show()

(
    df
    .iloc[-60:]
    ['Cocoa']
    .pipe(lambda df_: sns.lineplot(df_, marker='o'))
    .set(xlabel='Date',
         ylabel='Price',
         title='Cocoa Prices')
)

plt.show()



