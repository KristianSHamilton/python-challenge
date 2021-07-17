import os
import csv

csvPath = os.path.join( ".","budget_data.csv")

with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")

    #print(csvreader)
    
    csvHeader = next(csvReader)
    print(f"CSV Header: {csvHeader}")
    for row in csvReader:
        print(row)
