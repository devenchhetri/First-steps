#displaying basic python data structures(list, tuple)

#tuples cannot be modified once declared
x = 1, 2, 3, 4          #declaring a tuple
y = (1, 2, 3, 4)        #declaring a tuple in other way

#lists can be modified once declared. Its like array in C, Java
z = [1, 2, 3, 4]        #declaring a list

print(x[1])             #printing 2nd element of x
print(y[0])             #printing 1st element of y
print(z[1], z[2])       #printing 2nd and 3rd element of z

z.append(1)             #appending 1 to end of list z
z.insert(1,6)           #inserting 6 at 2nd position
print(z)

#z.remove(z[1])
#print(z)

print(z.count(1))       #printing count of 1's in list z
print(z.index(1))       #printing index(starting at 0) of first 1

print(z[1:3])           #printing slice from a list

z.sort()                #sorting a list
print(z)

p = ["Deven", "Naman", "Anurag"]  #list of string
p.sort()                          #sorting string
print(p)

q = [                             #declaring mutli-dimensional list
    [[1,2], [2,1]],
    [3,4],
    [5,6]
    ]
print(q[0][1][1])
print(q[2][1])
