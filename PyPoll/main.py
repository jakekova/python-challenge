import csv

path = "Resources/election_data.csv"

csv_file = open(path)
csv_reader = csv.reader(csv_file)

next(csv_file)


votes = 0
candidate_list = []

for row in csv_reader:
    votes += 1
    candidate_list.append(row[2])
    

