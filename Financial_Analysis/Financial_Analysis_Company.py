import os
import csv

#Path for csv File
csvpath = os.path.join("Resources", "budget_data.csv")

fields = []
rows = []
columns = []

#print out intro. of code
print("Financial Analysis")
print("- " * 30)

#Section for "Printing amount of months"
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
    #Extra row, so we must delete the first row in order to count all of the months
    total_months = csvreader.line_num - 1

    #print out the total of months
    print(f"Total numbers of months : {total_months}")

#Section for "Sum of Profit/Losses"
total = 0
with open(csvpath, 'r') as csvfile:
    next(csvfile) #skips header
    csvreader = csv.reader(csvfile, delimiter=",")
    yesterday = 0
    yearly_change = []
    max_yearly_change = []
    print_yearly_change = []
    average_round_up_list = []
    date_list = []
    for row in csvreader:

        today = row[1]
        mysum = row[1]

        change = int(today) -int(yesterday)

        yearly_change.append(change)

        average_round_up = change/total_months
        
        average_round_up_list.append(average_round_up)

        print_yearly_change.extend([int(today), int(yesterday), int(change)])

        max_yearly_change.append(int(change))

        yesterday = today
        
        total += int(mysum)

    maximum_yearly_change = max(max_yearly_change)
    minimum_yearly_change = min(max_yearly_change)
    avg_month = sum(average_round_up_list)
    avg_month_rd_up = round(avg_month, 2)

average = ((total)/(total_months))
average_rdup = round(average, 2)

with open(csvpath, 'r') as csvfile:
    next(csvfile) #skips header
    csvreader = csv.reader(csvfile, delimiter=",")
    yesterday = 0
    date_change = []
    for row in csvreader:
        today = row[1]
        date = row[0]

        change = int(today) -int(yesterday)
        yesterday = today

        if change == int(maximum_yearly_change):
            max_date = date
        elif change == int(minimum_yearly_change):
            min_date = date

print()
print(f"Total: ${total}")
print(f"Average amount: ${average_rdup}")
print(f"Average each month: ${avg_month_rd_up}")
print(f"Greatest Increase in Profits: {max_date} (${maximum_yearly_change}) ")
print(f"Greatest Decrease in Profits: {min_date} (${minimum_yearly_change}) ")
