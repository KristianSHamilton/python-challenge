import os
import csv

monthsTotal = 0
profitTotal = 0
profitDelta = 0
profitPrior = 0
profitDeltaTotal = 0
profitDeltaGreatest = 0
profitDeltaLeast = 0

csvPath = os.path.join( ".","budget_data.csv")

#Read CSV from path
with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")
    
    csvHeader = next(csvReader)
    
    #skip headers in first row
    firstRow = next(csvReader)
    profitDeltaTotal = int(firstRow[1])
    profitPrior = int(firstRow[1])
    monthsTotal = 1
    profitTotal = int(firstRow[1])
    
    for row in csvReader:
        #increments month  variable for every row
        monthsTotal = monthsTotal + 1
        #adds current  row's profit to the total profit variable
        profitTotal = profitTotal + int(row[1])
        #calcs change in price by subtracting the last row's profit from the current
        profitDelta = int(row[1]) - profitPrior
        #keeps a running total of  the price changes by adding current row delta to total variable
        profitDeltaTotal = profitDeltaTotal + profitDelta
        #now that profitPrior has  been  used in current loop, sets variable for next loop
        profitPrior = int(row[1])
        #finds greatest Delta value
        if profitDelta > profitDeltaGreatest:
            profitDeltaGreatest = profitDelta
        #finds smallest Delta value    
        if profitDelta < profitDeltaLeast:
            profitDeltaLeast = profitDelta


avgChange = profitDeltaTotal/monthsTotal

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {monthsTotal}")
print(f"Total Profit: ${profitTotal}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: ${profitDeltaGreatest}")
print(f"Greatest Decrease in Profits:  ${profitDeltaLeast}")
