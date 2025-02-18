import sys
#method 1
#packA
#method1 - sys path and invoke module.func()
sys.path.append("C:/Users/savig/PycharmProjects/PythonTraining/.venv/testcases/day15_packages/packA/")
sys.path.append("C:/Users/savig/PycharmProjects/PythonTraining/.venv/testcases/day15_packages/packB/")
sys.path.append("C:/Users/savig/PycharmProjects/PythonTraining/.venv/testcases/day15_packages/packC/")

import Emp
import Stu

obj1=Emp.Employee("123","smith",34000)       #constructor will run in local module
obj1.displayemp()

obj2=Stu.Student("222","john",3.5)
obj2.displaystu()

#method 2- from keyword - after sys path append

from Emp import *
from Stu import Student

obj1=Employee(102,"steve",7000)

obj1.displayemp()