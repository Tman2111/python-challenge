# poll_analysis_code

import os
import csv

#variable
total_votes = 0
candidates_votes ={}
candidate_list=[]


# Read the csv file for the election data
with open('election_data.csv') as csv_file:

# have to separate the months
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #Get the total vote count
        total_votes = total_votes + 1
        #this line of code below gets the candidate name in the row
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] = candidates_votes[candidate_name] + 1
print(candidates_votes, total_votes)