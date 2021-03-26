#Python Challenge Homework
#Created By: Leanne Thompson
#Created Date: March 2021

import os
import csv

#Read the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Initializing lists to store data
months = []
profit_amt = []
profit_change = []

#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    header = next(csvreader)
    
    #Read the rows after the header and format amt as integer        
    #Seperate out the columns
    for row in csvreader:
        months.append(row[0])
        profit_amt.append(int(row[1]))

    #Loop through the amounts to get the monthly change
    for r in range(len(profit_amt)-1):
   
        #Get the difference between the two months
        profit_change.append(profit_amt[r+1] - profit_amt[r])

#Look at min and max from amount that changec
max_inc_value = max(profit_change)
max_dec_value = min(profit_change)

#Set min and max to month list and set index
#Use +1 to put change on the next month
month_max_increase = profit_change.index(max(profit_change)) + 1
month_max_decrease = profit_change.index(min(profit_change)) + 1


         
#Set print statements outside of loop - no indent     
print("Financial Analysis")
print("---------------------------") 
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_amt)}")
print(f"Average Change: ${round((profit_change)/len(profit_change), 2)}")
print(f"Greatest Increase in Profits: {months[month_max_increase]} (${(str(max_inc_value))})")
print(f"Greatest Decrease in Profits: {months[month_max_decrease]} (${(str(max_dec_value))})")


        




   

