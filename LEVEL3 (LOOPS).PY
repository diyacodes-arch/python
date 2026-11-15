#PRINT NUMS FROM 1 TO 10 USING FOR LOOP

for i in range(1,11,1):
    print(i)
    

#PRINT NUMS FROM 10 TO 1 USING FOR LOOP
for i in range(10,0,-1):
    print(i)
      
i=1
while i<=20:
    print(i)
    i +=2   

#PRINT THE TABLE OF A NUM ENTERED BY THE USER
num=int(input("enter a number"))
for i in range(1,11,1):
      print(num*i)

#FIND THE SUM OF nums from 1 to 10
i=(1,2,3,4,5,6,7,8,9,10)
sum=0
for j in i:
    sum=sum+j
    print(sum)  

#PRINT EACH CHARACTER OF A WORD USING A LOOP
word=("diya")
for i in word:
    print(i)

#COUNT HOW MANY VOWELS ARE PRESENT IN A WORD
word=input("enter a word :")
count=0
vowel="aeiou"
for j in word:
    if(j in vowel):
        count +=1
        print(j)