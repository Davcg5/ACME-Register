from Exceptions import EmptyFileException, MinLenException, IncorrectFormat
class File(): 
    def __init__(self, fileName): 

        if self.validateExtension(fileName): 
            self.registers = open(fileName)
            self.registers = self.registers.readlines()
            self.cleanFile()
            self.checkNumberOfLines()
        else: 
            raise IncorrectFormat()
    def cleanFile(self): 
        self.registers = list(line for line in (l.strip() for l in self.registers) if line)
    
    def validateExtension(self, fileName): 
        extension = fileName.split(".")[-1]
        if extension == "txt": 
            return True
        else: 
            return False
        

    def checkNumberOfLines(self):
        
        if len(self.registers) ==0:
            raise  EmptyFileException
        elif len(self.registers) <3 : 
            raise MinLenException
  