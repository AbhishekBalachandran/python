lst = ["HTML","CSS","BOOTSTRAP","JAVASCRIPT","ANGULAR"]
with open("C:\lab\python\itemnotes.txt","w+") as file:
    for items in lst:
        file.write('%s\n' %items)
file.close()
with open("C:\lab\python\itemnotes.txt","r") as file:
        print("\nFile written successfully and the file is\n",file.read())
file.close()