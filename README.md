# ACME-Register
## Problem

The company ACME offer their employees the flexibility to work the hours they want. But due to some external circunstances they need to know what employees have been at the office within the same time frame. 

### Input 
The name of an employee and the schedule they worked, indicating the time and hours. 
This should be a .txt file with at least 5 sets of data, for example: 

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

### Expected output

ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

## Overview of the solution

First, a validation is performed over the file. The extension and number of lines are checked. 
Then, each register is separated by name and the shifts the employee was at the office and for each one of these shifts, day and time window are separated in order to find a time window in common with another employee as long as it's the same day. 

## Architecture 

My solution has a file called main.py, which is the file to be run, is the part of the solution thath when executed, interacts with the user. Here, the instances of the classes for the file and for the register table are created. 

Class File acts as a validator for the .txt file that is being read.
Class RegisterTable contains all the methods to separate the registers and count the times where two employees coincided at the office. 
There is a file called constants where the symbols between name and shifts and between the hours of a time window are set, the name for the days of the week are set as well. Acts as a configuration file where is easiest to change the name for the days of the week or the separators of the registers. 
There is a file called Exceptions where custom Exceptions were placed, with the purpose of showing a representative message to the user in case of an error in the registers. 
The file test.py contains unit tests applied to some functions of the class RegisterTable. 

## Approach and Methodology 

The main idea was to count the times an employee coincides with another as the register is read. This means that when the registers of an employee are read, the times this employee coincided with the previous employees are already being stored. 

Dictionaries were used for this purpose where the days will be the keys and as values there will be several dictionaries where the keys will be the time windows and the values will be lists with the names of the employees who worked on that time window. Example for the day MO: 

{"MO" : {(9:00, 10:00): ["Rene"]}, 
            (12:00, 13:00), ["Rene", "Astrid"]}


There will be 7 keys and for each key as many subkeys as time windows found for that day and for that subkeys there will be as many elements in the list as employees who worked on that time window on that day. 

When two employees coincide at the office, a new key and value are stored in a different dictionary which summarizes the information. This key is formed by the name of the employees and the value is the number of times the employees coincided at the office. 

The criteria for determining whether two employees coincide at the office is based in ranges and if whether these ranges overlap each other. For that purpose each time window is converted to a range of decimal numbers, which means the time window 10:30-11:30 is converted to a range that goes from 10.5 to 11.5 in intervals of 0.1.

Finally, the dictionary where the information was summarized was printed. 


In order to get to the final solution, a sketch-like code was created where many approaches were considered, specifically, for the parts of how to store the data that is being read and then how to get the coincidences. When the idea of finding the coincidences of the incoming employee with the previous employees by the time the register of the incoming employee is read was found, it was clear that the name of the employee was not the key to consider in the dictionary. 

Once the structure of the dictionary of registers was clear, 
 the functionality was splitted into functions and a first solution was found. From that, the methods were separated by the object they represent and the classes for File and RegisterTable were created. 

In order to test the functions and to see representative error messages based on the problem, tests and custom exceptions were created. Many tests with different data were run as well. 

From that, several optimizations were applied in order to make the code as simple as possible and get rid of redundant code, obtaining as result, the solution presented here. 


## Instructions

1. Download the repository and unzip it. 
2. Paste the .txt file of registers to be tested in the folder of the solution, it can be next to the solution or in a subfolder. 
3. From a terminal, go to the directory where the solution and the .txt file are. 
4. (Optional) If you want to run the tests, run *pip install unittest* and then *python test.py*. 
5. In the terminal type *python main.py*. 
6. The program will ask for the path of the .txt file, if the file is next to the solution (my suggestion), write the name of the file like this: *myfile.txt* or if the file is in a subfolder, write the name of the subfolder followed by the name of the file like this: *name_of_subfolder/myfile.txt*
7. After entering the path of the .txt file, the summary will be shown. 

