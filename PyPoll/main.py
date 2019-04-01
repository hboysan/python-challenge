#import os and csv files
import os
import csv

#set path
electiondata_csv = os.path.join('Resources', 'election_data.csv')

#initialize variables
candidates = []
total_votes = 0
vote_counts = []

#open the file
with open(electiondata_csv,newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)

   #go row by row and process each vote
   for row in csvreader:

       #add to total number of votes
       total_votes = total_votes + 1

       #candidate voted for
       candidate = row[2]

       #if candidate has other votes then add to vote tally
       if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_counts[candidate_index] = vote_counts[candidate_index] + 1
       #else create new spot in list for candidate
       else:
           candidates.append(candidate)
           vote_counts.append(1)

percentage = []
max_votes = vote_counts[0]
max_index = 0

#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
   vote_percentage = round(((vote_counts[count]/total_votes)*100),1)
   percentage.append(vote_percentage)

   if vote_counts[count] > max_votes:
       max_votes = vote_counts[count]
       print(max_votes)
       max_index = count

winner = candidates[max_index]

#print results
print("```text\n",
"Election Results\n",
"--------------------------\n",
f"Total Votes: {total_votes}")
for count in range(len(candidates)):
   print(f"{candidates[count]}: {percentage[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")
print("```")

with open('election_data.txt', 'w') as text:
    text.write("```text")
    text.write("Election Results")
    text.write("--------------------------")
    text.write(f"Total Votes: {total_votes}")
    for count in range(len(candidates)):
        text.write(f"{candidates[count]}: {percentage[count]}% ({vote_counts[count]})")
    text.write("---------------------------")
    text.write(f"Winner: {winner}")
    text.write("---------------------------")
    text.write("```")
