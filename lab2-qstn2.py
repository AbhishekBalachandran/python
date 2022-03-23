test_string = str(input("Enter a string to count the character frequency : "))
test_stringUpper = test_string.upper()
count = {i : test_stringUpper.count(i) for i in set(test_stringUpper)}
print("The count of characters(character frequency) in " ,test_string,"is : \n", count)