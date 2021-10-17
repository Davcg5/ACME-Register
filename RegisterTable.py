from Exceptions import NotExistingDay, IsNotInt

class RegisterTable():
    def __init__(self): 
        self.registerDict = {}
        self.summaryDict = {}
        self.DAYSOFWEEK= ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
        self.NAMESCHEDULESEPARATOR = "="
        self.RANGEHOURSSEPARATOR = "-"

    def convertToRange(self, stringRange):
        stringList = stringRange.split(self.RANGEHOURSSEPARATOR)
        numericalRange = tuple(map(lambda x: self.convertStringDateToDecimal(x), stringList))
        return numericalRange

    def fillDict(self, name, schedule):
        for day in schedule:             
            dayName, time = self.separateDayNameAndTime(day)
            self.registerDict[dayName] = {}
            self.registerDict[dayName][time] = [name]

    def convertStringDateToDecimal(self,string): 
        h,m = string.split(":")
        try: 
            decimalHour = float(int(h)+int(m)/60)
        except Exception as e: 
            raise IsNotInt()
        else:     
            return 
 

    def separateDayNameAndTime(self,day): 
        print(day)
        for weekDay in self.DAYSOFWEEK: 
            if weekDay in day: 
                time= day.split(weekDay)[-1]
                dayName = weekDay
                try: 
                    self.convertToRange(time)
                except Exception as e: 
                    print(e)
                else: 
                    return dayName, time
            else: 
                continue

    def separateNameAndSchedule(self, chain):
        name, schedule = chain.split(self.NAMESCHEDULESEPARATOR)
        return name, schedule 

    def checkCrosses(self, name, schedule):
        for day in schedule:
            try:  
                dayName, time = self.separateDayNameAndTime(day)
            except Exception as e:
                print("mal separado", e) 
            else: 
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

    def areOverlapping(self, rangeUser1:tuple, rangeUser2:tuple): 
        
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

