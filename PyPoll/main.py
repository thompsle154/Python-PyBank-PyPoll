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

#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    header = next(csvreader)
    
    #Read the rows in a loop to get the data        
    #The data has duplicates. Removing the duplicates first using set
    for row in csvreader:
        Candidate.append(row[2])
    Candidate_votes = set(Candidate)
    Candidate_votes = list(Candidate_votes)
    
    #Get the unique candidates 
    Number_candidates = len(Candidate_votes)
    #Test the code
    print(Number_candidates)



