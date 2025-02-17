#example 1- create a function
# def nameOffun():

def myfunc():
    print("first function")

#call function
myfunc()

#example 2- parameterized function
def myfunc1(name):
    print("Hello" ,name)

myfunc1('Smith')

#example 2- multi parameterized function
def add(a,b):
    return(a+b)

sum=add(5,4)
print(sum)
print(add)    #write memory add of function

#example 3: empty func
def fec1():
    return


print(fec1())   # output is None

#example 4- function can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(5,2))

print(largest(2,8))

#store res in var
res=largest(10,20)
print(type(res))

# why tuple - beacsue ()
# if a functions can give multiple valeu= that menas tuple type function
