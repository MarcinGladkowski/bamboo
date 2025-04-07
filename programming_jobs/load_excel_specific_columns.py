import pandas as pd
import resource
import time

start = time.time()

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024

print(f"Memory usage: {memory_usage_mb:.2f} MB")

pd.read_excel(
    io='./data/oesm23all/all_data_M_2023.xlsx',
    sheet_name='All May 2023 data',
    usecols=['AREA_TITLE', 'AREA_TYPE', 'OCC_TITLE', 'I_GROUP', 'TOT_EMP', 'JOBS_1000', 'O_GROUP', 'PCT_TOTAL', 'A_MEAN'],
    na_values=['*', '**', '#'],
)

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024

print(f"Memory usage: {memory_usage_mb:.2f} MB")

end = time.time()

"""
Memory usage: 101.76 MB
Memory usage: 733.47 MB
Execution time (s): 70.90411686897278
"""
print(f"Execution time (s): {end - start}")