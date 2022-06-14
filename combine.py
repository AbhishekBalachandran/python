print("Content of the file after combining corresponding lines is : \n")
file1 = open("C:\lab\python\File1.txt","r")
file2 = open("C:\lab\python\File2.txt","r")
for line1,line2 in zip(file1,file2):
    data = line1+line2
    print(data)