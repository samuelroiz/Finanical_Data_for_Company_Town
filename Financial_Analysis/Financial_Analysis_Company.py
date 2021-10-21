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
    #print(total_months)
    #print(f"Total numbers of rows: {csvreader.line_num - 1}")

    #print out the total of months
    print(f"Total numbers of months : {total_months}")

#def. of sum
def sum_columns(x):
    total = 0
    mysum = x[1]
    total += int(mysum)
    sum_columns.variable = total

#Section for "Sum of Profit/Losses"
total = 0
with open(csvpath, 'r') as csvfile:
    next(csvfile) #skips header
    csvreader = csv.reader(csvfile, delimiter=",") 
    for column in csvreader:
        mysum = column[1]
        total += int(mysum)
        
        # To find max and min
        split_mysum = mysum.split()
        res = [int(i) for i in split_mysum]
        list_of_column = []
        list_of_column = res
        blank = []
        blank_again = []
        b = []
        flatten_list = [(int())]
        # print(list_of_column)
        max_number = max(list_of_column)
        blank.extend(res)
        print(blank)
        blank_again[len(blank_again):]=res
        print(blank_again)
        jj = [y for x in (b, res) for y in x]
        print(jj)
        # for subl in res:
        #     for item in subl:
        #         flatten_list.append(item)
        print([i for row in [res] for i in row])
        y = sum(flatten_list, res)
        print(y)
        # print(flatten_list)








average = ((total)/(total_months))
average_rdup = round(average, 2)






print(f"Total: ${total}")
print(f"Average: ${average_rdup}")
# print(f"Average each month: ${average_rdup_month}")
# print(f"Greatest Increase in Profits: {date} ({h_value}) ")
# print(f"Greatest Decrease in Profits: {date} ({l_value}) ")

# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     for col in row:
#         #print("%10s"%col),
#         print(col)
#     print('\n')