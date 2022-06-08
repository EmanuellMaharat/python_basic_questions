# "coca cola"
for i in range(1,100):
     if i % 5 == 0 and i % 3 == 0:
        print("coca cola")
     elif i % 3 == 0:
         print("coca")
     elif i % 5 == 0:
        print("cola")
     else:
        print(i)
#
#Fibonacci
a,b = 0, 1
for i in range (1,10):
    print (a)
    a , b = b , a+ b

#list
mylist = [1,2,3,4,5,6,7,8,9,10]
# give squared num in my list
square = [num*num for num in mylist]
print (square)
