n = int(input("Enter the number of last lines to be read : "))
f = open("C:\lab\python\mysample.txt","r")
for line in (f.readlines() [-n:]):
    print(line)
f.close()