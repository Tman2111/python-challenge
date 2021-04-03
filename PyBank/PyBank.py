# bank_analysis_code

# modules
import os
import csv

# data path
data_csv = os.path.join("Resources", "budget_data.csv")


# Initialize our variables
total_months = 0
total_net_change = 0
cm_pl = 0
pm_pl = 867884
pl_change = 0
total_change_list =[]
# read data_csv
with open('budget_data.csv', 'r') as csv_file:

# have to separate the months
    csvreader = csv.reader(csv_file, delimiter=',')
# remove header row from calculations 
    csv_header = next(csv_file)
    #Loop through the csv_file
    for row in csvreader:
        total_months += 1
        total_net_change += int(row[1])
        cm_pl = cm_pl
        total_change = cm_pl - pm_pl
        total_change_list.append(total_change)




# print(total_months)
print(total_change_list)


print("Financial Analysis")
print("-----------------------------------")
print("Total months: " + str(total_months))
print("Total: $" +str(total_net_change)) 

        

