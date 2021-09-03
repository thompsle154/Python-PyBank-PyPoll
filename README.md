### Python-challenge Project Description
----
### PyBank
PyBank is a python script written to analyze two columns of financial data in a .csv file; dates and monetary values.

The PyBank folder contains an Analysis folder with a .txt file of summary outputs, a Resources folder with the budget_data.csv file used in this analysis and a python file titled main.py.

The main.py file in the PyBank folder:
  * Counts the total number of rows in the first column of the csv file 
  * Calculates the difference between two successive rows in a series
  * Differences are stored as a new list ("changes")
  * The average, and maximum and minimum values are determed from the "changes" list
  * Using list indexes, maximum and minimum values from the "changes" list are associated with the first column of data in the csv file

### PyPoll
PyPoll is a python script written to analyze three columns of election data in a .csv file; voter ids, voterr county, and the candidates last names.

The PyPoll folder contains an Analysis folder with a .txt file of summary outputs, a Resources folder with a election_data.csv file, and a python file titled main.py

The main.py file in the PyPoll folder:
  * Creates a new list of unique candidate names from a series
  * Calculates the total number of votes
  * Calculates the total and percentage of votes assinged to each candidate
  * Creates a dictionary of candidate names and percentage of votes won
  * Uses the dictionary to identify the candidate with the greatest percentage of votes

### Results
![image](https://user-images.githubusercontent.com/78496051/132043319-820d1626-370a-4e2d-934f-b7c124ffffda.png)
![image](https://user-images.githubusercontent.com/78496051/132045026-cf8974ec-4dd3-4be8-92a7-55997359fc84.png)

### Results Analysis
The Python Challenge consists of creating two scripts written in Python; PyBank and PyPoll. 

PyBank analyzed financial records of a company. The results are a Financial Analysis using Dates and Profit/Losses source data for 86 months. In this time, the company had a profit of $38,3825,578. The average change per month was $-2,315. We can conclude the greatest monthly increase in profits occurred in February 2012 and the greatest decrease was in Sept 2013.

PyPoll analyzed election data from a small town to modernize its vote counting process. The Election data contained the voter ID, the county the voter was from, and the candidate that was voted for to determine the winner. The election results show total votes of 3,521,001. Each of the four candidate's number of votes and percentage are displayed on the report and show who the winner of the election is. 
