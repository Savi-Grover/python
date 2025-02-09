name="John"
age=30
sal=5000.50

# method 1
print(name,age,sal)

# method2 - output in meaningful mannner

print("Name is:" , name)
print("Age is:" , age)
print("Sal is:" , sal)

# method3 - use % operator s- string ; d- int; g for decimal

print("Name is: %s Age is: %d Sal is:  %g" %(name,age, sal))

# method 4 use {} for values and .format to substiut values - shud be in proper order in .format

print("Name is: {} Age is: {} Sal is:  {}" .format(name,age, sal))

print("Age is: {}  Name is: {} Sal is:  {}" .format(name,age, sal)) #answer wrong because order changed

