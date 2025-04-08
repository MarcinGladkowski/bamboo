### Data
https://taxfoundation.org/wp-content/uploads/2025/02/2025-State-Individual-Income-Tax-Rates-and-Brackets-2025.xlsx

### Task:
```
Read the Excel spreadsheet into a Pandas data frame. The index should contain state names (well, abbreviations)
from the "State" column, without the footnotes. Remove the footnote lines at the end. 
You can remove the columns containing ">" symbols. You can treat both "none" and "n.a." as 0 values. 
Cells that contain text (i.e., not numbers) can be turned into 0.
Which state has the highest rate for single filers? Which states have no income tax at all?
```