
# input function is used to input user value
#input("enter first number:")
num1=input("enter first number:")
num2=input("enter sec number:")
# data type of num1 and num2 = is always considered as String type, whatever enetred by user =is string
#check datat type
print(type(num1))
print(type(num2))


# if both are string , can we perform + operation when provided nuber value
print(num1+num2)  #out=100200

#we need to convert inputs to number format= called type conversa

#method1
num1=int(input("enter first number:"))
num2=int(input("enter sec number:"))
print(num1+num2)

#method2- convert while calculating
num1=input("enter first number:")
num2=input("enter sec number:")
print(int(num1)+int(num2))

#example of decimal number
num1=input("enter first decimal number:")
num2=input("enter sec decimal number:")
print(num1+num2)        # res will be concatenation

#so,
print(float(num1)+float(num2))