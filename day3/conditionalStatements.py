
#3 types -
#conditional ( 3 types -if, if..else, elif)
#looping (while for )
#jumping statements (break continue)

##conditional statements
#example1: print a person is eligible for vote or not
age=int(input("Enter age:"))
if age>=18:
	print("eligible for vote")

# to write else part of above
age=int(input("Enter age:"))
if age>=18:
	print("eligible for vote")
else:
	print("not eligible for vote")

# we can also write multiple stmts in if
age=int(input("Enter age:"))
if age>=18:
	print("eligible for vote")
	print("eligible for vote")
	print("eligible for vote")
else:
	print("not eligible for vote")

#Example 2
if True:
	print("true condition")

else:
	print("false condition")

#Example 3
if 1:
	print("one")
else:
	print("not one")


# elif
age=int(input("Enter age:"))
if age>=18:
	print("eligible for vote")
elif age>15 or age<=17:
	print("can vote conditionally")
else:
    print("not eligible")

# example -
num=10
if num%2==0:
    print("Given number is Even")
else:
    print("Given number is odd")

# use ternary operator to use if else in single line

num=10
print("even") if num%2==0 else print("odd")

# multiple stmts in single line using {}

a=20
{print("hello"), print("python")} if a >=10 else {print("welcome"),print("python")}

# elif example
weekno=2
if weekno==1:
	print("sunday")
elif weekno==2:
	print("monday")
elif weekno==3:
	print("tues")
elif weekno==4:
	print("wed")
elif weekno==5:
	print("thur")
else:
	print("invalid week number")























