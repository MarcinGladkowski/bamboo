from pprint import pprint
import os

import pandas as pd
import time

start_time = time.time()

def load_data(filename: str = 'FACTDATA_MAR2024.TXT') -> pd.DataFrame:
    """
    Data can be load directly from ZIP file
    :param filename:
    :return:
    """
    return pd.read_csv(
        os.path.join('data', filename),
        sep=',',
        encoding='utf-8',
        dtype='str'
    )

def extend_with_agency(data: pd.DataFrame, filename: str, merge_index: str) -> pd.DataFrame:
    sub_data = load_dt(filename)
    return data.merge(sub_data, on=merge_index)

def load_dt(filename):
    sub_data = pd.read_csv(
        f'./data/DT{filename.lower()}.txt',
        sep=',',
        encoding='utf-8',
        dtype='str',
        engine='pyarrow',
    )
    return sub_data


main = load_data()

to_extend_by = ['LOC', 'AGELVL', 'EDLVL', 'LOSLVL', 'OCC', 'SALLVL', 'STEMOCC']
for key in to_extend_by:
    main = extend_with_agency(main, key, key)

main = extend_with_agency(main, 'AGY', 'AGYSUB')
main['EMPLOYMENT'] = main['EMPLOYMENT'].astype(int)

"""
Instead of merging:
(
    df
    ['AGYT']
    .value_counts()
    .head(20)
)
"""
result = main.groupby('AGY')['EMPLOYMENT'].sum().reset_index()
result.sort_values('EMPLOYMENT', ascending=False, inplace=True)
result.reset_index(drop=True, inplace=True)

result = result.merge(load_dt('AGY'), on='AGY', suffixes=('', '_sum'))
result = result.drop_duplicates(subset=['AGY'])

result['EMPLOYMENT'] = result['EMPLOYMENT'].apply(lambda x: f"{x:,}")

elapsed_time = time.time() - start_time
pprint(f"Execution time: {elapsed_time:.2f} seconds")

pprint(result[['AGY','AGYT','EMPLOYMENT']].head(20))
