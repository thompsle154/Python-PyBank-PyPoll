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

#Look at min and max from amount change
max_value = max(profit_change)
min_value = min(profit_change)

   #Get Average Change
    #Find change between all months than get the average
    #get max and min, then subtract, divided by number of lines (86)
    #input()
       #    First.append(row)
    #    avg_change = (max(row[1]) - min(row[1]) / (lines)))
    #print("Average Change: ", str(avg_change))

       
#Put outside of loop - no indent     
print("Financial Analysis")
print("---------------------------") 
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_amt)}")
print(f"Average Change: ${round((profit_change),2)}")

        




   

