' Import OS and CSV'

from distutils.file_util import move_file
import os
import csv
import shutil

'Establish variables'

Date = []
Profits = []
total = 0.0
Profit_Changes = []


' Set up path and CSV reader'

csvpath= os.path.join("Resources", "budget_data.csv")


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:

        'establish each list'

        Date.append(row[0])
        Profits.append(int(row[1]))

    'Determine total profits'
    for number in  Profits:    
        total = total + number

    'Determine Profit Changes'
    for changes in Profits[:85]:
        firstmonth = changes
        secondmonth = Profits[Profits.index(changes)+1]
        Profit_Changes.append(secondmonth - firstmonth)
   

'Determine the average profit change by defining the mean function'
def mean(Profit_Changes):
    length = len(Profit_Changes)
    total_changes = 0.0
    for num in Profit_Changes:
        total_changes += num
    return round(total_changes/length, 2)


'determine index values of greatest increase and decrease in profits'
max_date = Profit_Changes.index(max(Profit_Changes))

min_date = Profit_Changes.index(min(Profit_Changes))


'create path and  text file'
save_path = "home/Python-Challenge/PyBank/Analysis"
file = open("Financial_Analysis.txt", "w")


'print analysis and record to text file'
print("Financial Analysis")
print("---------------------")
file.write("Financial Analysis \n")
file.write("--------------------- \n")

'Find total number of months'
print("Total Months: " + str(len(Date)))
file.write("Total Months: " + str(len(Date)) + "\n")

'find total'
print("Total: $" + str(total))
file.write("Total: $" + str(total) + "\n")

'print average change'
print("Average Change: $" + str(mean(Profit_Changes)))
file.write("Average Change: $" + str(mean(Profit_Changes)) + "\n")

'print the greatest profit increase'
print("Greatest Increase in Profits: " +str(Date[max_date+1]) + " $" + str(max(Profit_Changes)))
file.write("Greatest Increase in Profits: " +str(Date[max_date+1]) + " $" + str(max(Profit_Changes)) + "\n")

'print the greatest profit decrease'
print("Greatest Decrease in Profits: " +str(Date[min_date+1]) + " $" + str(min(Profit_Changes)))
file.write("Greatest Decrease in Profits: " +str(Date[min_date+1]) + " $" + str(min(Profit_Changes)) + "\n")

'close text file'
file.close()

'move text file to correct folder'
current_loc = "C:\\Users\Tiffa\\Python-Challenge\\PyBank\\Financial_Analysis.txt"
new_loc = "C:\\Users\\Tiffa\\Python-Challenge\\PyBank\\Analysis\\Financial_Analysis.txt"
shutil.move(current_loc, new_loc)

