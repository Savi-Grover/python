# access function of a.py and b.py


# method1 - import module, make obj by assining filename.className, then invoke method
import a
import b

# obj=fileName.className
obja=a.Animal()

#obj.invokeMethod
obja.display()

#same for another class
objb=b.Bird()
objb.display()

# method 2- from keyword

from a import Animal
from b import Bird

obj1=Animal()
obj1.display()

obj2=Bird()
obj2.display()