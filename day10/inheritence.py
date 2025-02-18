#example 1: single inheritence

class A:
    def m1(self):
        print("this is m1 mthod from class A")

class B(A):       #B child of A
    def m2(self):
        print("this is m2 mthod from class B")

objB=B()
objB.m1()
objB.m2()

#example 2 : one more way of single inheritence

class AA:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class BB(AA):
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

bobjB=BB()
bobjB.m1()
bobjB.m2()

#example 3 - multi-level inheritence

class A1:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B1(A1):
    a,b=200,100
    def m2(self):
        print(self.a-self.b)
class CC(B1):
    i,j=200,100
    def m3(self):
        print(self.i*self.j)

objc=CC()
objc.m1()
objc.m2()
objc.m3()

#example 4- hierarchy inheritence
# A2 is parent to B2 and C2
class A2:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B2(A2):
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

class C2(A2):
    i,j=200,100
    def m3(self):
        print(self.i*self.j)

        # obj of c caanot access properties of B

Bobj=B2()
Bobj.m1()
Bobj.m2()

Cobj=C2()
Cobj.m1()
Cobj.m3()

#example 5- multiple inheritence

class P1:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class P2:
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

class C1(P1,P2):
    i,j=200,100
    def m3(self):
        print(self.i*self.j)

objC=C1()
objC.m1()
objC.m2()
objC.m3()

#Example 6- concepts in inheritance

# method overriding - same method in parent overriden in child class

class A1A:
    def m1(self):
        print("This is m1 method from class A")


class B1B(A1A):
    def m1(self):
        print("This is m1 method from class B")


objB1B=B1B()
objB1B.m1()    #child class method will run


#example 7 - access class var in inheritence

class A100:
    a,b=10,20

class B100(A100):
    i,j=100,200
    def m(self,x,y):
        print(x+y)  #local var
        print(self.i+self.j)  # class var
        print(self.a+self.b)  # class var
objB100=B100()
objB100.m(1000,2000)

#example 8- overriding variables

#that means parent class variables , inherited and changed by child classes

class Parent:
    name="Scott"

class Child(Parent):
    name="smith"    # overriding the variables value
    def test(self):
        print(super().name)   # if we want to use parent name

objParent=Child()
objParent.name
print(objParent.name)

# objParent.test  # if we want to print parent name , we need to use a method in parent class = def test (self)

#example 9 - Overriding methods

class Parent1:
    name="Scott"
    def house(self):
        print("house from Parent1")

class Child1(Parent1):
    name="smith"    # overriding the variables value
    def house(self):
        print("house from Child1")

objParent1=Child1()
objParent1.house()

#example 10- overloading , or # polymorphism in python
#one mthod-many forms , diff arguments

class Hello:

    def sayhello(self,name=None):
        if name is not None:
            print("Hello" +name)
        else:
            print("hello")


h=Hello()
h.sayhello("Gianna")   # one method with param
h.sayhello()          # same method , no argument

#example 11 -another example of overloading
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)


addobj=Calculation()
addobj.add()
addobj.add(10,20)
addobj.add(10,20,50)