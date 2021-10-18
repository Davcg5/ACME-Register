import unittest

from RegisterTable import RegisterTable
from Exceptions import WrongSeparatorNameSchedule, WrongSeparatorRangeHours, NotExistingDay

class TestConversion(unittest.TestCase):
    def testConversionToRange(self):
        """
        Test that it can generate a valid range
        """
        registerTable = RegisterTable()
        data = (11.0, 12.5)
        result = registerTable.convertToRange(data)
        self.assertEqual(result, [11.0,11.1,11.2,11.3,11.4,11.5,11.6,11.7,11.8,11.9,12.0,12.1,12.2,12.3,12.4])
    def testConversionStringToDecimal(self):
        """
        Test that it can convert date string to decimal
        """
        registerTable = RegisterTable()
        data = "10:00"
        result = registerTable.convertStringDateToDecimal(data)
        self.assertEqual(result, 10.0)
    def testConversionToTuple(self): 
        """
        Test that it can convert a string of hours to a tuple
        """
        registerTable = RegisterTable()
        data = ["10:00", "12:00"]
        result = registerTable.convertToTuple(data)
        self.assertEqual(result, (10.0, 12.0))



class TestSeparation(unittest.TestCase):
    def testSeparationNameSchedule(self):
        """
        Test that it can separate Name and Schedule correctly
        """
        registerTable = RegisterTable()
        data = "RENE=MO10:00-12:00"
        resultName,resultSchedule  = registerTable.separateNameAndSchedule(data)
        self.assertEqual(resultName, "RENE" )
        self.assertEqual(resultSchedule, "MO10:00-12:00" )
    def testSeparationNameScheduleFail(self):
        """
        Test that the exception for the wrong separator is raised
        """
        registerTable = RegisterTable()
        data = "RENE-MO10:00-12:00"
        with self.assertRaises(WrongSeparatorNameSchedule):
            resultName,resultSchedule  = registerTable.separateNameAndSchedule(data)
    def testSeparationDayNameTimeFail(self):
        """
        Test that the exception for the wrong separator is raised
        """
        registerTable = RegisterTable()
        data = "MO10:00_12:00"
        with self.assertRaises(WrongSeparatorRangeHours):
            resultDayName,resultTime  = registerTable.separateDayNameAndTime(data)

    def testSeparationDayNameTime(self):
        """
        Test that the exception for the wrong separator is raised
        """
        registerTable = RegisterTable()
        data = "MO10:00-12:00"
        print("testing this one")

        resultDayName,resultTime  = registerTable.separateDayNameAndTime(data)
        self.assertEqual(resultDayName, "MO" )
        self.assertEqual(resultTime, (10.0, 12.00) )

class TestDaysOfWeek(unittest.TestCase): 

    def testIncorrectNameOfDay(self):
        """
        Test that the exception for the wrong name of a day is raised
        """
        registerTable = RegisterTable()
        data = "MON10:00-12:00"
        with self.assertRaises(NotExistingDay):
            resultDayName,resultTime  = registerTable.separateDayNameAndTime(data)


if __name__ == '__main__':
    unittest.main()