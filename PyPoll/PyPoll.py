# poll_analysis_code

import os
import csv

#data path
data_csv = os.path.join("Resources", "election_data.csv")


#variables
total_votes = 0
candidates = []
votes_for =[]
percent_of_vote = []



# Read the csv file for the election data
with open('election_data.csv') as csv_file:

# have to separate the months
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #Get the total vote count
        total_votes = total_votes + 1
        
        # tally the votes for each cadidate
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(row[2])
            votes_for.append(1)

        else:
            candidate_index = candidates.index(row[2])
            votes_for[candidate_index] += 1

# print(total_votes)
