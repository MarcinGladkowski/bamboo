import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    filepath_or_buffer='data/data-table.csv',
    index_col='week_start',
    parse_dates=['week_start'], # better displays labels for x axis
)

df.plot.line()
plt.show()

