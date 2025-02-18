#example 1-
print("This is starting point of prog..")
print("This is starting point of prog..")
print("This is starting point of prog..")

try:
    print(x)   # no termination will occur here
except:
    print("exception occured")

print("This is end point of prog..")
print("This is end point of prog..")
print("This is end point of prog..")

#example 2-

print("This is staring point of example2..")
print("Program in progress")
try:
    print(10/0)     #ZeroDivisionError: division by zero

except ZeroDivisionError:  #mention name but it will not work if any other type of exc found
    print("exception occured")

print("This is end point of example2..")

#example 3- multiple except blocks, else, finally
try:
    num1,num2=10,0
    result=num1/num2
    print("result is:" ,result)
except ZeroDivisionError:
    print("thrown 0 divison")
except SyntaxError:
    print("thrown syntax error")
except:
    print("exc handled")

else:      #optional, but written after all exception stmts
    print("no exceptions found")

finally:  #optional, but written in last
    print("always executed")


#example 4- user defined exceptions - Raise

def enterAge(age):
    if age<0:
        raise ValueError("only +ive age allowed")
    if age>15:
        print("not child")
    else:
        print("child")


enterAge(-1)

# handle above exception when user runs the not met condition
# comment above code

age1=-1
try:
    enterAge(age1)
except ValueError:
    print("ValueError exception occured")