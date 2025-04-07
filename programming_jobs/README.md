Data source:
```
https://www.bls.gov/oes/special-requests/oesm23all.zip
```

Task
```
Here are this week's five questions and tasks:

Read in the data from Excel. We only need some of the columns (AREA_TITLE, AREA_TYPE, OCC_TITLE, I_GROUP, TOT_EMP, JOBS_1000, O_GROUP, PCT_TOTAL, and A_MEAN. 
Treat "*", "**", and "#" as a NaN value. Does it take less time to read the data if we limit the columns? How much does it change the size of the data (in memory) by limiting the columns?

Store the data in Feather and Parquet format, and read from these files back into Pandas. Does it take less time to read from these formats? Which is faster?
```