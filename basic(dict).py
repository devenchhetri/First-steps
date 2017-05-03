#An important data structure in Python is Dictionary. It has key-value pairs

egDict = {'Deven':27, 'Anurag':25, 1:23}                         #declaring a dictionary

print(egDict)                                                    #printing entire dictionary
print(egDict['Deven'])                                           #printing value for key 'Deven'

egDict['laks'] = 28                                              #adding an item in dictionary
print(egDict)

egDict['laks'] = 29                                              #changing value of a key by reassigning a value to key
print(egDict)

del egDict['laks']                                               #deleting an item from dictionary
print(egDict)

egDiction = {'nav':[22, 'mech'], 'dev':[27, 'cs'], 'anu':[25, 'fire']}  #showing that a value can be a list within a dictionary
print(egDiction)
print(egDiction['dev'][1])                                       #printing specific element from a list, which is a value of key 'dev'


#built-in functions
x = -2.3
print(abs(x))                                                    #abs() is for absolute value

y = [1,2,4,3,6,9,8,5,7]
print(max(y))                                                    #max() is for maximum value
print(min(y))                                                    #min() is for minimum value

#casting
print(str(x))                                                    #typecasting a variable(float) to string

z = '55'
print(float(z))                                                  #typecasting a variable(float) to string
