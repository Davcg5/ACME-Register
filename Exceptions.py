class EmptyFileException(Exception):
    def __init__(self, message = "File must not be empty"):
        super().__init__(message)
        

class MinLenException(Exception):
    def __init__(self, message = "File must have at least 5 registers"):
        super().__init__(message)

class NotExistingDay(Exception):
    def __init__(self, message = "Day not found"):
        super().__init__(message)

class WrongSeparatorNameSchedule(Exception):
    def __init__(self, message = "Separator is not correct"):
        super().__init__(message)


class WrongSeparatorRangeHours(Exception):
    def __init__(self, message = "Separator is not correct for the range of hours"):
        super().__init__(message)

class IncorrectFormat(Exception):
    def __init__(self, message = "Wrong format"):
        super().__init__(message)