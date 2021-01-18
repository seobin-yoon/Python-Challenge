import os
import csv
# open csv file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    print("Election Results")
    print("----------------------------")
    #initial values of variables
    vote_Khan = 0
    vote_Correy = 0
    vote_Li = 0
    vote_OTooley = 0 
    num_rows = 0
    for row in csvreader:
    # total votes
        num_rows += 1 

        if row[2] == "Khan":
            vote_Khan += 1
            
        elif row[2] == "Correy":
            vote_Correy += 1

        elif row[2] == "Li":
            vote_Li += 1

        else:
            vote_OTooley += 1
    #percentage of each candidate
    perc_Khan = "{:.3f}".format(vote_Khan *100 / num_rows)
    perc_Correy = "{:.3f}".format(vote_Correy *100 / num_rows)
    perc_Li = "{:.3f}".format(vote_Li *100 / num_rows)
    perc_OTooley = "{:.3f}".format(vote_OTooley *100 / num_rows)

    # Find winner 

    list1 = [perc_Khan, perc_Correy, perc_Li, perc_OTooley]
    if max(list1) ==  perc_Khan:
        winner_name = "Khan"
                
    elif max(list1) ==  perc_Correy:
        winner_name = "Correy"

    elif max(list1) == perc_Li:
        winner_name = "Li"

    else:
        winner_name = "O'Tooley"
    
    # print in terminal
    print("Total Voters: ", num_rows)
    print("----------------------------")
    print(f"Khan: {perc_Khan}% ({vote_Khan})")
    print(f"Correy: {perc_Correy}% ({vote_Correy})")
    print(f"Li: {perc_Li}% ({vote_Li})")
    print(f"O'Tooley: {perc_OTooley}% ({vote_OTooley})")
    print("----------------------------")
    print(f"Winner: {winner_name}")
    print("----------------------------")
     
    # export txt file
    output = open("output.txt", "w")
    text0 = "text"
    text1 = "Election Results"
    text2 = "--------------------------"
    text3 = (f"Total Voters: {num_rows}")
    text4 = "--------------------------"
    text5 = (f"Khan: {perc_Khan}% ({vote_Khan})")
    text6 = (f"Correy: {perc_Correy}% ({vote_Correy})")
    text7 = (f"Li: {perc_Li}% ({vote_Li})")
    text8 = (f"O'Tooley: {perc_OTooley}% ({vote_OTooley})")
    text9 = "--------------------------"
    text10 = (f"Winner: {winner_name}")
    text11= "--------------------------"
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(text0,text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11))
        



