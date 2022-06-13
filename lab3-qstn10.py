# one
# two
# three
# four
# five
# three
# four
# nine
# nine
# one

with open("C:\lab\python\samplefile2.txt","r") as file :
    word = input("Enter the word to be searched \n")
    s = file.read()
    lst = s.split()
    count = 0
    for i in lst :
        if(i == word):
            count += 1
    print("Word {} occurred {} times".format(word,count))