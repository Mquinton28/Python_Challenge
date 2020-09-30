# Modules
import os
import csv

# set path for file
election_data = os.path.join("..", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_election_data.csv")

# create lists
total_votes = []
candidates = []
results = []
percentage_of_votes = []

# open csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_votes.append(row[0])
        candidates.append(str(row[2])

# max = 0
# min = 0
# max_index = 0
# min_index = 0

# percent = round(int(total_votes) / len(total_votes), 2)
# percentage_of_votes.append(percent)
# Print Statements
#print("Election Results")
#print("----------------------")
#print(f"Total Votes: {len(total_votes)}")
#print("------------------------")

# output file