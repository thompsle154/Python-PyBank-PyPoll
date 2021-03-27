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

    #Test to see if this returns the right number of candidates
    #print(Number_candidates)
    
    #Calculate the total number of votes
    #Use len because it returns the number of items in an object
    total_votes = len(Candidate)
    #Get the unique candidates
    Number_candidates = len(Candidate_votes)
    
    #Test the code
    #print(total_votes)

    #Create a dictionary
    Election = {}
    #People= {"Correy": 704200, "Li": 492940, "Khan": 2218231, "O'Tooley": 105630}
    dict_names=(["Correy", "Li", "Khan", "O'Tooley"])
    dict_totals= ([704200, 492940, 2218231, 105630])
    print(People[dict_names])  #Error unhashable type: 'list'



