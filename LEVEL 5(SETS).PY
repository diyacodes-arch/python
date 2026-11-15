set={"apple","mango","papaya","banana","grapes"}
print(set)

#add a new item to a set
set={"apple","mango","papaya","banana","grapes"}
set.add("orange")
print(set)

#remove an item from a set
set={"apple","mango","papaya","banana","grapes"}
set.remove("mango")
print(set)

#create 2 sets and find their union
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
print(set1.union(set2))

#create 2 sets and find their intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
print(set1.intersection(set2))

#given a list with duplicate values,convert it into a set to remove duplicates
list=[1,2,2,3,4,5,5,6,4,3,7,8]
print(list)
set={1,2,2,3,4,5,5,6,4,3,7,8}
print(set)
