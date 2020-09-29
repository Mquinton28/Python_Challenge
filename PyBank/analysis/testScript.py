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
#with open(budget_data, encoding='utf-8') as csvfile: 
with open(budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Skip Headers
        header = next(csvreader)
        for row in csvreader:
                total_months.append(row[0])
                total_profit_loss.append(int(row[1]))

# Define Variables
max = 0
min = 0
max_index = 0
min_index = 0

for cur_index, cur_profit_loss in enumerate(total_profit_loss):
        if cur_profit_loss > max:
                max = cur_profit_loss
                max_index = cur_index
        if cur_profit_loss < min:
                min = cur_profit_loss
                min_index = cur_index


average_profit_loss = sum(total_profit_loss) / len(total_profit_loss)
#greatest_profit_increase = max(total_profit_loss)
#greatest_profit_decrease = min(total_profit_loss)

#Print Statements
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit_loss)}")
print(f"Average Change: ${round(average_profit_loss, 2)}")
print(f"Greatest Profit Increase: {total_months[max_index],max}")
print(f"Greatest Profit Decrease: {total_months[min_index], min}")


#variable for output file
pybank_analysis = os.path.join("Pybank_final.txt")
#export text file
with open(pybank_analysis, "w") as txtfile:
        txtfile.write("FinalScript")
        txtfile.write("Financial Analysis")

