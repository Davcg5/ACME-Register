
from RegisterTable import RegisterTable
from File import File
if __name__ == "__main__":

    a = input("Ingrese la ruta relativa del archivo de texto plano ")

    f = File(a)
    lines = f.registers
    registerTable = RegisterTable()

    for i, p in enumerate (lines): 
        try: 
            name, schedule = registerTable.separateNameAndSchedule(p)
        except Exception as error: 
            print(error)
        else:     
            schedule = schedule.split(",")
            if (len(registerTable.registerDict.keys() )==0): 
                registerTable.fillDict(name, schedule)
            else: 
                registerTable.checkCrosses(name, schedule)

    print(registerTable.registerDict)
    registerTable.retrieveTable()

