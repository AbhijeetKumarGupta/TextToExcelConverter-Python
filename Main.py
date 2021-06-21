import csv
import random
import re

# We will use this import to split a single list into multiple list
from itertools import accumulate 

# Declaration of variable we will need
raceLength = 260.286
index = 0
testStr = ""
average = 0
listIndex = 0

# Declaration of lists we will need
fields = [] 
rows = []
rank = []
name = []
time = []
averageList = []
totalList = []

# Name of the file with data
filename = "f1_monaco.txt"

# Reading file and importing data to field and rows list
with open(filename, 'r') as csvfile:
 
    csvreader = csv.reader(csvfile) 
       
    fields = next(csvreader) 
   
    for row in csvreader:
        rows.append(row)

# Reading rows list and importing data to lists rank, name and time
for i in range (0,10):
    for row in rows[i]:
        if(listIndex == 0):
            rank.append(row)
        elif(listIndex == 1):
            name.append(row)
        else:
            time.append(row)
        listIndex = listIndex + 1
    listIndex = 0
                             
# Reading data in row list and calculating average and putting it in averageList

for i in range (0,10):
    for row in rows[i]:
        if(index == 2):
            testStr = row
            time = re.split('[-:]',testStr)
            for j in range(0,3):
                if(j == 0):
                    average += (float(time[j]) * 3600)
                elif(j ==  1):
                    average += (float(time[j]) * 60)
                else:
                    average += float(time[j])
        if(average>0):
            averageList.append(((260.286/average)*3600))
        index = index + 1
        average = 0
    index = 0

# Some more variables we will need in this part to keep track of rows and column
tempInd = 0
rankInd = 0
nameInd = 0
aveInd = 0

# Merging all lists to create a list with total values
 # Adding fields
for i in range (0, 3):
    if(i<2):
        totalList.append(fields[i])
    elif(i == 2):
        totalList.append('Average Speed (km\h)')

 # Adding rest of the data
for i in range (0, 30):
    if(tempInd == 0):
        totalList.append(rank[rankInd])
        rankInd = rankInd + 1
        tempInd = tempInd + 1
    elif(tempInd == 1):
        totalList.append(name[nameInd])
        nameInd = nameInd + 1
        tempInd = tempInd + 1
    elif(tempInd == 2):
        totalList.append(str(averageList[aveInd]))
        aveInd = aveInd + 1
        tempInd = 0

# It tells how many parts list should be divided and each part contain how many elements
length_to_split = [3,3,3,3,3,3,3,3,3,3,3]

# Splits the total list into 11 equal parts each part with 3 elements
Output = [totalList[x - y: x] for x, y in zip( 
          accumulate(length_to_split), length_to_split)] 

# Write the data from the totalList to csv file
with open('Averageracespeedgrandprix.csv', 'w', ) as myfile:
    wr = csv.writer(myfile)
    for word in Output:
        wr.writerow(word)

    

        


        
