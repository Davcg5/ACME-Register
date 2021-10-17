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
            self.registerDict[dayName] = {}
            self.registerDict[dayName][time] = [name]

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
                return round(float(int(h)+int(m)/60), 2)

 

    def separateDayNameAndTime(self,day): 
        for weekDay in self.DAYSOFWEEK: 
            if weekDay in day: 
                time= day.split(weekDay)[-1]
                dayName = weekDay
                try: 
                    time =self.convertToTuple(time)
                except Exception as e: 
                    print("aquí?",e)
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

                if dayName not in self.registerDict.keys(): 
                    self.fillDict(name, schedule)
                else: 
                    if time not in self.registerDict[dayName].keys():
                        self.checkOverlappings(dayName, time, name)
                        self.registerDict[dayName][time] = [name]
                    else: 
                        for al in self.registerDict[dayName][time]: 
                            self.fillTable(al, name)

                            self.registerDict[dayName][time] = list(set(self.registerDict[dayName][time] +[name]))

    def areOverlapping(self, rangeUser1:tuple, rangeUser2:tuple): 
        print("1", rangeUser1)
        rangeUser1 = self.convertToRange(rangeUser1)
        rangeUser2 = self.convertToRange(rangeUser2)
        setRange1 = set(rangeUser1)
        print("is it ", len(setRange1.intersection(rangeUser2)))
        return len(setRange1.intersection(rangeUser2))>0

    def convertToRange(self, tupleRange): 
        
        begin = int(round(tupleRange[0]*10,0))
        end = int(round(tupleRange[1]*10,0))
        listRange = [x / 10.0 for x in range(begin, end+1, 1)]
        return listRange

    def checkOverlappings(self, dayName, timeN, nameN): 
        print("acá")
        for time in self.registerDict[dayName].keys():
            if self.areOverlapping(time, timeN): 
                for al in self.registerDict[dayName][time]:     
                    self.fillTable(al, nameN)
            else: 
                continue

    def fillTable(self, prevName, name): 
        key = prevName+"-"+name
        if key not in self.summaryDict.keys(): 
            self.summaryDict[key] = 1
        else: 
            self.summaryDict[key] =self.summaryDict[key]+1

    def retrieveTable(self): 
        for key, value in self.summaryDict.items(): 
            print( f"{key}: {value}")