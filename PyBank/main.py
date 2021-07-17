import os
import csv

monthsTotal = 0
profitTotal = 0
profitDelta = 0
profitPrior = 0
profitDeltaTotal = 0

csvPath = os.path.join( ".","budget_data.csv")


with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")
    
    csvHeader = next(csvReader)
    
    #skip headers in first row
    firstRow = next(csvReader)
    profitDeltaTotal = int(firstRow[1])
    profitPrior = int(firstRow[1])
    
    for row in csvReader:

        monthsTotal = monthsTotal + 1
        profitTotal = profitTotal + int(row[1])
        profitDelta = int(row[1]) - profitPrior
        print(profitDelta)
        profitDeltaTotal = profitDeltaTotal + profitDelta
        profitPrior = int(row[1])


#        print(row)


print(monthsTotal)
print(profitTotal)
print(profitDelta)
print(profitDeltaTotal)
