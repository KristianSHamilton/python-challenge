import os
import csv

candidateList = []
totalVotes =  0

csvPath = os.path.join( ".","Resources","election_data.csv")
Vote_Analysis_Export = os.path.join(".", "Analysis","Vote_Analysis.txt")

#Read CSV from path
with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")
    
    csvHeader = next(csvReader)
    
    print(csvHeader)  

    for row in csvReader: 
        
        candidateName = row[2]
        totalVotes = totalVotes + 1
        if candidateName not in candidateList:
            
            candidateList.append(candidateName)
        


output = (
#"Financial Analysis\n"
#"-----------------------------\n"
f"Total Votes: {totalVotes}\n"
#f"Total Profit: ${}\n"
#f"Average Change: ${}\n"
#f"Greatest Increase in Profits: ${}\n"
#f"Greatest Decrease in Profits: ${}"
)

print(output)

#writes output to file
with open(Vote_Analysis_Export, "w") as txt_file:
    txt_file.write(output)