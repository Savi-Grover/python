#propertiese of tuple

#-ordered
#-unchangeable, no modifications allowed, immutable, more secure than list
#-written in ()

#example 1 - create tuple

tuple1=('apple','banana','cherry')
print(tuple1)

#example 2 - access tuple items
#use index, starts from 0
print(tuple1[1])

# last element
print(tuple1[-1])

#create empty tuple
tuple01=()

# Example 3: range of indexes
mytuple=("apple","banana","cherry","kiwi")
print(mytuple[2:5])

#count 4 from last end
print(mytuple[-4:-1])

#change tuple values- not possible
# cannot modify existing value
# cannot insert a new value
# cannot append new value
# cannot remove a va;ue

#-- to bring changes, we need to convert tuple to list and then do modifucations

# tuple---------> list(modify)-----> change back to tuple

tuple2=('apple','banana','cherry')
mylist=list(tuple2)

mylist[0]="orange"
print(mylist)

tuple11=tuple(mylist)
print(tuple11)

#reading all elements iteratively
tuple3=('apple','banana','cherry')
for i in tuple3:
    print(i)

# if element present or not

tuple4=('apple','banana','cherry')

if "banana" in tuple4:
    print("yes")
else:
    print("no")

# count/total elements in tuple
print(len(tuple4))

# add items in tuple - not possible
# use list to do that
# lets try adding tuple element
# -- tuple4[3]="kiwi"
# --print(tuple4)
# run time error - TypeError: 'tuple' object does not support item assignment

# copy the tuple

copiedTuple=tuple11
print(copiedTuple)

#joining 2 tuples
tuple33=copiedTuple+tuple11
print(tuple33)

