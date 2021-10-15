class RegisterTable():
    def __init__(self): 
        self.registerDict = {}
        self.summaryDict = {}
        self.DAYSOFWEEK= ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

    def convertToRange(self, stringRange):
        stringList = stringRange.split("-")
        numericalRange = tuple(map(lambda x: self.convertStringDateToDecimal(x), stringList))
        return numericalRange

    def fillDict(self, name, schedule):
        for day in schedule: 
            
            dayName, time = self.separateDayNameAndTime(day)
            self.registerDict[dayName] = {}
            self.registerDict[dayName][time] = [name]

    def convertStringDateToDecimal(self,string): 
        h,m = string.split(":")
        return float(int(h)+int(m)/60)
    def separateDayNameAndTime(self,day): 
        for weekDay in self.DAYSOFWEEK: 
            if weekDay in day: 
                time= day.split(weekDay)[-1]
                dayName = weekDay      
                return dayName, self.convertToRange(time)

    def separateNameAndSchedule(self, chain):
        name, schedule = chain.split("=")
        return name, schedule 

    def checkCrosses(self, name, schedule):
        for day in schedule: 
            dayName, time = self.separateDayNameAndTime(day)
            if dayName not in self.registerDict.keys(): 
                self.checkOverlappings(dayName, time, name)
                self.fillDict(name, schedule)
            else: 
                if time not in self.registerDict[dayName].keys():
                    self.registerDict[dayName][time] = [name]
                else: 
                    for al in self.registerDict[dayName][time]: 
                        self.fillTable(al, name)

                        self.registerDict[dayName][time] = list(set(self.registerDict[dayName][time] +[name]))

    def areOverlapping(self, rangeUser1, rangeUser2): 
        setRange1 = set(rangeUser1)
        return len(setRange1.intersection(rangeUser2))>0

    def checkOverlappings(self, dayName, timeN, nameN): 

        for time in self.registerDict[dayName].keys():
            if self.areOverlapping(time, timeN): 
                for al in self.registerDict[dayName][time]:     
                    fillTable(al, name)
            else: 
                continue

    def fillTable(self, prevName, name): 
        key = prevName+"-"+name
        if key not in self.summaryDict.keys(): 
            self.summaryDict[key] = 1
        else: 
            self.summaryDict[key] =self.summaryDict[key]+1



file1 = open('myfile.txt', 'r')
lines = file1.readlines()

registerTable = RegisterTable()
for p in lines: 
  name, schedule = registerTable.separateNameAndSchedule(p)
  schedule = schedule.split(",")
  if (len(registerTable.registerDict.keys() )==0): 
    registerTable.fillDict(name, schedule)
  else: 
    registerTable.checkCrosses(name, schedule)
  
  
print(registerTable.summaryDict)