#CREATE A LIST OF 5 FRUITS AND PRINT THE LIST
list=["apple","mango","banana","papaya","kiwi"]
print(list)

#CREATE A LIST OF 5 NUMS AND PRINT THE FIRAST AND LAST ELEMENT
num=[1,2,3,4,5]
print(num[0])
print(num[4])

# CREATE A LIST OF 5 NUMBERS AND PRINT THE FIRST AND LAST ELEMENT
list=[1,2,3,4,5]
list.append(6)
print(list)

# REMOVE AN ITEM TO A LIST USING REMOVE()
list=[1,2,3,4,5,6]
list.remove(3)
print(list)

#FIND THE LENGTH OF A LIST USING LEN()
i=[1,2,3,4,5,6,7,8,9]
print(len(i))

# PRINT EVERY ELEMENT OF A LIST USING FOR LOOP
num=[10,20,30,40,50,60,70,80,90,100]
for i in num:
    print(i)
  
#FIND THE LARGEST NUM IN THE LIST
num=[10,25,36,43,52,6]
x=52
for i in num:
    if (i==x):
         print("the largest number is :",x)

# FIND THE SUM OF ALL NUMS IN THE LIST
list=[10,25,36,43,52,6]
sum=0
for i in list:
    sum =sum+i
    print(sum)

