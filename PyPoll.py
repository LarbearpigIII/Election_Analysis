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

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)

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

