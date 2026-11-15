#create a dictionary containing a person's name,age ,city.print it.
dict={
    "name":"diya",
    "age": 21,
    "city": "mohali"
    }
for key ,value in dict.items():
    print(key ,":" ,value)

#print only the person's name from dict
dict={
    "name":"diya",
    "age": 21,
    "city": "mohali"
    }
print(dict["name"])

#add a new key called email
me={
    "name":"diya",
    "age":20,
    "city":"mohali",
}
me["email"]="joshidiya656@gmail.com"
for keys,values in me.items():
    print(keys,":",values)

#delete a key
me={
    "name":"diya",
    "age":20,
    "city":"mohali",
    "email":"joshidiya656@gmail.com"
}
del me["email"]
for keys,values in me.items():
    print(keys,":",values)

a=int("A",11)
print(a)

#loop to print keys
dict={
    "name":"diya",
    "age": 21,
    "city": "mohali"
    }
for key  in dict.keys():
    print(key)


#loop to print values
dict={
    "name":"diya",
    "age": 21,
    "city": "mohali"
    }
for values  in dict.values():
    print(values)

#create a dict of 3 students and their marks.print the marks of one student
marks={
    "riya":43,
    "diya":54,
    "aarav" :67
}
print("marks of diya :",marks['diya'])