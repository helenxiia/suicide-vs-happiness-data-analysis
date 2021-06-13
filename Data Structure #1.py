import csv
import math

def merge(suicide, happy):
    final = {}
    for i in range (0, len(suicide)-1):
        for k in range (0,len(happy)-1):   
            if suicide[i][0] == happy[k][0]:
                final[suicide[i][0]] = []
                final[suicide[i][0]].append(happy[k][1])
                final[suicide[i][0]].append(suicide[i][1])
        
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
final = merge(countrySuicide, countryHappy)
print(final)
            

    

