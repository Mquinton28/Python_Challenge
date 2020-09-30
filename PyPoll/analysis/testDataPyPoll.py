# Modules
import os
import csv

# set path for file
election_data = os.path.join("..","PyPoll", "Resources", "election_data.csv")

# create lists
total_votes = []
candidate = []
percentage_of_votes = []

# open csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_votes.append(row[0]) = total_votes + 1
        candidate.append(str(row[2])

#if candidate == "O'Tooley":

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