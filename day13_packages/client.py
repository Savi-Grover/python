import sys

#path of package pack1

#method1 - sys path and invoke module.func()
sys.path.append("C:/Users/savig/PycharmProjects/PythonTraining/.venv/testcases/day13_packages/pack1")

import module1
import module2

module1.display()
module2.show()

#method2- from keyword
from module1 import *
from module2 import *

display()
show()
