
from RegisterTable import RegisterTable
from File import File
if __name__ == "__main__":

    a = input("Ingrese la ruta relativa del archivo de texto plano ")

    f = File(a)
    lines = f.registers
    registerTable = RegisterTable()

    for register in lines: 
        try: 
            name, schedule = registerTable.separateNameAndShifts(register)
        except Exception as error: 
            print(f"Avoiding register {register} because of: {error}" )
        else:     
            registerTable.checkPressence(name, schedule)

    print(registerTable.registerDict)
    registerTable.retrieveTable()
