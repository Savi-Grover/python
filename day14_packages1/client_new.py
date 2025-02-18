import sys

#path of package pack1

#method1 - sys path and invoke module.func()
sys.path.append("C:/Users/savig/PycharmProjects/PythonTraining/.venv/testcases/day14_packages1/")

import module1
module1.display()


sys.path.append("C:/Users/savig/PycharmProjects/PythonTraining/.venv/testcases/day14_packages1/pack2")

import module2
module2.show()

#method2- from keyword
from module1 import *
from module2 import *

display()
show()
