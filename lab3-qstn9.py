# one
# two
# three
# four
# five


with open("C:\lab\python\samplefile2.txt","r") as file:
    line_count = 0
    for line in file:
        if line != "\n":
            line_count +=1
file.close()
print("The number of lines are ",line_count)