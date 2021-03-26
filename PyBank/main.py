#Python Challenge Homework
#Created By: Leanne Thompson
#Created Date: March 2021

import os
import csv

#Read the csv file
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')

#Initializing lists to store data
months = []
profit_amt = [
#profit_change = []

with open(budgetdata_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Count total number of months
    lines = len(list(csvreader))
    print("Total Months : " + str(lines))
    
    #Read the rows after the header and format amt as integer        
    #Get total of amounts in profit/loss column for all months
    
    for row in csvreader:
        months.append([row[0], int(row[1])])
        total_amt += (int(row[1]))
        #date.append(row[0]+1)
    #print ("Total : " + (total_amt))    
    print(total_amt)
    #print(alldata)

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
     
       #Get total number of months
#print("Total Months: %d"%(csvreader.line_num))




   

