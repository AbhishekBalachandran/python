string = input("Enter the string:")
string = string.replace(" ","").lower()
characterList = {}
for x in string:
	if x in characterList:
		characterList[x] +=1
	else:
		characterList[x] =1
count = 0
for x in characterList:
	if characterList[x]>1:
		count +=1
print("Count of repeated characters")
print(count)
