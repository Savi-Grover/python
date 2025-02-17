#example 1- positional example = i and j are ordered based on position
def func1(i,j):
	print(i,j)

func1(10,20)


#example 2- keyword arguments- explicitely specify valeu to particuler param , not ondering their position
def func2(i,j):
	print(i,j)

func2(j=10,i=20)

#example 3-default values  assigned to positional arguments

def func3(i,j=10):
	print(i,j)

func3(100,200)      # default valeu will be replaced by 200

func3(100)       #default j value will be used

#example 4-keyword arguments
def greetings(name, greetsmsg):
    print(greetsmsg+" "+name)

greetings('John', 'Good Morning')

greetings(greetsmsg='Good Morning', name='John')


#example 5- combination of positional and keyword arguments

def my_combo_func(a,b,c):
    print(a,b,c)

my_combo_func(10,20,30)  # positional


my_combo_func(a=10,b=40,c=90)  # keyword

my_combo_func(b=40,a=10,c=90)  # keyword argument

my_combo_func(10,40,c=110)  #combinational

my_combo_func(10,b=40,c=110)  #combinational

# my_combo_func(10,b=20,30) # order=positional, keyword, positional again - wrong order
# #SyntaxError: positional argument must appear before keyword argument - RULE

my_combo_func(10,c=40,b=110) # logical error