import os
import csv

candidateList = []
totalVotes =  0
candidateVote = {}
votePercentage = {}
winningTotal = 0

csvPath = os.path.join( ".","Resources","election_data.csv")
Vote_Analysis_Export = os.path.join(".", "Analysis","Vote_Analysis.txt")

#Read CSV from path
with open(csvPath) as csvFile: 

    csvReader = csv.reader(csvFile, delimiter = ",")
    
    #read header
    csvHeader = next(csvReader)
     
    for row in csvReader: 
        
        #for each loop assign vote to candidateName
        candidateName = row[2]
        
        #increment total votes cast by one each loop
        totalVotes = totalVotes + 1
        
        #adds candidate name to the list if they are not already on there
        if candidateName not in candidateList:
            
            candidateList.append(candidateName)
            
            #candidateVote set to 0 if it is their first vote
            candidateVote[candidateName] = 0
        
        #adds vote to respective candidate in candidateVote list
        candidateVote[candidateName] = candidateVote[candidateName] + 1
    
    for candidateName in candidateList:
        
        #calcs percentage of votes for each candidate, x 100 to go from decimal to percentage
        votePercentage[candidateName] = candidateVote[candidateName] / totalVotes * 100
        
        #loops through to see which candidate won and saves their name to a variable for printing later
        if candidateVote[candidateName] > winningTotal :
            
            winningTotal = candidateVote[candidateName]
           
            winner = candidateName
            


#writes output to file and prints to prompt
with open(Vote_Analysis_Export, "w") as txt_file:
    
    electionHeader = (f"Election Results\n"
                      f"-----------------------------\n"
                      f"Total Votes: {totalVotes}\n")
    
    print(electionHeader)
    
    txt_file.write(electionHeader)
    
    for candidateName in candidateList:
        
        #prints stats, votePercentage casted as integer to round decimal places to whole number
        electionBody = f"{candidateName}: {int(votePercentage[candidateName])}% ({candidateVote[candidateName]} votes)\n"
                         
        print(electionBody)
        
        txt_file.write(electionBody)
    
    electionWinner = (f"-----------------------------\n"
                      f"Winner: {winner}\n"
                      f"-----------------------------\n")
    
    print(electionWinner)
    
    txt_file.write(electionWinner)