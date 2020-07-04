import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data

    header = next(reader)

    for row in reader:

        total_votes = total_votes + 1

       name = row[2]

       if name not in candidates:
           candidaates[name] = 1
        
        else:candidates[name] = candidates[name] + 1



print("Total Votes", total_votes)

for candidate_name, vote_count in candidates.items():
    percentage = vote_count / total_votes * 100
    print(f"{candidate_name}: {vote_count}, {percentage}")
   
    
#The total number of votes cast

#A complete list of candidates who received votes

# The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:
