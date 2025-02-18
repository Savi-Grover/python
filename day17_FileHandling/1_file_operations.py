#example 1- text file

# save in var file, write mode; there are r= read, a=append
file=open("C:\DemoFiles\myfiles.txt",'w')

file.write("stmt1...")   #write removes exsiting data and add new content in w mode
file.write("stmt2...\n")  #new line \n
file.write("stmt3...")

file.close()

print("text file prog completed")

#example 2- read from text file
file=open("C:\DemoFiles\myfiles.txt",'r')

file.readline()  #read first line only

print(file.read())  #read whole and print

file.close()

#example 3- append in existing data in text file
file=open("C:\DemoFiles\myfiles.txt",'a')

file.write("sixth line ")
file.write("seventh line \n")
file.write("eigth line \n")
file.close()

#example 4- 