from Exceptions import EmptyFileException, MinLenException, IncorrectFormat
class File(): 
    def __init__(self, fileName): 
        """
        Initializa variables and validate the file
        """
        if self.validateExtension(fileName): 
            self.registers = open(fileName)
            self.registers = self.registers.readlines()
            self.cleanFile()
            self.checkNumberOfLines()
        else: 
            raise IncorrectFormat
    def cleanFile(self): 
        """
        Delete empty lines from file
        """
        self.registers = list(line for line in (l.strip() for l in self.registers) if line)
    
    def validateExtension(self, fileName): 
        """
        Validate the extension of the file
        """
        extension = fileName.split(".")[-1]
        if extension == "txt": 
            return True
        else: 
            return False
        

    def checkNumberOfLines(self):
        """
        Validate the number of lines of the File
        """
        if len(self.registers) ==0:
            raise  EmptyFileException
        elif len(self.registers) <5 : 
            raise MinLenException
  