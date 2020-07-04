import os
import csv

csv_path = os.path.join("budget_data.csv")

dates = []
profits = []
average_change = []

with open(csv_path , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        print(row[0])
        print(row[1])
        dates.append(row[0])
        profits.append(int(row[1]))

#find min and max index
biggestIndex = 0
smallestIndex = 0

for index in range(1, len(dates)):
    if profits[biggestIndex] < profits[index]:
        biggestIndex = index
    if profits[smallestIndex] > profits[index]:
        smallestIndex = index

print("Total Months:", len(dates))
print("Total:", sum(profits))
change = len(dates) / sum(profits)
print("Average Change:" , change)

print("Greatest Increase in Profits:", dates[biggestIndex], (profits[biggestIndex]))

print("Greatest Decrease in Profits:", dates[smallestIndex], (profits[smallestIndex]))

#Total Months: 86
 # Total: $38382578
 # Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)


    
