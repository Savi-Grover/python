
#method1 - import module class and call method using syntax= className.methodName(params)

# import CalculatorModule
# CalculatorModule.add(10,20)
# CalculatorModule.mul(5,2)

#method2 - from class import specific fun
from CalculatorModule import add, mul

add(10,20)
mul(5,2)

#method3 - from class import * - all functions
from CalculatorModule import *
add(100,200)
mul(5,4)
