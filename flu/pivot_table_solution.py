import pandas as pd

flu_data = pd.read_csv(
    filepath_or_buffer='data/VIW_FID.csv',
    engine='pyarrow',
    on_bad_lines='skip',
    parse_dates=['ISO_WEEKSTARTDATE'],
    usecols=['COUNTRY_AREA_TERRITORY',
             'ISO_WEEKSTARTDATE',
             'ISO_YEAR',
             'AH1N12009',
             'AH3',
             'AH5',
             'AH7',
             'AOTHERTYPES',
             'RSV',
             'INPATIENTS',
             'MORTALITY_ALL',
             'COMMENTS',
             'REPORTED_CASES'
             ]
)

result = flu_data.loc[lambda df_: df_['ISO_WEEKSTARTDATE'].dt.year >= 2020].pivot_table(
    index=pd.Grouper(
        key='ISO_WEEKSTARTDATE',
        freq='1QE'),
    columns='COUNTRY_AREA_TERRITORY',
    values='MORTALITY_ALL',
    aggfunc='sum'
).agg(['max', 'idxmax'], axis='columns').loc[lambda df_: df_['max'] > 0]


print(result.head())