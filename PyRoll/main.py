import os
import csv
import sys

def addCandidate(candidate):
    if not candidate in candidatesList.keys():
        candidatesList[candidate] = 1
    else:
        candidatesList[candidate] = candidatesList[candidate] + 1

original = sys.stdout
output_file = "Resources/output.txt"
sys.stdout = open(output_file, 'w')

file_path = os.path.join('Resources','election_data.csv')
totalVotes = 0
candidatesList = {}
print("Election Results")
print("-------------------------")

with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        totalVotes = totalVotes + 1
        addCandidate(row[2])

print("Total Votes: " + str(totalVotes))
print("-------------------------")
winner = ""
maxVotes = 0
for candidate in candidatesList.keys():
    votes = candidatesList[candidate]
    if votes > maxVotes:
        winner = candidate
        maxVotes = votes
    percentage = votes/totalVotes
    print(candidate + ": " + "{0:.3%}".format(percentage) + " (" + str(votes) + ")")

print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

sys.stdout = original
print(open(output_file, 'r').read())
