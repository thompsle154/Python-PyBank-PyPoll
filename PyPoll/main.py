#Python Challenge Homework - PyPoll
#Created By: Leanne Thompson
#Created Date: March 2021

import os
import csv

#Read the csv file
csvpath = os.path.join('Resources', 'election_data.csv')
#txtpath = os.path.join('Analysis', 'Financial_Analysis.txt')

#Initializing lists to store data
Candidate = []
Candidate_votes = []

Total_votes = 0

#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    header = next(csvreader)
    
    #Read the rows in a loop to get the data        
    #The data has duplicates. Remove the duplicates first using set
    for row in csvreader:
        Candidate.append(row[2])
    Candidate_votes = set(Candidate)
    Candidate_votes = list(Candidate_votes)

           
    #Calculate the total number of votes
    #Use len because it returns the number of items in an object
    Total_votes = len(Candidate)
    #Get the unique candidates
    Number_candidates = len(Candidate_votes)
        
    #Test the code
    #print(total_votes)

    #Create a dictionary
    #Used Name and Id to store value pairs. Added tuple
    Election = {}
    People= {'Correy': tuple([704200]), 'Li': tuple([492940]), 'Khan': tuple([2218231]), 'OTooley': tuple([105630])}
    dict_names=(['Correy', 'Li', 'Khan', 'OTooley'])
    dict_totals=([704200, 492940, 2218231, 105630])
    

    print("Election Results")
    print("----------------------")
    print("Total Votes:", (Total_votes))
    print("----------------------")

    #Add for loop to use the dictionary
    for i in range(Number_candidates):
        Election [Candidate_votes[i]]= Candidate.count(Candidate_votes [i])

        #Test to see candidate names
        print(Candidate_votes[i])
        print('%.3f'%round(float(Election[Candidate_votes[i]])/Total_votes*100) + '%') #print 3 decimal places
        print(Election[Candidate_votes[i]])  #to print number of votes each candidate won
    print("-------------------")
    print("Winner: " + str(max(Candidate_votes)))







