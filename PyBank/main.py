import os
import csv

# open csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)


    print("Financial Analysis")
    print("---------------------")
# initial variables
    initial = next(csvreader)
    dates = []
    num_rows = 1
    total = int(initial[1]) #start w day 1 
    change = 0 # aka value of the day after 
    day_before = int(initial[1]) # aka value of the day before
    profits = []
    
    for row in csvreader:

    # total  months
        dates.append(row[0])
        num_rows += 1
    # total amount of profit/losses
        total += int(row[1])
    # to find out profits/losses
        change = int(row[1])- day_before
        day_before = int(row[1])
        profits.append(change)
        

   #Average change over the entire period 
    period = len(profits)
    total_pr = sum(profits)
    avg_change = "{:.2f}".format(total_pr/ period)

    #Greatest increase in profits over the entire period
    greatest_increase = max(profits)
    greatest_date = dates[profits.index(greatest_increase)]

    #Greatest decrease in loss over the entire period 
    greatest_decrease = min(profits)
    decrease_date = dates[profits.index(greatest_decrease)]
   

# print in terminal
print("Total Months: ", num_rows)
print("Total: $", total)
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# export txt file
output = open("output.txt", "w")
text0 = "text"
text1 = "Financial Analysis"
text2 = "---------------------"
text3 = (f"Total Months: {num_rows}")
text4 = (f"Total: ${total}")
text5 = (f"Average Change: ${avg_change}")
text6 = (f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
text7 = (f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(text0,text1,text2,text3,text4,text5,text6,text7))