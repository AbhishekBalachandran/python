f1 = open("C:\lab\python\File1.txt","r") 
f2 = open("C:\lab\python\File2.txt","r")
print("Content of first file is : ",f1.read())
print("Content of the second file is : ",f2.read())

f3 = open("C:\lab\python\mergefile1file2.txt","w")
lines1 = f1.readlines()
lines2 = f2.readlines()
for i in range (len(lines1)):
    merge = lines1[i] + lines2[i]
    f3.write(merge)
f1.close()
f2.close()
f3.close()
f3 = open("C:\lab\python\mergefile1file2.txt","r")
print("Content of the file after combining corresponding lines is : ",f3.read())
f3.close()




# for lines1,lines2 in zip(f1,f2):
#     data = lines1+lines2
#     print("Content of the file after combining corresponding lines is : ",data)