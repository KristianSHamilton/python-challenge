import os
import csv



csvPath = os.path.join( ".","Resources","election_data.csv")
Vote_Analysis_Export = os.path.join(".", "Analysis","Vote_Analysis.txt")

#Read CSV from path
with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")
    
    csvHeader = next(csvReader)
    
  
    
#    for row in csvReader:
       


output = ("test"
#"Financial Analysis\n"
#"-----------------------------\n"
#f"Total Months: {}\n"
#f"Total Profit: ${}\n"
#f"Average Change: ${}\n"
#f"Greatest Increase in Profits: ${}\n"
#f"Greatest Decrease in Profits: ${}"
)

print(output)

#writes output to file
with open(Vote_Analysis_Export, "w") as txt_file:
    txt_file.write(output)