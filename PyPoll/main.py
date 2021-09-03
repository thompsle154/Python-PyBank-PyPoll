# Python Challenge Homework - PyPoll
# Created By: Leanne Thompson
# Created Date: March 2021

import os
import csv

# Read the csv file
csvpath = os.path.join('Resources', 'election_data.csv')
txtpath = os.path.join('Analysis', 'Financial_Analysis.txt')

# Initializing lists to store data
Candidate = []
Candidate_votes = []

# Total Vote Counter
Total_votes = 0

# Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    header = next(csvreader)
    
    # Read the rows in a loop to get the data
    # The data has duplicates. Remove the duplicates first using set
    for row in csvreader:
        Candidate.append(row[2])
    Candidate_votes = set(Candidate)
    Candidate_votes = list(Candidate_votes)
           
    # Calculate the total number of votes
    # Use len because it returns the number of items in an object
    Total_votes = len(Candidate)
    # Get the unique candidates
    Number_candidates = len(Candidate_votes)
        
    # Create a dictionary
    # Used Name and total of votes to store value pairs. Added tuple
    Election = {}
    People = {'Correy': tuple([704200]), 'Li': tuple([492940]), 'Khan': tuple([2218231]), 'OTooley': tuple([105630])}
    dict_names = (['Correy', 'Li', 'Khan', 'OTooley'])
    dict_totals = ([704200, 492940, 2218231, 105630])
    
    print("Election Results")
    print("----------------------")
    print("Total Votes:", Total_votes)
    print("----------------------")

    # Add for loop to use the dictionary
    for i in range(Number_candidates):
        Election[Candidate_votes[i]] = Candidate.count(Candidate_votes[i])

        # Print the list of candidate that received votes
        print((Candidate_votes[i] + ':') + ' ' + ('%.3f' % round(float(Election[Candidate_votes[i]])/Total_votes*100) + '%') + ' ' + '(' + str(Election[Candidate_votes[i]]) + ')')
    
    # Print the winner based on popular vote
    print("-------------------")
    print("Winner: " + str(max(Candidate_votes)))

    # Print to a text file
    f = open(txtpath, "w+")
    print(f"Election Results", file=f)
    print(f"----------------------", file=f)
    print(f"Total Votes: {Total_votes}", file=f)
    print(f"----------------------", file=f)
    for i in range(Number_candidates):
        Election[Candidate_votes[i]] = Candidate.count(Candidate_votes[i])
        print(f"{(Candidate_votes[i]) + ':' + ' ' + '%.3f'%round(float(Election[Candidate_votes[i]])/Total_votes*100) + '%' + ' ' + '(' + str(Election[Candidate_votes[i]]) + ')'}", file=f)
    print(f"-------------------", file=f)
    print(f"Winner: {(str(max(Candidate_votes)))})", file=f)
    f.close
