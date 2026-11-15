# f=open("demo.txt","w")
# data=f.write("i want to improve my skill")
# print(data)

# f.close()  

# with open("demo.txt","r") as f:
#     data= f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("ai/ml engineer")

# with open("practice.txt","w") as f:
#     f.write("hi everyone\nwe are learning file i/o\nusing java\ni like programming in java")

# with open("practice.txt","r") as f:
#     data=f.read()

# new_data=data.replace("java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word) !=-1):
        print("found")
    else:
        print("not found")
