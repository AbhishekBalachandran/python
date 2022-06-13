# HELLO!
# '''''
# This is a sample file ....
# Thank You.
# ~~~~~~~~~
# The end
# ...

with open("C:\lab\python\mysample.txt","r") as file:
    a = file.read().split()
    m = 0
    for i in a:
        if len(i) > m:
            m = len(i)
            word = i
    file.close()
    print("The longest word is ",word,"with",m,"number of characters.")
    
