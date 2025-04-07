### Data source
https://www.newyorkfed.org/medialibrary/Interactives/sce/sce/downloads/data/FRBNY-SCE-Credit-Access-Data.xlsx?sc_lang=en
https://www.newyorkfed.org/medialibrary/Interactives/sce/sce/downloads/data/2015-SCE-Credit-Access-survey-questionaire.pdf?sc_lang=en

### Task
```
- Read data from both the the `overall` and `demographics` sheets into data frames. In both cases, use the date as the index, parsing it into a `datetime` value.
A common question to ask people about their financial security is whether they could come up with a certain amount of money, given the need. 

- Questions N24 and N25 in the survey ask participants to indicate the percentage chance that 
they would have an unexpected $2,000 expense in the coming 12 months, and also the percentage chance that they could
 come up with $2,000 if they needed to. Using the `overall` data frame, produce a line plot comparing these values 
 over the course of the data set. What does this indicate? If we use subplots, does the clarity of the plot change? 
 Does setting the y axis to be 0-100, rather than set automatically, change our interpretation?
```