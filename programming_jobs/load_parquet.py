import pandas as pd
import resource
import time

start = time.time()

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024

print(f"Memory usage: {memory_usage_mb:.2f} MB")

pd.read_parquet(
    path='./data/oesm23all/all_data_M_2023.parquet',
    columns=['AREA_TITLE', 'AREA_TYPE', 'OCC_TITLE', 'I_GROUP', 'TOT_EMP', 'JOBS_1000', 'O_GROUP', 'PCT_TOTAL', 'A_MEAN'],
)

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024
print(f"Memory usage: {memory_usage_mb:.2f} MB")

end = time.time()

"""
Super fast!

Memory usage: 101.59 MB
Memory usage: 228.23 MB
Execution time (s): 0.07042193412780762
"""
print(f"Execution time (s): {end - start}")