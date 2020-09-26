# Modules
import os
import csv

# set path for file
csvpath = os.path.join("..", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Variables

# Open the CSV
def budget_data(filepath):
    with open(filepath, "r") as profit:
        csvreader = csv.reader(csvpath, delimiter=",")

    header = next(csvreader)

    for months in range(profit):
        
