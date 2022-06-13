with open("C:\lab\python\samplefile2.txt","r") as file:
    lines = file.read().splitlines()
    variable = lines
print(variable)
file.close()