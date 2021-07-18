import os
import csv

candidateList = []
totalVotes =  0
candidateVote = {}
votePercentage = {}


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
    
    for candidateName in candidateList:
        #calcs percentage of votes for each candidate, x 100 to go from decimal to percentage
        votePercentage[candidateName] = candidateVote[candidateName] / totalVotes * 100



#writes output to file
with open(Vote_Analysis_Export, "w") as txt_file:
    
    electionHeader = (f"Election Results\n"
                    f"-----------------------------\n"
                    f"Total Votes: {totalVotes}\n")
    
    print(electionHeader)
    
    txt_file.write(electionHeader)
    
    for candidateName in candidateList:
        
        #prints stats, votePercentage casted as integer to round decimal places to whole number
        electionPrint = f"{candidateName}: {int(votePercentage[candidateName])}% ({candidateVote[candidateName]} votes)\n"
                         
        print(electionPrint)
        
        txt_file.write(electionPrint)