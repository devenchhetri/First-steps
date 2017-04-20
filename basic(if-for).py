print('abc'+str(5))                 #for printing output('abc' is a string and 5 is converted to string with str() function, + is concatenation operator)

print(2+6)                          #printing sum of 2+6

print('abc '+str(9+1)+' xyz')       #printing 2 strings and sum which is converted to string

#single line comment                #writing single line comment

                                    #witing multi line comment within ''' '''
'''
multi
line
comment
'''
                                    #printing multi line output
print('''
multi line print
==============
|            |
|            |
|   Center   |
|            |
|            |
==============

''')


cond = 1                            #displaying while loop
while cond <= 10:
    print(cond)
    cond +=1
print("\n")                         #for line break

numList = [2,4,6,8,0]               #displaying for loop
for eachNo in numList:
    print(eachNo)
print("\n")

x = 1
for i in range(1,11):
    x = x*i
print(x, "\n")


x=3                                 #displaying if-else conditionals
y=2
z=1

if x<y:
    print('x<y')
elif x<z:
    print('x<z')
else:
    print('x is greater')


