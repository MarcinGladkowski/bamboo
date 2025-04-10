import pandas as pd

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

# Group by name and monthly datetime
monthly_grouped = flights.groupby(
    [pd.Grouper(level='AirportCode'), pd.Grouper(level='FlightDateTime', freq='M')]
).sum()

# Reset index for plotting
monthly_grouped.reset_index(inplace=True)

# Plot the data
for name, group in monthly_grouped.groupby('name'):
    plt.plot(group['FlightDateTime'], group['NonUsaPassengerCount'], label=name)

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Monthly Data by Name')
plt.legend()
plt.show()