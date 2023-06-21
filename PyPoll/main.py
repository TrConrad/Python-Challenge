' Import OS and CSV'

import os
import csv
import shutil

'Establish variables'

Voter_ID = []
County = []
Candidate = []
Charles_count = 0.0
Diana_count = 0.0
Raymon_count = 0.0


' Set up path and CSV reader'

csvpath= os.path.join("Resources", "election_data.csv")


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:

        'establish each list'

        Voter_ID.append(int(row[0]))
        County.append(row[1])
        Candidate.append(row[2])


'count total number of votes for each Candidate'

Charles_count = Candidate.count("Charles Casper Stockham")
Diana_count = Candidate.count("Diana DeGette")
Raymon_count = Candidate.count("Raymon Anthony Doane")

'Find the percentage of votes each Candidate recieved'
charles = round((Charles_count/(len(Voter_ID)))*100, 3)
diana = round((Diana_count/(len(Voter_ID)))*100, 3)
raymon = round((Raymon_count/(len(Voter_ID)))*100, 3)

'create path and  text file'
save_path = "home/Python-Challenge/PyPoll/Analysis"
file = open("Election_Results.txt", "w")


'print analysis of Election Data'
print("Election Results")
print("---------------------")
file.write("Election Results \n")
file.write("--------------------- \n")

'Find total number of votes'
print("Total Votes: " + str(len(Voter_ID)))
print("---------------------")
file.write("Total Votes: " + str(len(Voter_ID)) + "\n")
file.write("--------------------- \n")


'Print the voter name, percent of votes they won, and total number of votes they won'
print("Charles Casper Stockholm: " + str(charles) + "% (" + str(Charles_count) + ")")
print("Diana DeGette: " + str(diana) + "% (" + str(Diana_count) + ")")
print("Raymon Anthony Doane: " + str(raymon) + "% (" + str(Raymon_count) + ")")
print("---------------------")
file.write("Charles Casper Stockholm: " + str(charles) + "% (" + str(Charles_count) + ") \n")
file.write("Diana DeGette: " + str(diana) + "% (" + str(Diana_count) + ") \n")
file.write("Raymon Anthony Doane: " + str(raymon) + "% (" + str(Raymon_count) + ") \n")
file.write("--------------------- \n")

'Determine and print the Election winner'

winner= max(charles, diana, raymon)
if winner == charles:
    print("Winner: Charles Casper Stockham")
    file.write("Winner: Charles Casper Stockham \n")
elif winner == diana:
    print("Winner: Diana DeGette")
    file.write("Winner: Diana DeGette \n")
else:
    print("Winner: Raymon Anthony Doane")
    file.write("Winner: Raymon Anthony Doane \n")

print("---------------------")
file.write("--------------------- \n")

'close the file'
file.close()

'move the file to the correct folder'
'move text file to correct folder'
current_loc = "C:\\Users\Tiffa\\Python-Challenge\\PyPoll\\Election_Results.txt"
new_loc = "C:\\Users\\Tiffa\\Python-Challenge\\PyPoll\\Analysis\\Election_Results.txt"
shutil.move(current_loc, new_loc)

