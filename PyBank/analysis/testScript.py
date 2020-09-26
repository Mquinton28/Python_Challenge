# Modules
import os
import csv

# set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Variables
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# Open the CSV
def budget_data(filepath):
    with open(budget_data, "r") as csvfile:
        csvreader = csv.reader(csvpath, delimiter=",")

    csvheader = next(budget_data)

    row = 0
    average = sum([row(1)]) / len([row(1)])


    for months in csvreader:
        if row[0] == months('....'):
            total = total + 1
            print (total)

        print(sum[row(1)])
        print(average)