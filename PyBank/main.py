import csv
path = "Resources/budget_data.csv"

csv_file = open(path)
csv_reader = csv.reader(csv_file)

next(csv_file)


months = 0
net_total = 0
greatest_inc = 0
greatest_dec = 0
avg_list = []

for row in csv_reader:
    months += 1
    net_total += int(row[1])
    avg_list.append = int(row[1])

