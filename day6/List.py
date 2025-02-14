#propertiese of Lists

#-written in []
#-ordered- order of elements matter. changeable/mutable - one elem can be changed by other value- add, dldete operations

#example 1- create list
myList1=[10,20,30,50]
myList2=["apple","banana","cherry"]
myList3=["Apple", 10, "banana", 20]
myList4=list()   # empty List
print(myList1)
print(myList2)
print(myList3)
print(myList4)

# example 2 - accessing items from the list
myList11=["apple","banana","cherry"]

# item indexed from 0
print(myList11[2])

# to return last element, we use -1
print(myList11[-1])

#example 3- Range of indexes, (last range not included)
myList21=["apple","banana","cherry","orange","kiwi","melon", "mango"]
print(myList21[2:5]) # start from index 2 to 5-1=(4)
print(myList21[-4:-1])  # -4 is counted from end of list, last element -1 not included

#example 4= mutation/change a item value on list
mylist31=["apple","banana","cherry"]
print(mylist31)  #change apple to orange

##access the element first, change value & then print
mylist31[0]="orange"
print(mylist31)

#example 5- Iteratively read all items using for loop statement
mylist32=["apple","banana","cherry"]
for i in mylist32:
    print(i)

#example 6- check if item is present in list or not
mylist33=["apple","banana","cherry"]

if "apple" in mylist33:
    print("Yes, apple is present")
else:
    print("No, apple is not present")


# example 7: count total items in list/length
mylist34=["apple","banana","cherry"]
print(len(mylist34))

# example 8: Add items- append() - item added at end of list ; insert()
mylist35=["apple", "banana", "cherry"]
mylist35.append("orange")
print(mylist35)

# if we need to insert item at middle or non-end position
mylist35.insert(1,"kiwi")
print(mylist35)

# example 9: remove item for list - pop and delete
mylist36=["apple", "banana", "cherry"]
mylist36.pop(2)  #specify index
print(mylist36)

#del - keyword
del mylist36[1]   # index
print(mylist36)

#clear()
mylist37=["apple", "banana", "cherry"]
mylist37.clear()
print(mylist37)      # only list var is left , but items are removed

#example 10: copy list
mylist111=["apple","banana","cherry"]

#method1 - list function
mylist222=list(mylist111)

print(mylist111)
print(mylist222)

#method 2 - copy function
mylist223=mylist111.copy()

print(mylist111)
print(mylist223)

#example 11- combine/join 2 lists
#concatenation or + operator
list01=['a','b','c']
list02=[1,2,3]
list03=list01+list02
print(list03)

#using loop stmt
for i in list02:
    list01.append(i)
print(list01)

#using extend function
list01.extend(list02)
print(list01)













