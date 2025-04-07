import pandas as pd

df = pd.read_excel(
    io='./data/oesm23all/all_data_M_2023.xlsx',
    sheet_name='All May 2023 data',
    usecols=['AREA_TITLE', 'AREA_TYPE', 'OCC_TITLE', 'I_GROUP', 'TOT_EMP', 'JOBS_1000', 'O_GROUP', 'PCT_TOTAL',
             'A_MEAN'],
    na_values=['*', '**', '#'],
)

df.to_parquet('./data/oesm23all/all_data_M_2023.parquet')
