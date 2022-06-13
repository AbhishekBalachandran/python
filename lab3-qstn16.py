with open("C:\lab\python\samplefile2.txt","r+") as f:
    line = f.readlines()
    print(line)
    [print(l.strip()) for l in line]