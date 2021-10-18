class EmptyFileException(Exception):
    def __init__(self, message = "File must not be empty"):
        super().__init__(message)
        

class MinLenException(Exception):
    def __init__(self, message = "File must have at least 5 registers"):
        super().__init__(message)

class NotExistingDay(Exception):
    def __init__(self, message = "Day has not been found in the predefined days of week"):
        super().__init__(message)

class WrongSeparatorNameSchedule(Exception):
    def __init__(self, message = "Separator is not correct for the name and shifts"):
        super().__init__(message)


class WrongSeparatorRangeHours(Exception):
    def __init__(self, message = "Separator is not correct for the time window"):
        super().__init__(message)

class IncorrectFormat(Exception):
    def __init__(self, message = "Wrong format of file"):
        super().__init__(message)