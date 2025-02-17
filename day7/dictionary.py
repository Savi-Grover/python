#example 1- create a dictionary
dict1={101:"abc",201:"ytr",301:"bvg"}
print(dict1)    # may /may not be same order

#example 2- access the items from dictionary
dict2={
    "brand": "hyudai",
    "model": "i10",
    "year" : 2021
}

print(dict2["brand"])    # key act as index in dictionary'

#example 3- access the items from dictionary using get()
x=dict2.get("model")
print(x)

#example 4- change values in dict - using key
dict2["year"]=2022
print(dict2)

#example 5 - read all elements using for loop

# capture only key
for i in dict2:
    print(i)

#capture only values
for i in dict2:
    print(dict2[i])

for i in dict2.values():
        print(i)

#capture key value both
for x,y in dict2.items():
    print(x,y)

#example 6- check key is existed in dictionary or not
dict3={
    "brand": "hyudai",
    "model": "i10",
    "year" : 2021

}

if "model" in dict3:
    print("exist")
else:
    print("not exist")

#or
print("model" in dict3)  # true or #false

#example 7- length of dict
print(len(dict3))

#example 8- add items in dict- add new key -value
dict3["color"]="red"
print(dict3)

#example 9 - remove items in dict- remove by key - use pop()
dict3.pop("year")
print(dict3)

#example 10- del method
del dict3["model"]
print(dict3)

#example 11- del whole dict
del dict3
#print(dict3)     #name error

#example 12 - clear items but empty dict remains
dict1.clear()
print(dict1)

#example 13- copy dict to other dict - without using copy()
dict22=dict2
print(dict22)

#copy()
dict4=dict22.copy()
print(dict4)

