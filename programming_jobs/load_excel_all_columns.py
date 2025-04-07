import pandas as pd
import resource
import time

start = time.time()

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024

print(f"Memory usage: {memory_usage_mb:.2f} MB")

pd.read_excel('./data/oesm23all/all_data_M_2023.xlsx', sheet_name='All May 2023 data')

end = time.time()

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024

print(f"Memory usage: {memory_usage_mb:.2f} MB")

"""
Memory usage: 101.64 MB
Memory usage: 974.30 MB
Execution time (s): 63.35534477233887
"""
print(f"Execution time (s): {end - start}")
