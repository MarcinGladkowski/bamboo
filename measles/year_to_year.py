import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame (Replace this with your actual dataset)
df = pd.read_csv(
    filepath_or_buffer='data/data-table.csv',
)


df['week_start'] = pd.to_datetime(df['week_start'])

# Extract year-wise data
year1 = 2023
year2 = 2024

df1 = df[df['week_start'].dt.year == year1]
df2 = df[df['week_start'].dt.year == year2]

# Group by month and calculate mean (or sum)
df1_grouped = df1.groupby(df1['week_start'].dt.month)['cases'].sum()
df2_grouped = df2.groupby(df2['week_start'].dt.month)['cases'].sum()

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df1_grouped.index, df1_grouped.values, marker='o', label=f'{year1}')
plt.plot(df2_grouped.index, df2_grouped.values, marker='s', label=f'{year2}')

# Formatting the plot
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.title('Month-to-Month Comparison')
plt.legend()
plt.grid()
plt.show()
