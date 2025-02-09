# while loop

# print 1....10 numbers
# while declare loop- we need 3 things -initialisaton/strt point, increment, condition

i=1  #initialisation
while i<=10:    #condition
    print(i)
    i=i+1       #increment
    #print("loop") - part of loop

print("Done") # this is outside of loop

# print 1....10 numbers in descending order=10,9,8,7....1
i=10  #initialisation
while i>0:    #condition or i>=1
    print(i)
    i=i-1       #increment

# for loop
# advantage = all 3 things writen in one line using range()
# so less lines of code
# also we use in operator

# print 1....10 numbers

for i in range(10):
    print(i)     # 0....9

# start=1; last= n-1
for i in range(1,11):
    print(i)  # 0....10


# only even number between 1 to 20
for i in range(1,21,1):
    print(i)  # 0....10

# or
for i in range(0,21,2):
    print(i)  # 0....10

# decending order
for i in range(10, 0, -1):
    print(i)  # 0....10

# to print - 5,10,15.....100
for i in range(5, 101, 5):
    print(i)  # 0....10

