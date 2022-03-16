# Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attrivute on hte dattime class to get the present time.
now = dt.datetime.now()
#Print the present time.
print("The time right now is ", now)

# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the mt dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
            # 2. Add to the total vote count.
            total_votes += 1

            #Print the cadidate name from each rowl
            candidate_name = row[2]

            # If the candidate does not match any existing candidate...
            if candidate_name not in candidate_options:
                # Add it to list of candidates.
                candidate_options.append(candidate_name)
                # Begin tracking that candidate's vote count.
                candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
            candidate_votes[candidate_name] += 1

# Determine teh percenage of votes for each candidate by looping through the list
# Iterate throught the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) *100

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    # Print out cach candidate's name vote count, and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Open the electionresults and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)

# Close the file.
election_data.close()

#Create a fliename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")
# Close the file 
txt_file.close()

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

