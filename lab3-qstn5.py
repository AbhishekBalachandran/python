# one
# two
# three
# four
# five
list = []
f = open("C:\lab\python\samplefile2.txt","r")
list = [lines.strip() for lines in (f.readlines())]
print("the lines when stored in to a list is \n",list)
f.close()
print(type(list))