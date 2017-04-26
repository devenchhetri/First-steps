#Simple Class for basic arithmetic operations

class Cal:                  #defining class Cal

    def addition(x,y):      #defining function for addition
        add = x + y
        print(add)

    def minus(x,y):         #defining function for subtraction
        sub = x - y
        print(sub)

    def divide(x,y):        #defining function for division
        div = x/y
        print(div)

    def multi(x,y):         #defining function for multiplication
        mul = x * y
        print(mul)

Cal.addition(3,2)           #calling function addition, with class name directly, similarly below for other functions
Cal.minus(3,2)
Cal.divide(3,2)
Cal.multi(3,2)



