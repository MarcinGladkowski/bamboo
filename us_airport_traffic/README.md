# Data source
https://awt.cbp.gov/ -> generate report -> download csv (e.g terminal)

# Tasks
1. Download the data for the six airports, and combine them into a single data frame. 
Turn the "Flight Date" and "HourRange" columns into a single datetime column (using the first time in "HourRange"). 
Set the index to combine the "IATA" column (i.e., the airport name) and the "datetime" column.

2. Create a line graph showing, on a monthly basis, how many non-US passengers entered the US at each airport in this data set.
Do we see any recent downturn?