#Basic File operations (write/append/read)

file1 = open("abc.txt",'w')                          #opens/creates a file in write mode
text = "Hey, what's up!!"
file1.write(text)                                    #writing above text to file abc.txt
file1.close()                                        #closing the file

appendFile = open("abc.txt", 'a')                   #opens a file in append mode
text1 = "\nHow is everything. \nGood."
appendFile.write(text1)                             #appends the above text to the end of file content
appendFile.close()                                  #closing the file

readFile = open("abc.txt", 'r').read()              #opens a file in read mode
readFileLines = open("abc.txt", 'r').readlines()    #opens a file in read mode, but it returns array of string with each line being a string
print(readFile)                                     #print output of file in read mode
print(readFileLines)                                #print output of file with readline


