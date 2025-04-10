
import pandas as pd

filename = 'data/2025-State-Individual-Income-Tax-Rates-and-Brackets-2025.xlsx'

df = (pd
      .read_excel(filename,
                  header=[0, 1],
                  nrows=217)
      .replace(to_replace='\\(.*\\)', value='', regex=True)
      .replace(to_replace='none', value='0')
      .replace(to_replace='n.a.', value='0')
      .replace(to_replace='^\\s*$', value=pd.NA, regex=True)
      .replace(to_replace='\\s+$', value='', regex=True)
      .replace(to_replace='^\\s+', value='', regex=True)
      .assign(state=lambda df_: df_[('Unnamed: 0_level_0', 'State')].ffill())
      .set_index('state')
      .replace(to_replace='^.*[^\\d.].*$', value='', regex=True)
      .drop(columns=[('Unnamed: 0_level_0', 'State'),
                     ('Single Filer', 'Rates.1'),
                     ('Married Filing Jointly', 'Rates.1')])
      .replace(to_replace='\\D+', value='', regex=True)
      .replace(to_replace='', value='0')
      .astype(float)
      .ffill()
      .drop_duplicates()
      )

highest_rates = (
    df
    [('Single Filer', 'Rates')]
    .agg(['max', 'idxmax'])
)

print(highest_rates)

zero_rates = (
    df
    [('Single Filer', 'Rates')]
    .loc[lambda s_: s_ == 0]
)

print(zero_rates)