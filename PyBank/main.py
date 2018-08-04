import os
import csv
import sys
import numpy as np
from datetime import datetime


original = sys.stdout
output_file = "Resources/output.txt"
sys.stdout = open(output_file, 'w')

file_path = os.path.join('Resources','budget_data.csv')

countMonths = 0
totalNetAmount = 0
greatestIncrease = 0
greatestIncreaseDate = ""
greatestDecrease = 0
greatestDecreaseDate = ""
averageChange = []
prevAmount = 0
with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for index, row in enumerate(reader):
        countMonths = countMonths + 1
        amount = float(row[1])
        totalNetAmount = totalNetAmount + amount
        if index != 0:
            periodDiff = amount - prevAmount
            averageChange.append(periodDiff)
            if periodDiff > greatestIncrease:
                greatestIncrease = periodDiff
                greatestIncreaseDate = row[0]
            if periodDiff < greatestDecrease:
                greatestDecrease = periodDiff
                greatestDecreaseDate = row[0]
        prevAmount = amount


print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(countMonths))
print("Total: ${:,.2f}".format(totalNetAmount))
print("Average Change: " + " ${:,.2f}".format((np.mean(averageChange))))

print("Greatest Increase in Profits: " + datetime.strptime("1-" + greatestIncreaseDate, "%d-%b-%y").strftime("%b-%Y")
      + " (${:,.2f}".format(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + datetime.strptime("1-" + greatestDecreaseDate, "%d-%b-%y").strftime("%b-%Y")
      + " (${:,.2f}".format(greatestDecrease) + ")")

sys.stdout = original
print(open(output_file, 'r').read())