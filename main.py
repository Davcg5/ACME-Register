
from RegisterTable import RegisterTable
if __name__ == "__main__":

    a = input("Ingrese el nombre del archivo con su ruta ")

    file1 = open(a, 'r')
    lines = file1.readlines()
    print(len(lines))

    registerTable = RegisterTable()
    for p in lines: 
        name, schedule = registerTable.separateNameAndSchedule(p)
        schedule = schedule.split(",")
        if (len(registerTable.registerDict.keys() )==0): 
            registerTable.fillDict(name, schedule)
        else: 
            registerTable.checkCrosses(name, schedule)
        
    print(registerTable.registerDict)
    print(registerTable.summaryDict)

