DAYSOFWEEK= ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]


def convertToRange(stringRange):
  stringList = stringRange.split("-")
  numericalRange = tuple(map(lambda x: convertStringDateToDecimal(x), stringList))
  return numericalRange
def fillDict(name, schedule):
  for day in schedule: 
    
    dayName, time = separateDayNameAndTime(day)
    dicti[dayName] = {}
    dicti[dayName][time] = [name]

def convertStringDateToDecimal(string): 
  h,m = string.split(":")
  return float(int(h)+int(m)/60)
def separateDayNameAndTime(day): 
  for weekDay in DAYSOFWEEK: 
    if weekDay in day: 
      time= day.split(weekDay)[-1]
      dayName = weekDay      
      return dayName, convertToRange(time)

def separateNameAndSchedule(chain):
  name, schedule = chain.split("=")
  return name, schedule 

def checkCrosses(name, schedule):
  for day in schedule: 
      dayName, time = separateDayNameAndTime(day)
      if dayName not in dicti.keys(): 
            checkOverlappings(dayName, time, name)
            fillDict(name, schedule)
      else: 
        if time not in dicti[dayName].keys():
            dicti[dayName][time] = [name]
        else: 
          for al in dicti[dayName][time]: 
            fillTable(al, name)

            dicti[dayName][time] = list(set(dicti[dayName][time] +[name]))

def areOverlapping(rangeUser1, rangeUser2): 
    setRange1 = set(rangeUser1)
    return len(setRange1.intersection(rangeUser2))>0

def checkOverlappings(dayName, timeN, nameN): 

    for time in dicti[dayName].keys():
        if areOverlapping(time, timeN): 
            for al in dicti[dayName][time]:     
                fillTable(al, name)
        else: 
            continue

def fillTable(prevName, name): 
    key = prevName+"-"+name
    if key not in tableDict.keys(): 
        tableDict[key] = 1
    else: 
        tableDict[key] =tableDict[key]+1



file1 = open('myfile.txt', 'r')
lines = file1.readlines()

dicti={}
tableDict = {}
for p in lines: 
  name, schedule = separateNameAndSchedule(p)
  schedule = schedule.split(",")
  if (len(dicti.keys() )==0): 
    fillDict(name,schedule)
  else: 
    checkCrosses(name, schedule)
  
  
print(tableDict)