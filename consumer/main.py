from pprint import pprint

import pandas as pd

consumers_index_data_frame = pd.read_csv(
    filepath_or_buffer='data/prod.csv',
    on_bad_lines='skip',
    usecols=lambda x: x.startswith(('ics', 'ice', 'icc', 'px1')) or x in ['Month', 'yyyy']
)

"""Date formatting: https://docs.python.org/3/library/datetime.html"""
consumers_index_data_frame['Date'] = pd.to_datetime(
    consumers_index_data_frame['yyyy'].astype(str) + consumers_index_data_frame['Month'].astype(str),
    format='%Y%m').dt.strftime('%Y-%m')

consumers_index_data_frame = consumers_index_data_frame.set_index('Date')
consumers_index_data_frame = consumers_index_data_frame.sort_index()

consumers_index_data_frame = consumers_index_data_frame[['ics_all', 'icc_all', 'ice_all']]

import numpy as np
"""Update data to the newest not published in csv file"""
consumers_index_data_frame.loc[pd.to_datetime('2025-02-01')] = np.nan
consumers_index_data_frame.loc[pd.to_datetime('2025-02-01'), ['ics_all', 'icc_all', 'ice_all']] = [64.7, 65.7, 64.0]

pprint(consumers_index_data_frame[['ics_all', 'icc_all', 'ice_all']]
       .pct_change()
       .tail(1))

print('Consumer indexes year to year:')


year_to_year = (
    consumers_index_data_frame
    [['ics_all', 'icc_all', 'ice_all']]
    .pct_change(periods=12) # year to year in percentage
    .iloc[-1]
)

pprint(
    year_to_year[['ics_all', 'icc_all', 'ice_all']]
)
