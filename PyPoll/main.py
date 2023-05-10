import os
import csv

election_csv = "PyPoll/Resources/election_data.csv"

def election_votes(election_csv):
    with open(election_csv, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        data = list(csv_reader)

# calculae total number of votes 
    total_votes = len(data)

    candidates = set()

    votes_per_candidate = {}

    for row in data:
        candidate = row[2]
        candidates.add(candidate)
        votes_per_candidate[candidate] = votes_per_candidate.get(candidate, 0) + 1

# Calculate the percentage of votes of each candidate
    percentage_per_candidate = {}
    for candidate, votes in votes_per_candidate.items():
        percentage = (votes / total_votes) * 100
        percentage_per_candidate[candidate] = round(percentage, 3)

# Sort the candidates in descending order
    sorted_candidates = sorted(candidates, key=lambda 
                               candidate: votes_per_candidate[candidate], reverse=True)

    # Find the candidate with the maximum votes
    winner = sorted_candidates[0]

    # print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates:
        votes = votes_per_candidate[candidate]
        percentage = percentage_per_candidate[candidate]
        print(f"{candidate}: {percentage}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# export results to a text file
    output_filename = "PyPoll/analysis/election_results.txt"
    with open(output_filename, "w") as output_file:
        output_file.write("Election Results\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("-------------------------\n")
        for candidate in candidates:
            votes = votes_per_candidate[candidate]
            percentage = percentage_per_candidate[candidate]
            output_file.write(f"{candidate}: {percentage}% ({votes})\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Winner: {winner}\n")
        output_file.write("-------------------------\n")

election_votes(election_csv)
