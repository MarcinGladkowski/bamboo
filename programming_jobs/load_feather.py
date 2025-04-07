import pyarrow.feather as feather
import resource
import time

start = time.time()

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024
print(f"Memory usage: {memory_usage_mb:.2f} MB")

df = feather.read_feather('data/oesm23all/all_data_M_2023.feather')

memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# Convert to megabytes
memory_usage_mb = memory_usage_kb / 1024
print(f"Memory usage: {memory_usage_mb:.2f} MB")

end = time.time()

"""
Super fast!

Memory usage: 54.25 MB
Memory usage: 187.52 MB
Execution time (s): 0.25522351264953613
"""
print(f"Execution time (s): {end - start}")