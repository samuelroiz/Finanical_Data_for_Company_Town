import os
import csv


print()
print("Election Results")
print("- " * 15)

#Path for csv File
csvpath = os.path.join("Resources", "election_data.csv")

fields = []
rows = []


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
    #Extra row, so we must delete the first row in order to count all of the months
    total_voters = csvreader.line_num - 1

    #print out the total of voters
    print(f"Total voters : {total_voters}")
    
with open(csvpath, 'r') as csvfile:
    next(csvfile) #skips header
    csvreader = csv.reader(csvfile, delimiter=",")

    vote_name = []
    khan_votes = 0
    khan_vote_total = 0
    correy_votes = 0
    correy_vote_total = 0
    li_votes = 0
    li_vote_total = 0
    otooley_votes = 0
    otooley_vote_total = 0

    for row in csvreader:
        
        vote_name = row[2]
        if vote_name == "Khan":
            khan_votes += 1
            khan_vote_total = khan_votes
            # khan_vote_total = khan_votes
        elif vote_name == "Correy":
            correy_votes += 1
            correy_vote_total = correy_votes
        elif vote_name == "Li":
            li_votes += 1
            li_vote_total = li_votes
        elif vote_name == "O'Tooley":
            otooley_votes += 1
            otooley_vote_total = otooley_votes
    
    khan_percentage = ((khan_vote_total/total_voters) * 100)
    khan_percentage_rd_up = round(khan_percentage , 2)
    correy_percentage = ((correy_vote_total/total_voters) * 100)
    correy_percentage_rd_up = round(correy_percentage, 2)
    li_percentage = ((li_vote_total/total_voters) * 100)
    li_percentage_rd_up = round(li_percentage , 2)
    otooley_percentage = ((otooley_vote_total/total_voters) * 100)
    otooley_percentage_rd_up = round(otooley_percentage, 2)
    print("- " * 15)
    print(f"Khan: {khan_percentage_rd_up}% ({khan_vote_total})")
    print(f"Correy: {correy_percentage_rd_up}% ({correy_votes})")
    print(f"Li: {li_percentage_rd_up}% ({li_votes})")
    print(f"O'Tooley: {otooley_percentage_rd_up}% ({otooley_votes})")
    print("- " * 15)
    if khan_vote_total > correy_vote_total and khan_vote_total > li_vote_total and khan_vote_total > otooley_vote_total:
        print("Winner: Khan")
    elif correy_vote_total > khan_vote_total and correy_vote_total > li_vote_total and correy_vote_total > otooley_vote_total:
        print("Winner: Correy")
    elif li_vote_total > khan_vote_total and li_vote_total > correy_vote_total and li_vote_total > otooley_vote_total:
        print("Winner: Li")
    elif otooley_vote_total > khan_vote_total and otooley_vote_total > correy_vote_total and otooley_vote_total > li_vote_total:
        print("Winner: O'Tooley")


    print("- " * 15)