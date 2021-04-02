# bank_analysis_code

# modules
import os
import csv

# data path
data_csv = os.path.join("Resources", "budget_data.csv")

# read data_csv
with open(data_csv, "r") as csv_file:

# have to separate the months
    csvreader = csv.reader(csv_file, delimiter=',')
# remove header row from calculations 
    csv_header = next(csv_file)


# What are our variables?
    months = 0
    net_change_p_and_l = 0


    for row in csvreader:

        count_months=len(list(csvreader(open('budget.data.csv'))))-1

        

