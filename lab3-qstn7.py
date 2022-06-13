array = []
with open("C:\lab\python\samplefile2.txt","r") as file:
    lines = file.read().splitlines()
    for line in lines :
        array.extend(line.split())
    print(array)
file.close()
