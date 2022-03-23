lst = []
string = ""
limit = int(input("How many characters : "))
print("Enter the characters : ")
for i in range(limit):
    characters = str(input(""))
    lst.append(characters)
print("The list of characters are \n",lst)
for i in lst:
    string += i
print("The string is :",string, "\n The type is : ",type(string))

