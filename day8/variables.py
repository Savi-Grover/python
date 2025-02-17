#local and global variables

#example1 - declaration of local and global var

global_var=20 #not used within func, it is global

def func():
    local_var=10 #local var
    print(local_var)
    print(global_var) # global can be accessed by func

func()

# print(local_var)  # error - local can not be accessed outside the func

#example 2: local vs global priority

xy=100

def cool():
    xy=200
    print(xy)  # prioirty willbe given to local if name same as global


cool()

#example 3- access GV-inside func, and change it
xyz=100

def cool():
    global xyz     #refer GV
    xyz=500       #change gv

    #or
    # global xy=500   # invalid syntax in python
    print(xyz)  # prioirty willbe given to local if name same as global


cool()
print(xyz)       #  changed Gv can also be called outside func

#example 4-  GV can also be created inside func ; but with global keyword

def cool3():
    global c
    c=50
    print(c)

cool3()

print(c)  # can be accessed outside the func