class EmptyFileException(Exception):
    def __init__(self, message = "File must not be empty"):
        super().__init__(message)
        

class MinLenException(Exception):
    def __init__(self, message = "File must have at least 5 registers"):
        super().__init__(message)

class NotExistingDay(Exception):
    def __init__(self, message = "Day not found"):
        super().__init__(message)


class IsNotInt(Exception):
    def __init__(self, message = "Is not int "):
        super().__init__(message)

class IncorrectFormat(Exception):
    def __init__(self, message = "Wrong format"):
        super().__init__(message)