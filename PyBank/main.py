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
#profit_change = []

#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Read the rows after the header and format amt as integer        
    #Get total of amounts in profit/loss column for all months
    
    for row in csvreader:
        months.append(row[0])
        profit_amt.append(int(row[1]))
        #total_amt += (int(row[1]))

        
    #Loop through the amounts to get the monthly change
      #  for r in range(len(profit_amt)-1:
    
    #print ("Total : " + (profit_amt))    
    #print(profit_amt)
    

    #Get Average Change
    #Find change between all months than get the average
    #get max and min, then subtract, divided by number of lines (86)
    #input()
    #    avg_change = 0
    #for row in csv_reader:
    #    First.append(row)
    #    avg_change = (max(row[1]) - min(row[1]) / (lines)))
    #print("Average Change: ", str(avg_change))

       
      
    #Create title header
print("Financial Analysis")
print("---------------------------") 
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_amt)}")
        




   

