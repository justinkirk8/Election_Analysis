# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has requested the following tasks to complete an election audit of a recent local congressional election for the precinct.

1. Calculate the total number of votes cast.
2. Get a complete list of the counties where votes were cast in the precinct.
3. Calculate the total number of votes cast in each county.
4. Calculate the percentage of votes cast in each county.
5. Determine the county with the largest turn-out.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10 (64-bit), Visual Studio Code

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The turn-out and percentage of turn-out in each county was:
  - Jefferson county had a turn-out of 38855 votes which represented 10.5% of the precinct.
  - Denver county had a turn-out of 306055 votes which represented 82.8% of the precinct.
  - Arapahoe county had a turn-out of 24801 votes which represented 6.7% of the precinct.
- The county with the highest turn-out was: 
   - Denver with 306055 votes which represented 82.8% of the precinct.
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

![PyPoll_challenge_terminal.png](https://github.com/justinkirk8/Election_Analysis/blob/main/Resources/PyPoll_challenge_terminal.png)  

## Election-Audit Summary
This script could easily be used for any election audit so long as the data is proved in csv file that has the same order of column data and is placed in the resources folder. The script automatically collects the name of the counties and the name of the candidates with any votes to begin tally. It then automatically does the analysis performed above.

One improvement that could be made on this script is to add an input request for the file name in the resources folder. Currently one must be comfortable enough with coding in order to edit the file paths or change the csv file to "election_results" every time they want to run the code. The same input could be used to name the .txt file with the analysis as well.

A second improvement would be to run this script from an executable file. This, along with the above improvement, would allow anyone without coding knowledge to use the .exe file, input the file name of the csv they placed in the resources folder, and receive a text file in the analysis folder with their results.

