def convertToRange(stringRange):
  stringList = stringRange.split("-")
  numericalRange = tuple(map(lambda x: convertStringDateToDecimal(x), stringList))
  return numericalRange

def convertStringDateToDecimal(string): 
  h,m = string.split(":")
  return float(int(h)+int(m)/60)

def getKeys(hours):
  hours = hours.split("=")
  name = hours[0]
  hours=hours[1]
  print("name", name)
  for h in hours.split(","):
    day = h[:2]
    k = convertToRange(h[2:])
    if day not in dicti.keys(): 
      dicti[day] = {}      
      if k not in dicti[day].keys():
        dicti[day][k] = [name]
      else: 
        print("aca name con ", dicti[day][k])
    else: 
      if k not in dicti[day].keys():
        dicti[day][k] = [name]
      else: 
        for al in dicti[day][k]: 
          print(f"encuentra {al} con {name}")
        dicti[day][k] = dicti[day][k] +[name]
        

personal = ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']

dicti={}
fdict={}
for p in personal: 
  a = p.split("=")
  b = getKeys(p)


print(dicti)