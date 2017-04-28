#playing with data in csv file

#must have 'sample_csv.csv' file in the same folder with this file before we run this file

import csv                                                  #importing csv module

with open("sample_csv.csv") as csvFile:                     #opening csv file named sample_csv.csv
    readCSV = csv.reader(csvFile, delimiter=',')            #reading the content of csv file with specified delimiter

    first = []                                              #declaring empty list which will be holding first names
    last = []                                               #declaring empty list which will be holding last names

    for row in readCSV:
        fir = row[1]                                        #assigning first name from each row as fir
        las = row[2]                                        #assigning last name from each row as las

        first.append(fir)                                   #appending first names (fir) to the first list
        last.append(las)                                    #appending last names (las) to the last list

    print(first)
    print(last)

    ask_first = input("Whose last name do you want? ")      #taking user input for first name
    if ask_first in first:
        ans = first.index(ask_first)
        print(last[ans])                                    #displaying the last name for the first name input by user, if it exists
    else:
        print("Wrong name")                                 #displaying 'Wrong name' if the first name does not exist
