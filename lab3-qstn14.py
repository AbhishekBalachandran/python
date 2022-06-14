# Content of the first file is   :    File1Line1 :
#                                     File1Line2 :
#                                     File1Line3 :


# Content of the second file is   :   File2Line1
#                                     File2Line2
#                                     File2Line3 
                      

print("Content of the file after combining corresponding lines is : \n")
file1 = open("C:\lab\python\File1.txt","r")
file2 = open("C:\lab\python\File2.txt","r")
for line1,line2 in zip(file1,file2):
    data = line1+line2
    print(data)