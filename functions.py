def cal(a,b):
    sum=a+b
    print(sum)
    return sum
cal(2,3)
cal(12,3)

def cal(a,b):
    return a*b
multiply=cal(3,4)
print(multiply)

#WAF TO PRINT THE LEGTH OF A LIST.(LIST IS THE PARAMETER)
cal=[1,2,3,4,5,6,7,8,9]
def list(cal):
    print(len(cal))
list(cal)


#WAF TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE(LIST IS THE PARAMETER)
list=[3,5,8,8,2,7,0,53]
def cal(list):
    for item in list:
        print(item,end=" ")
    
cal(list)

#WAF TO FIND THE FACTORIAL OF N(N IS THE PARAMETER)
def fac(n):
    multiply=1
    i=1
    while i<=n:
        multiply *=i
        i +=1
    return multiply
n=5
print("factorial is:",fac(n))

#WAF TO CONVERT USD TO INR
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD =",inr_val,"INR")
converter(10)

