#example 1- create class and obj

class class1:
    def func1(self):         # self is always written , default param in METHOD which indicates methods associated to class name in method definition
        pass
    def display(self,name):   #extra param will be given after self
        print(name)

#object of class
class1()

#store obj in var, creating 2 obj
obj1=class1()
obj2=class1()

#calling /invoking methods - instance methods
obj1.func1()
obj2.display("john")

#example 2- two types of methods within the class

#1. instance method - called through the object
#2. static method - directly call using class, no obj needed, these methods are common for every object

class class2:
    def m1(self):   #self represents class , not any param
        print("this is instance method")

    @staticmethod
    def m2(self,num): #self keyword in static method is diff, here it does notvrefer to class self, here it just param
        print(num)

#obj
mc=class2()

mc.m1()

mc.m2(10,100)  # we need to use self while calling static method through obj

# calling m2 directly without obj
class2.m2(10,20)

#example 3- local & global variables in class

#Global variables
#Local variables
#class variables

class myclass:
    a,b=10,20    #class vairbales , cannot be accessed inside method
    def add(self):
       # print(a,b)
        print(self.a+self.b)    #to access class var inside method using self
    def mul(self):
        print(self.a*self.b)
mc=myclass()
mc.add()
mc.mul()

#example 4- all kinds of variables

i,j=15,25 #global varibles

class myclass1:
    a,b=10,20   #class var
    def add(self,x,y): #x,y - local var
        print(x+y)
        print(self.a + self.b)
        print(i+j)      #global var can be direclty accessed

myobj=myclass1()
myobj.add(100,200)

#example 5- same name of global,local & class variables

a,b=15,25 #global varibles

class myclass2:
    a,b=10,20   #class var
    def add(self,a,b): #a,b - local var
        print("answer of example 5")
        print(a+b)   #access local
        print(self.a + self.b)   #access class varibales using self

        print(globals()['a']+globals()['b'])      #global var cannot be direclty accessed because of same name , so we use globals()

myobj=myclass2()
myobj.add(100,200)

#example 6- multiple obj of single class
class demo:
    def method1(self, name):
        print("this is method1")
        print(name)

objj1=demo()
objj1.method1("john")

objj2=demo()
objj2.method1("scott")

#example 7 - constructor
# when method name same as class name
# we use consyrutor hen we need to execute method without explicitely invoking them.
# construcotr automatically executes when class obj created

# method vs cnstructor
#- method - any name, return value/s, can take arguments or params, to call method, we need to use obj
#- constructor - name shud - def __init__(self)
#- name is fixed, do not return any value, can take arguments or param, no obj needed to invoke
#- constructor are called automatically when obj is declared/creation

class constClass:
    def __init__(self):
        print("this is  constructor")

    def m1(self):
        print("hello...")

mcobj=constClass()      # invoke construtor automatically
mcobj.m1()             # need obj to run method m1

#example 8 - constructor with arguments
class name:
    name="smith"
    def __init__(self,name):
        print(name)
        print(self.name)   # class variables accessed by slef

# to call constructor, we need to pass param to obj declaration as constructer is parameterized
mcc=name("David")

#example 9- emp class has one constrcutor with 3 params- id, name, sal
#one more method diplay() - whihc will print id,name,salary

class Emp:
    # no need to create class var here, we can create in method
    def __init__(self, eid, name, sal):
        self.eid=eid  #converting local var to class var
        self.name=name
        self.sal=sal
    def display(self):
        print(self.eid,self.name,self.sal)

e1=Emp(101, "john", 50000)
e1.display()

e2=Emp(102, "Radnor", 60000)
e2.display()


#example 10- emp class has one constrcutor with 3 params- id, name, sal
#one more constructor to -  print id,name,salary

class Emp1:
    # no need to create class var here, we can create in method
    def __init__(self, eid, name, sal):
        self.eid=eid  #converting local var to class var
        self.name=name
        self.sal=sal
    def __str__(self):        # default constuctor which return string type of data
        return(self.ename)

e11=Emp1(101, "john", 50000)
print(e11)         #print obj command will run str constructor



