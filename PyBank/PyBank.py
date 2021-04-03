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
pm_pl = 0
pl_change = 0
months = []
monthly_change_list =[]
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
        cm_pl = int(row[1])
        
        if (total_months == 1):
            pm_pl = cm_pl
        continue

        else:

            #calculating monthly profit/loss
            monthly_change = cm_pl - pm_pl

            # adding to the months lis
            months.append(row[0])

            # adding changes to change list
            monthly_change_list.append(monthly_change)

            # reset prev month to current month
            pm_pl = cm_pl

sum_pl = sum(monthly_change)
avg_pl = round(sum_pl/total_months - 1), 2)

highest_change = max(monthly_change_list)
lowest_change = min(monthly_change_list)

highest_c_i = monthly_change_list.index(highest_change)
lowest_c_i = monthly_change_list.index(lowest_change)

most_month = months[highest_c_i]
least_month = months[lowest_c_i]



# printing to terminal
print("Financial Analysis")
print("-----------------------------------")
print("Total months: " + str(total_months))
print("Total: $" +str(total_net_change))
print(f"Average Change:  ${avg_pl}") 
print(f"Greatest Increase in Profits: {most_month} (${highest_change}")
print(f"Greatest Decrease in PRofits: {least_month} (${lowest_change}")

# Results text file
PyBank_results = os.path.join("Output", "budget_data.txt")

with open(PyBank_results, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write("Total months:  {total_months}\n")
    outfile.write()
    outfile.write("Average Change:  $")

        

