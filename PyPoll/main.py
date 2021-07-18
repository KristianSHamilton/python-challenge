import os
import csv

candidateList = []
totalVotes =  0
candidateVote = {}

csvPath = os.path.join( ".","Resources","election_data.csv")
Vote_Analysis_Export = os.path.join(".", "Analysis","Vote_Analysis.txt")

#Read CSV from path
with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")
    #read header
    csvHeader = next(csvReader)
     

    for row in csvReader: 
        
        candidateName = row[2]
        totalVotes = totalVotes + 1
       
        if candidateName not in candidateList:
            
            candidateList.append(candidateName)
            candidateVote[candidateName] = 0
    
        candidateVote[candidateName] = candidateVote[candidateName] + 1
    
    #prints voting stats for each candidate within the candidate list
    for candidateName in candidateList:
        #calcs percentage of votes for each candidate, x 100 to go from decimal to percentage
        votePercentage = candidateVote[candidateName] / totalVotes * 100
        #prints stats, votePercentage casted as integer to round decimal places to whole number
        print(f"{candidateName}: {int(votePercentage)}% ({candidateVote[candidateName]} votes)")

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