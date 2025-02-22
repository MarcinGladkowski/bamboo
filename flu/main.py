import pandas as pd

data_dictionary = pd.read_csv('data/VIW_FLU_METADATA.csv', engine='pyarrow')

"""File contains malformed data, so we need to skip bad lines"""
flu_data = pd.read_csv(
    filepath_or_buffer='data/VIW_FID.csv',
    engine='pyarrow',
    on_bad_lines='skip',
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

flu_data = flu_data[flu_data['REPORTED_CASES'].notna()]
flu_data = flu_data[flu_data['ISO_YEAR'] > 2018]

flu_data['REPORTED_CASES'] = flu_data['REPORTED_CASES'].astype(int)

"""ISO_WEEKSTARTDATE is a date column, so we need to convert it to datetime"""
flu_data['ISO_WEEKSTARTDATE'] = pd.to_datetime(flu_data['ISO_WEEKSTARTDATE'])


flu_data['quarter'] = flu_data['ISO_WEEKSTARTDATE'].dt.quarter

"""
We need to recognize quarter based on ISO_WEEKSTARTDATE column
"""
cases_for_country = flu_data.groupby(['ISO_YEAR', 'quarter', 'COUNTRY_AREA_TERRITORY'])['REPORTED_CASES'].sum().reset_index()

cases_for_country.sort_values('REPORTED_CASES', ascending=False, inplace=True)

cases_for_country.to_csv('data/reported_cases_by_country_and_quarter.csv', index=False)
