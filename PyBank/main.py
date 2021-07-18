import os
import csv

monthsTotal = 0
profitTotal = 0
profitDelta = 0
profitPrior = 0
profitDeltaTotal = 0
profitDeltaGreatest = 0
profitDeltaLeast = 0

csvPath = os.path.join( ".","Resources","budget_data.csv")
Financial_Analysis_Export = os.path.join(".", "Analysis","Financial_Analysis.txt")

#Read CSV from path
with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")
    
    csvHeader = next(csvReader)
    
    #skip headers in first row set data accordingly
    firstRow = next(csvReader)
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

# calc average change by dividing profit Delta by monthsTotal - 1 to account for nonexistent change on first month
avgChange = profitDeltaTotal/(monthsTotal - 1)

output = (
"Financial Analysis\n"
"-----------------------------\n"
f"Total Months: {monthsTotal}\n"
f"Total Profit: ${profitTotal}\n"
f"Average Change: ${avgChange}\n"
f"Greatest Increase in Profits: ${profitDeltaGreatest}\n"
f"Greatest Decrease in Profits: ${profitDeltaLeast}"
)

print(output)

#writes output to file
with open(Financial_Analysis_Export, "w") as txt_file:
    txt_file.write(output)