id = input("What's your name? ")                    #getting input from a user
print("Hi",id)

#Basics of statistics module
import statistics as s                              #importing statistics module

eg_list = [1,2,3,4,5,6,7,8,9,7,5,6,4,3,5,7,1,7]     #creating a list (array)

x1 = s.mean(eg_list)                                #x1 stores mean
x2 = s.median(eg_list)                              #x2 stores median
x3 = s.mode(eg_list)                                #x3 stores mode
x4 = s.stdev(eg_list)                               #x4 stores standard deviation
x5 = s.variance(eg_list)                            #x5 stores variance

print(x1,x2,x3,x4,x5)




