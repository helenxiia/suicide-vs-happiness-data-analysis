#Created by Helen Xia
#File I/O Assignment 2019 (Data Structure #2)
#Ms. Quesnelle ICS4U

import csv
import math

def averageSuicide(suicide):
    newList = []
    for i in range (0,len(suicide)):
        count = len(suicide[i][1])
        total = 0
        for k in range (0, len(suicide[i][1])):
             total += suicide[i][1][k]
        average = total / count
        newList.append([suicide[i][0], average])
    return newList
        

def createRatio(happy,suicide,orginal):
    adict = {}
    for i in range (0, len(suicide)):
        for k in range (0,len(happy)):
            if suicide[i][0] == happy[k][0]:
                ratio = suicide[i][1] / (10 - happy[k][1])
                adict[ratio] = []
                adict[ratio].append([happy[k][0],happy[k][1],orginal[i][1]])
    return adict

def createRange(ratioDict):
    final = {}
    final["<1"] = []
    final[">1 & <2"] = []
    final[">2 & <3"] = []
    final["<3"] = []
    for item in ratioDict:
        if item < 1:
            final["<1"].append([item,ratioDict[item][0]])
        elif item > 1 and item < 2:
            final[">1 & <2"].append([item,ratioDict[item][0]])
        elif item >2 and item <3:
            final[">2 & <3"].append([item,ratioDict[item][0]])
        else:
            final["<3"].append([item,ratioDict[item][0]])
    return final

                
def combineSuicide (countrySuicideUncombined):
    diction = {}
    alist = []
    for i in range (0, len(countrySuicideUncombined)-1): 
        if countrySuicideUncombined[i][0] not in diction:
            diction[countrySuicideUncombined[i][0]]= []
        diction[countrySuicideUncombined[i][0]].append(countrySuicideUncombined[i][1])
    for item in diction:
        alist.append([item,diction[item]])
    return(alist)

    

countryHappy = []
countrySuicideUncombined = []

with open ("HappinessReport2016.csv", encoding = "utf-8", errors = "replace") as fileIn:

    reader = csv.DictReader(fileIn)
    for line in reader:
        temp = []
        temp.append(line["Country"])
        temp.append(float(line["Happiness Score"]))
        countryHappy.append(temp)
        
    

with open ("SucideRatesAllYears.csv", encoding = "utf-8", errors = "replace") as fileIn: 

    reader = csv.DictReader(fileIn)
    for line in reader:
        if line["year"] == "2016":
            
            temp = []
            temp.append(line["\ufeffcountry"])
            temp.append(float(line["suicides/100k pop"]))
            countrySuicideUncombined.append(temp)
    
#Main

countrySuicide = combineSuicide(countrySuicideUncombined)
averageSuicide = averageSuicide(countrySuicide)
ratioDict = createRatio(countryHappy, averageSuicide, countrySuicide)
final = createRange(ratioDict)
print(final)

