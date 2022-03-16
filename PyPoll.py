#import dependencies
import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#initialize Candidate Options
candidate_options = []

#initialize candidate dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     # Print the header row.
     headers = next(file_reader)

     #The data we need to retrieve.
     
     for row in file_reader:
          # obtain the total number of votes cast
          total_votes += 1
          
          # obtain list of candidates who received votes
          candidate_name = row[2]
          # Add the candidate name to the candidate list.
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               
               #initialize tracking that candidates vote count
               candidate_votes[candidate_name] = 0
               
          #Add a vote to that candiddate's count
          candidate_votes[candidate_name] += 1
     
     # Determine the percentage of votes for each candidate by looping through the counts.
     for candidate_name in candidate_votes:
          #retrieve number of votes for candidate
          votes = candidate_votes[candidate_name]
          #calculate % of total
          vote_percentage = float(votes) / float(total_votes) * 100
          
          #print each candidate
          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          
          # Determine winning vote count and candidate
          # 1. Determine if the votes are greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # 2. If true then set winning_count = votes and winning_percent =
               # vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # 3. Set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name

winning_candidate_summary = (
     f"-------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-------------------------\n")
print(winning_candidate_summary)


          






# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")