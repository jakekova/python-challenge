import csv
import statistics

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
    avg_list.append(int(row[1]))
    if int(row[1]) > greatest_inc:
        greatest_inc = int(row[1])
        greatest_inc_date = row[0]
    elif int(row[1]) < greatest_dec:
        greatest_dec = int(row[1])
        greatest_dec_date = row[0]

print("Financial Analysis")
print('')
print("---------------------")
print('')
print(f"Total Months: {months}")
print('')
print(f'Total: ${net_total}')
print('')
print(f'Average Change: ${round(statistics.fmean(avg_list), 2)}')
print('')
print(f'Greatest Increase in Profits: {greatest_inc_date} : {greatest_inc}')
print('')
print(f'Greatest Decrease in Profits: {greatest_dec_date} : {greatest_dec}')