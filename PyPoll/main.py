#Delcare dependancies
import os
import csv

#Set path for data
poll_data_csv = os.path.join('.', 'Desktop','PyPoll', 'election_data.csv')

#Create Lists

total_votes = 0
list_of_candidates = []
percentage_of_votes =[]
votes_for_candidates = []
winner_of_election = []

#Read Data

with open(poll_data_csv, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    for row in csvreader:
       
        total_votes += 1 

        if row[2] not in list_of_candidates:
            
            list_of_candidates.append(row[2])
            
            index = list_of_candidates.index(row[2])
            
            votes_for_candidates.append(1)
            
        else:
            
            index = list_of_candidates.index(row[2])
            votes_for_candidates[index] += 1

# Find the winning candidate
winner = max(votes_for_candidates)
index = votes_for_candidates.index(winner)
winning_candidate = list_of_candidates[index]

for votes in votes_for_candidates:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentage_of_votes.append(percentage)
