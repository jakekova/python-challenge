import csv

# set up csv access

path = "Resources/election_data.csv"

csv_file = open(path)
csv_reader = csv.reader(csv_file)

# skip header
next(csv_file)

# define varibles 

votes = 0
candidate_list = []
charles_vote = 0
diana_vote = 0
raymon_vote = 0

for row in csv_reader:
    #each row is a vote
    votes += 1
    #first candidate starts the lists of candidates
    candidate_name = row[2]
    #if a new name occurs, add it to list
    if candidate_name not in candidate_list:
        candidate_list.append(candidate_name)
    # count votes according to who is running and when the name occurs
    if row[2] == "Charles Casper Stockham":
        charles_vote += 1
    elif row [2] == "Diana DeGette":
        diana_vote += 1
    elif row [2] == "Raymon Anthony Doane":
        raymon_vote += 1
# make percentages 
charles_perc = round(((charles_vote / votes) * 100),3)
diana_perc = round(((diana_vote / votes) * 100),3)
raymon_perc = round(((raymon_vote / votes) * 100),3)
# find winner
if charles_vote > diana_vote and raymon_vote:
    winner = "Charles Casper Stockha"
elif diana_vote > charles_vote and raymon_vote:
    winner = "Diana DeGette"
elif raymon_vote > charles_vote and diana_vote:
    winner = "Raymon Anthony Doane"

print(winner)

print("Election Results")
print(" ")
print("-------------------------")
print(" ")
print(f"Total Votes: {votes}")
print(" ")
print("-------------------------")
print(" ")
print(f"{candidate_list[0]}: {charles_perc} ({charles_vote})")
print(" ")
print(f"{candidate_list[1]}: {diana_perc} ({diana_vote})")
print(" ")
print(f"{candidate_list[2]}: {raymon_perc} ({raymon_vote})")
print(" ")
print("-------------------------")
print(" ")
print(f"Winner: {winner}")
print(" ")
print("-------------------------")

with open("analysis/analysis.txt", "w") as txt_file:
    txt_file.write("Election Results \n"
                   "\n"
                   "------------------------- \n"
                   "\n"
                   f"Total Votes: {votes} \n"
                   "\n"
                   "------------------------- \n"
                   "\n"
                   f"{candidate_list[0]}: {charles_perc} ({charles_vote}) \n"
                   "\n"
                   f"{candidate_list[1]}: {diana_perc} ({diana_vote}) \n"
                   "\n"
                   f"{candidate_list[2]}: {raymon_perc} ({raymon_vote}) \n"
                   "\n"
                   "------------------------- \n"
                   "\n"
                   f"Winner: {winner} \n"
                   "\n"
                   "------------------------- \n"
    )
