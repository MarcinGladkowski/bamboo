import pandas as pd
from matplotlib import pyplot as plt

atlanta = pd.read_csv(
    filepath_or_buffer="data/atlanta_terminal_e_A171_2023-02-04-2025-08-04.csv",
)

san_francisco = pd.read_csv(
    filepath_or_buffer="data/san_francisco_terminal_A286_2023-02-04-2025-08-04.csv",
)

def format_flight_date_time(data_frame: pd.DataFrame) -> pd.DataFrame:
    data_frame['HourRange'] = data_frame['HourRange'].str.extract(r'(\d+)')
    data_frame['FlightDateTime'] = pd.to_datetime(data_frame['FlightDate'].astype(str) + data_frame['HourRange'].astype(str), format="%Y-%m-%d%H%M").dt.strftime('%Y-%m-%d %H:%M')
    return data_frame


atlanta = format_flight_date_time(atlanta)
san_francisco = format_flight_date_time(san_francisco)

flights = pd.concat([atlanta, san_francisco])
flights.set_index(['AirportCode', 'FlightDateTime'], inplace=True)

# Ensure FlightDateTime is a DatetimeIndex
flights.index = flights.index.set_levels(
    [flights.index.levels[0], pd.to_datetime(flights.index.levels[1])]
)

# Group by name and monthly datetime
monthly_grouped = flights.groupby(
    [pd.Grouper(level='AirportCode'), pd.Grouper(level='FlightDateTime', freq='M')]
).sum()

# Reset index to prepare data for plotting
monthly_grouped = monthly_grouped.reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
for airport_code in monthly_grouped['AirportCode'].unique():
    airport_data = monthly_grouped[monthly_grouped['AirportCode'] == airport_code]
    plt.plot(
        airport_data['FlightDateTime'],
        airport_data['NonUsaPassengerCount'],  # Replace with the column you want to plot
        label=airport_code
    )

plt.title('Monthly Traffic by Airport')
plt.xlabel('Date')
plt.ylabel('Traffic')
plt.legend(title='Airport Code')
plt.grid(True)
plt.tight_layout()
plt.show()
