CHARACTERSOFDAY = 2


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
  return day[:CHARACTERSOFDAY], convertToRange(day[CHARACTERSOFDAY:])
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

personal = ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']

dicti={}
for p in personal: 
  name, schedule = separateNameAndSchedule(p)
  print("llega", name)
  schedule = schedule.split(",")
  if (len(dicti.keys() )==0): 
    fillDict(name,schedule)
  else: 
    checkCrosses(name, schedule)
  
  
print(dicti)