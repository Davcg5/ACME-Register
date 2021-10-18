from Exceptions import NotExistingDay, WrongSeparatorNameSchedule, WrongSeparatorRangeHours
from constants import DAYSOFWEEK, NAMESHIFTSSEPARATOR, RANGEHOURSSEPARATOR
class RegisterTable():
    def __init__(self): 
        self.registerDict = {}
        self.summaryDict = {}
        self.initializeRegisterDict()
        self.DAYSOFWEEK= DAYSOFWEEK
        self.NAMESHIFTSSEPARATOR = NAMESHIFTSSEPARATOR
        self.RANGEHOURSSEPARATOR = RANGEHOURSSEPARATOR

    def convertToTuple(self, hours):
        """
        Converts a list of two strings into a tuple to be 
        a key in the intern dictionary of a day

        In: hours: list of string each string is a time
        Out: A numerical range especifically a tuple that represents 
        a time window. 
        """

        numericalRange = tuple(map(lambda x: self.convertStringHourToDecimal(x), hours))
   
        return numericalRange

    def initializeRegisterDict(self): 
        """
        Initialize the dictionary of registers with the days 
        of the week one day represents a key and its value is 
        another dictionary
        """
        for day in DAYSOFWEEK: 
            self.registerDict[day] = {}
 

    def fillDict(self, dayName, timeWindow, name): 
        """
        Fill the intern dictionaries of the corresponding name. 
        time window are keys of the intern dictionaries
        in case that the incoming window time exists, in that key 
        the incoming name will be added to the existing names in that window time, otherwise
        the key is created and as value, the incoming name is placed

        In: dayName: Name of the day, the key in the registersDictionary
        timeWindow: Intern key of a day 
        name: name of the employee
        """
    
        if timeWindow not in self.registerDict[dayName].keys():
            self.registerDict[dayName][timeWindow] = [name]
        else: 
            self.registerDict[dayName][timeWindow] = list(set(self.registerDict[dayName][timeWindow] +[name]))


    def convertStringHourToDecimal(self,stringHour):  
        """
        Convert a date in string like ("10:00") 
        to a float number (10.0) 
        In: 
        stringHour: a string representing an hour
        Out: 
        a float number representing an hour
        """
        h,m = stringHour.split(":")

        try: 
            h = int(h) 
            m = int(m)
        except Exception: 
            return Exception
        else: 
            return float(h+(m/60))

    def separateDayNameAndTime(self,shift): 
        """
        Separate the name of the day from the hours of that day

        In: 
        shift: a string with the day and hours worked that day

        Out: 
        dayName: a string representing the name of the day 
        timeWindow: a tuple representing the time window worked
        Or: 
        An exception caused by the difference between the days of the constant DAYSOFWEEK
        and the day of the shift
        An exception caused by using a different separator from RANGEHOURS for the hours. 
        """

        for weekDay in self.DAYSOFWEEK: 
            if weekDay in shift: 
                timeWindow= shift.split(weekDay)[-1]
                dayName = weekDay
                if self.validateTime(timeWindow) == True: 
                    try: 
                        hourBegin, hourFinish = timeWindow.split(self.RANGEHOURSSEPARATOR)
                    except Exception as e:
                        raise WrongSeparatorRangeHours                   
                    else: 
                        timeWindow = self.convertToTuple([hourBegin, hourFinish])

                        return dayName, timeWindow
                else: 
                    print("po acá")
                    raise  NotExistingDay
            else: 
                continue

    def validateTime(self, shift):
        """
        Validate that a time contains only numbers
        In:
        A string representing a shift
        Out: 
        A boolean representing whether there are no letters in the string
        """
        if shift.isupper() or shift.islower() : 
            return False
        else: 
            return True

    def separateNameAndShifts(self, register):
        """
        Separate the name from the shifts worked. 
        In: 
        register: A string containing a row of the file, a register. 
        Out: 
        name: a string with the name of the employee. 
        shifts: a string with all the shifts when the employee worked. 
        """
        try: 
            name, shifts = register.split(self.NAMESHIFTSSEPARATOR)
        except Exception as error: 
            raise WrongSeparatorNameSchedule
        else: 
            return name, shifts 

    
    def checkPressence(self, name, shifts):
        """
        Check whether one employee was at the same time as another employee

        In: 
        name: name of the employee
        shifts: a string with the shifts worked of the employee
        """
        shifts = shifts.split(",")
        for shift in shifts:
            try:  
                dayName, timeWindow = self.separateDayNameAndTime(shift)
            except Exception as error:
                exceptionName = error.__class__.__name__
                print(exceptionName)
                if exceptionName =="NotExistingDay": 
                    print(f"Avoiding shifts:{shifts} for name: {name} because of: {error}")
                elif exceptionName == "WrongSeparatorRangeHours":
                    print(f"Avoiding shift: {shift} for {name}, because of: {error}")
                else: 
                    print(f"avoiding because of: {error}")
            else: 
                rangeUser1 = self.convertToRange(timeWindow)

                for existingTimeWindow in self.registerDict[dayName].keys():
                    rangeUser2 = self.convertToRange(existingTimeWindow)
                    setRange1 = set(rangeUser1)
                    if len(setRange1.intersection(rangeUser2))>0: 
                        for existingName in self.registerDict[dayName][existingTimeWindow]: 
                            self.fillTable(existingName, name)
                    else: 
                        continue
                self.fillDict(dayName, timeWindow, name)    
                    


    def convertToRange(self, tupleRange): 
        """
        Convert a tuple to a range 
        In: 
        tupleRange: a tuple containing the limits of the range
        Out: 
        A list of the numbers of the range 
        """
        begin = int(round(tupleRange[0]*10,0))
        end = int(round(tupleRange[1]*10,0))
        listRange = [x / 10.0 for x in range(begin, end, 1)]
        return listRange

 

    def fillTable(self, prevName, name): 
        """
        Fill the summary dict with the pairs of employees
        In: 
        prevName: string with the name that already exists in the registerDictionary
        name: string with the name of the incoming employee
        """
        key = prevName+"-"+name
        if key not in self.summaryDict.keys(): 
            self.summaryDict[key] = 1
        else: 
            self.summaryDict[key] =self.summaryDict[key]+1

    def retrieveTable(self): 
        """
        Print the content of the summaryDict 
        """
        for key, value in self.summaryDict.items(): 
            print( f"{key}: {value}")