import shutil


with open("C:\lab\python\stfile.txt","r") as first_file:
    print("Content of first file is :",first_file.read())
with open("C:\lab\python\secondfile.txt","r") as second_file:
    print("Content of second file is :",second_file.read())
with open("C:\lab\python\stfile.txt","r") as first_file, open("C:\lab\python\secondfile.txt","w") as second_file:
    for line in first_file:
        second_file.write(line)
with open("C:\lab\python\secondfile.txt","r") as second_file:
    print("Content of second file after copying first file to second file is :",second_file.read())
first_file.close()
second_file.close()
