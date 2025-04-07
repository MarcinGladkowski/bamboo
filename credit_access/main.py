import pandas as pd
import matplotlib.pyplot as plt


filename = 'data/FRBNY-SCE-Credit-Access-Data.xlsx'

overall_df, demographics_df = (pd.read_excel(
    io=filename,
    sheet_name=['overall', 'demographics'],
    header=1,
    parse_dates=['date'],
    date_format='%Y%m',
    index_col='date')
.values())

overall_df[['ChanceNeed', 'ChanceComeUp']].plot.line(ylim=(0, 100))

plt.show()

