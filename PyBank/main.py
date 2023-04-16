import csv
path = "Resources/budget_data.csv"

csv_file = open(path)
csv_reader = csv.reader(csv_file)

next(csv_file)


months = 0
net_total = 0.0
greatest_inc = 0.0
greatest_dec = 0.0



