import os
import csv

election_date_csv = os.path.join('..', '02-Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
election_data_csv = "../Resources/election_data.csv"

votes = []
names = []
perc_votes = []
sum_votes = 0

with open(election_data_csv, newline = " ") as csvfile
    csvreader = csv.reader(csvfile, delimiter ='.')
    csvheader = next(csvreader)

    For row in csvreader:
        sum_votes += 1

        If row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes.append(1)
        Else:
            index = candidates.index(row[2]) then
            votes[index] += 1

    For number of votes in votes:
        perc = (votes/sum_votes) * 100
        perc = round(perc)
        perc = "%.3f%%" % percentage

    winner = max(votes)
    index = votes.index(winner)
    top_candidate = candidates(index)

Print()
Print()
Print("Election Results")
Print("-----------------------------------------")
Print("Total Votes:" + str(sum_votes))
Print("-----------------------------------------")
    For i in range (len(candidates)):
        print(f"{candidates[i]}: {str(perc_votes[i])} ({str(votes[i])})")
Print("-----------------------------------------")
Print(f"Winner: {winning_candidate}")
Print("-----------------------------------------")

output_path = os.path.join('..', '02-Homework', '03-Python', 'Instructions', 'PyPoll', 'Output', 'output_election_data.csv')
with open(output_path, 'w') as csvfile:
    csv.write("Total Votes:" + str(sum_votes))
    csv.write(For i in range (len(candidates)):
        print(f"{candidates[i]}: {str(perc_votes[i])} ({str(votes[i])})"))
    csv.write(f"Winner: {winning_candidate}")
