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
          fillDict(name, schedule)
      else: 
        if time not in dicti[dayName].keys():
          dicti[dayName][time] = [name]
        else: 
          for al in dicti[dayName][time]: 
            print(f"esta {al} con {name}")
            dicti[dayName][time] = list(set(dicti[dayName][time] +[name]))



file1 = open('myfile.txt', 'r')
lines = file1.readlines()

dicti={}
for p in lines: 
  name, schedule = separateNameAndSchedule(p)
  print("llega", name)
  schedule = schedule.split(",")
  if (len(dicti.keys() )==0): 
    fillDict(name,schedule)
  else: 
    checkCrosses(name, schedule)
  
  
print(dicti)