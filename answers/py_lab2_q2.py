string = input("Enter the string:")
string = string.replace(" ","").lower()
characterList = {}
for x in string:
	if x in characterList:
		characterList[x] +=1
	else:
		characterList[x] =1
print("Character frequency is")
print(characterList)
print(type(characterList))