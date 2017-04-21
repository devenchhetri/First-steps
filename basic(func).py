def window(width, height, breadth=4, color='b'):    #defining a function with one argument having a default value
    print(width, height, breadth, color)

window(3,5,color='w')                               #calling above function without passing a value to breadth argument


def simple_add(num1, num2):                         #defining a function which does simple addition
    ans = num1 + num2
    print('\nnum1 is', num1)
    print('num2 is', num2)
    print('sum is', ans)
    print()

simple_add(num2=3,num1=5)                           #calling the above function with different order of arguments from that in function defintion


x=7

def eg():                                           #function showing a way to manipulate a global variable x, declared above
    globx = x
    globx += 5
    return globx

x=eg()                                              #calling above function by directly assigning to gobal vaiable x
print(x)
