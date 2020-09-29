# Modules
import os
import csv

# set path for file
budget_data = os.path.join("..", "Resources", "budget_data.csv")

# Create Lists
total_months = []
total_profit_loss = []
average_profit_loss = []

# Open the CSV
with open(budget_data, encoding='utf-8') as csvfile: 
        csvreader = csv.reader(csvfile, delimiter=",")

# Skip Headers
        header = next(csvreader)

for row in csvreader:
    total_months.append(row[0])
    total_profit_loss.append(int(row[1]))
    average_profit_loss = sum(int[row(1)]) / len([row(1)])

#Print Statements
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(total_months)}")

#variable for output file
pybank_analysis = os.path.join("Pybank_final.txt")
#export text file
#with open(pybank_analysis, "w") as txtfile
#writer = txt.writer(txtfile)