# HELLO!
# '''''
# This is a sample file ....
# Thank You.
# ~~~~~~~~~

file = open("C:\lab\python\mysample.txt","r")
n = int(input("Enter the number of lines to be read : "))
if n<=0:
    print("O lines are read.Kindly enter minimum 1.")
else:
    for i in range(n):
        line = file.readline()
        print(line)
file.close()