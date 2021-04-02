# bank_analysis_code

# modules
import os
import csv

# data path
data_csv = os.path.join("Resources", "budget_data.csv")

# read data_csv
with open(data_csv, "r") as csv_file:
    Clmn1 =[]

# have to separate the months
    csvreader = csv.reader(csv_file, delimiter=',')
# remove header row from calculations 
    csv_header = next(csv_file)


# What are our variables?
    changes_p_and_l = 0
    total_months = 0

    for row in csvreader:

        Clmn1.append(row[1])
        changes_p_and_l = changes_p_and_l + (int(row[1])
        total_months = len(list(csvreader(open('budget.data.csv'))))-1

