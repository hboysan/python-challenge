# Pyhton3 PyBankcsv

#Importing in os

import os
import csv

# Set the patch for budgetdata_csv

budgetdata_csv = os.path.join('Resources', 'budget_data.csv')

#Create the storable list

date = []
profit = []
changes = []

# Initialize variables

total_months = 0
total_profits = 0
total_change = 0

# Open the csv file that set on the path budgetdata_csv

with open(budgetdata_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)

   # Loop in the csv file
   for row in csvreader:

     # Count total_months in the csv file
     total_months = total_months + 1

     # Need to collect the date for greatest_increase
     date.append(row[0])

     # Append the profit and calculate the total_profits
     profit.append(row[1])
     total_profits = total_profits + int(row[1])

     #Calculate the monthly_changes
     final_profit = int(row[1])
     monthly_changes = final_profit

     #Store these the monthly_changes in a list
     changes.append(monthly_changes)

     total_change = total_change + monthly_changes


     #Calculate the average change in profits
     avg_change = (total_change/total_months)

     #Find the max and min change in profits
     greatest_increase = max(changes)
     greatest_decrease = min(changes)

     inc_date = date[changes.index(greatest_increase)]
     dec_date = date[changes.index(greatest_decrease)]

   print("```text\n",
       "Financial Analysis\n",
       "----------------------------------------------------------\n",
       "Total Months: " + str(total_months), "\n",
       "Total Profits: " + "$" + str(total_profits), "\n",
       "Average Change: " + "$" + str(int(avg_change)), "\n",
       "Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_increase) + ")", "\n",
       "Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_decrease)+ ")", "\n",
       "```")

with open('budget_data.txt', 'w') as text:
    text.write("```text\n"
        "  Financial Analysis"+ "\n"
        "----------------------------------------------------------\n"
        "    Total Months: " + str(total_months) + "\n"
        "    Total Profits: " + "$" + str(total_profits) +"\n"
        "    Average Change: " + '$' + str(int(avg_change)) + "\n"
        "    Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_increase) + ")\n"
        "    Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_decrease) + ")\n"
        "```")
