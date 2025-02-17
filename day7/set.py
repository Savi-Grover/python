#example 1- create set
myset1={"apple","banana","cherries"}
print(myset1)  # output will come in any order

#example 2 - accessing items from set
for i in myset1:
    print(i)

#example 3 - to check if value in set or not
print("banana" in myset1) #true
print("orange" in myset1)  #false

#example 4 - add new element in set
# add function - add single item at a time
myset1.add("orange")
print(myset1)

# update function - can add multiple items at a time
myset1.update(["mango","grapes"])
print(myset1)

#example 5 - len/number of items in set
print(len(myset1))

#example 6 - remove item from set- remove, discard
myset1.remove("orange")
print(myset1)

#myset1.remove("xyz")  #try remove random value - Key error
#print(myset1)

myset1.discard("grapes")
print(myset1)

myset1.discard("xyz")  # it will not give error on random value
print(myset1)

#so discard fun - not throw any error on non existent valeu remove

#example 7 - clear all elements
myset1.clear()
print(myset1)          #empty set

#example 8- delete set variable
del myset1
# print(myset1)   # give error as set deleted

# example 9 - joining 2 set - union()
myset11={"a","b","c"}
myset22={1,2,3}

myset3=myset11.union(myset22)
print(myset3)

# example 10 - joining 2 set - update()
myset11.update(myset22)
print(myset11)

