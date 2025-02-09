
#2 data type for number= int; float
#1 data type for str for string

num1=100
num2=10.5
print(type(num1))
print(type(num2))

# example 1
# find maximum of all numbers -max()
print(max(10,20,30))

#min
print(min(10.4,20,30.5))

#example2
#strings - few imp functions -

s="welcome"
s='welcome'
s=str('welcome')

#creating empty string varibales
name=""
name=''
name=str()

#muttable( can be changed value of var) and
#immutable( cannot change the value of var)

str1="welcome"
print(id(str1))        # will give id of mem str11 having value=welcome

str1=str1+"to python"  # new value = welcome to python will b e ref by mem str1
print(id(str1))	       # new id value will be not be same

# so above we see, if value is changed after updation, then it is immutable

# example 3: + and * with string

str="welcome"
print(str+"programming") # concetenate
print(str*2)  # printed 2 times

# example 4
#slicing concept - uses [] operator
str1="welcome"
print(str1[1:3])

# starting index 0
# ending index 3 but not included = answer is el

print(str1[:6])  # answer= welcom, starting index default to 0
print(str1[2:])

print(str1[1:-1])  # -1 will remove last char in string

print(str1[1:-2])

# example 5- ord() and char()
#ord()= return eqv ASCII number of a char

print(ord('A'))

#chr()= return eqv char when passed ascii number
print(chr(65))

# example 6 : max() , min(), len()
print(max("abc"))
print(min("abc"))
print(len("abc"))

# example 7 -in and not in operator
s='welcome'
print("come" in s)  # True
print("lome" in s)  # false
print("lome" not in s) # true

# example 8 - compae str using relational operators
print("tim"=="tie")  #fal
print("free"!="freedom") #t
print("arrow" > "aron")  #t # check alphabetical order
print("right" >= "left") #t
print("teeth" < "tee") #f
print("yellow" <= "fellow") #f # y is greater than f
print("abc" > "") #t

# example 9- testing strings true/false

s="welcome to python"
print(s.isalnum())          #false - func will check if str contain any number
print("Welcome".isalpha())  #true -check is Welcome is alpha
print("2012".isdigit())	    #tr
print("first Number".isidentifier())  #false, check python keywords
print(s.islower())	    # true, check if str contains lower
print("WELCOME".isupper())  # tr
print(" ".isspace())        # t

# example 10 -substring functions
s="welcome to python"
print(s.endswith("thon"))  #tr
print(s.startswith("good")) #false
print(s.find("come"))  #3
print(s.find("become")) #-1
print(s.count("o"))   #3

#Example 11 - Converting string
s="String in Python"
s1=s.capitalize()
print(s1)  # each wprd starts with uppercase

s2=s.title()
print(s2)

s3=s.lower()
print(s3)

s4=s.upper()
print(s4)

s5=s.swapcase()  #called camelcase
print(s5)

s6=s.replace("in","on")
print(s6)   #string on Python

#example 12 = reverse logic using for loop
s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reversed string is:", rev_str)

#example 13= another example of rev
s="welcome"
rev_str=s[::-1]  #start:end:-1 ; default start=0
print(rev_str)








































