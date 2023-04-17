import csv
import statistics
import sys
# set up path and csv access

path = "Resources/budget_data.csv"

csv_file = open(path)
csv_reader = csv.reader(csv_file)

next(csv_file)

# define varibles
months = 0
net_total = 0
greatest_inc = 0
greatest_dec = 0
avg_list = []
b = 0

#count months by each row, a continual total, list of changes that i will take the avg of, and an if statement to be locating the largest and smallest changes

for row in csv_reader:
    months += 1
    net_total += int(row[1])
    a = int(row[1])
    avg_list.append(int(a - b))
    if int(a - b) > greatest_inc:
        greatest_inc = int(a - b)
        greatest_inc_date = row[0]
    elif int(a - b) < greatest_dec:
        greatest_dec = int(a - b)
        greatest_dec_date = row[0]

    b = int(row[1])



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
print(f'Greatest Increase in Profits: {greatest_inc_date} : ${greatest_inc}')
print('')
print(f'Greatest Decrease in Profits: {greatest_dec_date} : ${greatest_dec}')

# printed to console above
# pathed and into a text file in the other folder

with open("analysis/analysis.txt", "w") as txt_file:
    txt_file.write("Financial Analysis \n"
                   "\n"
                   "--------------------- \n"
                   "\n"
                   f"Total Months: {months} \n"
                   "\n"
                   f'Total: ${net_total} \n'
                   "\n"
                   f'Average Change: ${round(statistics.fmean(avg_list), 2)} \n'
                   "\n"
                   f'Greatest Increase in Profits: {greatest_inc_date} : ${greatest_inc} \n'
                   "\n"
                   f'Greatest Decrease in Profits: {greatest_dec_date} : ${greatest_dec}'
    )

    