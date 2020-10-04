# Modules
import os
import csv

# set path for file
election_data = os.path.join("..","Resources", "election_data.csv")

# create lists
total_votes = []
votes = 0
candidates = []
percentage_votes = []

# open csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        votes = votes + 1
        candidate = row[2]
    
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            votes[candidate_index] = total_votes[candidate_index] + 1
        
        else:
            candidates.append(candidate)
            total_votes.append(1)

max = total_votes[0]
max_index = 0

for count in range(len(candidates)):
    total_percentage_votes = total_votes[count]/votes*100
    percentage_votes.append(total_percentage_votes)
    if total_votes[count] > max:
        max = total_votes[count]
        print(max)
        max_index = count
winner = candidates[max_index]

# Print Statements
print("Election Results")
print("----------------------")
print(f"Total Votes: {votes}")
print("------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentage_votes[count]}% ({total_votes[count]}")
print(f"Winner: {winner}")

# output file
#variable for output file
pybank_analysis = os.path.join("PyPoll_final.txt")
#export text file
with open(pypoll_analysis, "w") as txtfile:
        txtfile.write("FinalScript")
        txtfile.write("Election Results")
        txtfile.write("----------------------------")
        txtfile.write(f"Total Votes: {votes}")
        txtfile.write("------------------------")
        txtfile.write(f"{candidates[count]}: {percentage_votes[count]}% ({total_votes[count]}")
        txtfile.write(f"Winner: {winner}")