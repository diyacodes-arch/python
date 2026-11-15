# write a function to print hello print.
def write():
    
    print("hello world")
write()  

# caf that takes a name as an argument and prints'hello,name'.
def fun(name):
    
    print("hello",name)
fun("diya")

# caf that takes 2 numbers and return their sum
def add(a,b):
    sum=a+b
    print(sum)
    return add

add(20,50)

# caf that takes a number and return its square
def num(a):
    square=a*a
    print(square)
    return num
num(5)

# caf that takes a number and tells whether it is even or odd
def num(b):
    if (b/2==0):
        print("even")
    else:
        print("odd")
    return num
num(79)

# caf that takes two numbers and return the largest number
def fun(a,b):

    if(a>b):
        print("a is the largest number")
    else:
        print("b is the largest number")
    return fun
fun(57530000,87578)

# caf that a list and returns its sum
list=[3,45,7,2,78,97]
def fun(list):
    sum=0
    for i in list:
        sum=sum+i
        print(sum)
    return fun
fun(list)

#caf that takes a number and return its multiplication table
def fun(h):
    for i in range(1,11,1):
        print(h,"*",i,"=",h*i)
    return fun
fun(5)