from Exceptions import NotExistingDay, WrongSeparatorNameSchedule, WrongSeparatorRangeHours

class RegisterTable():
    def __init__(self): 
        self.registerDict = {}
        self.summaryDict = {}
        self.DAYSOFWEEK= ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
        self.NAMESCHEDULESEPARATOR = "="
        self.RANGEHOURSSEPARATOR = "-"

    def convertToTuple(self, stringRange):
        stringList = stringRange.split(self.RANGEHOURSSEPARATOR)
        numericalRange = tuple(map(lambda x: self.convertStringDateToDecimal(x), stringList))
        return numericalRange

    def fillDict(self, name, schedule):

        for day in schedule:  
            dayName, time = self.separateDayNameAndTime(day)

            if dayName not in self.registerDict.keys(): 
                self.registerDict[dayName] = {}
                self.registerDict[dayName][time] = [name]

            else: 
                if time not in self.registerDict[dayName].keys():
                    self.registerDict[dayName][time] = [name]
                else: 
                    self.registerDict[dayName][time] = list(set(self.registerDict[dayName][time] +[name]))

    def convertStringDateToDecimal(self,string): 
       
        try: 
             h,m = string.split(":")
        except Exception as e: 
            raise WrongSeparatorRangeHours()
        else:
            try: 
                h = int(h) 
                m = int(m)
            except: 
                raise NotExistingDay()
            else: 
                return float(int(h)+int(m)/60)

 

    def separateDayNameAndTime(self,day): 
        for weekDay in self.DAYSOFWEEK: 
            if weekDay in day: 
                time= day.split(weekDay)[-1]
                dayName = weekDay
                try: 
                    time =self.convertToTuple(time)
                except Exception as e: 
                    continue
                else: 
                    return dayName, time
            else: 
                continue
        raise NotExistingDay()

    def separateNameAndSchedule(self, chain):
        try: 
            name, schedule = chain.split(self.NAMESCHEDULESEPARATOR)
        except Exception as error: 
            raise WrongSeparatorNameSchedule
        else: 
            return name, schedule 

    
    def checkCrosses(self, name, schedule):
        for day in schedule:
            try:  
                dayName, time = self.separateDayNameAndTime(day)
            except Exception as e:
                print(e) 
            else: 
                self.addOverlaps(dayName, time, name)     
        
        self.fillDict(name, schedule)

    def addOverlaps(self, dayName, timeN, nameN): 
        rangeUser1 = self.convertToRange(timeN)

        for time in self.registerDict[dayName].keys():
            print("time", time)
            rangeUser2 = self.convertToRange(time)
            setRange1 = set(rangeUser1)
            if len(setRange1.intersection(rangeUser2))>0: 
                print("overlaps")
                for al in self.registerDict[dayName][time]: 
                    self.fillTable(al, nameN)
            else: 
                continue
                

    def convertToRange(self, tupleRange): 
        
        begin = int(round(tupleRange[0]*10,0))
        end = int(round(tupleRange[1]*10,0))
        listRange = [x / 10.0 for x in range(begin, end, 1)]
        return listRange

 

    def fillTable(self, prevName, name): 
        key = prevName+"-"+name
        if key not in self.summaryDict.keys(): 
            self.summaryDict[key] = 1
        else: 
            self.summaryDict[key] =self.summaryDict[key]+1

    def retrieveTable(self): 
        for key, value in self.summaryDict.items(): 
            print( f"{key}: {value}")