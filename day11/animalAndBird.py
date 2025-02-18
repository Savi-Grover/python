# best approach- we want to call function from animal and bird

import animal1
import bird1

animal1.fly()
animal1.color()

bird1.fly()
bird1.color()


#mthod2

from animal1 import *
from bird1 import *

fly()      #problem - which module is will be called? # bird- latest imported
color()   #bird module called

# solution to above
from animal1 import *
fly()
color()

from bird1 import *
fly()
color()

