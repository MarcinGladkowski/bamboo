import pandas as pd


df = pd.read_excel(
    io='./data/CMO-Historical-Data-Monthly.xlsx',
    sheet_name='Monthly Prices',
    header=4, # columns names from row 4
)

print(df.columns)