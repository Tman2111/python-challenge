# bank_analysis_code

# modules
import os
import csv

# data path
# data_csv = os.path.join("Resources", "budget_data.csv")
# file_path = "Resources/budget_data.csv"


# Initialize our variables
total_months = 0
total_net_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999]
net_change_list = []


# read data_csv
with open('election_data.csv', 'r') as csv_file:

# have to separate the months
    csvreader = csv.reader(csv_file, delimiter=',')
# remove header row from calculations 
    csv_header = next(csv_file)
    # prev_net_change = int(row[1])
    # net_net_change = int(row[1]) - prevchange

    #Loop through the csv_file
    for row in csvreader:
        total_months += 1
        total_net_change += int(row[1])
        # net_change = int(row[1]) - prevchange
        #net_change = int
        # count_months=len(list(csvreader(open('budget.data.csv'))))-1
        # net_total_p_and_l = 
print(total_months)
print(total_net_change)


        

