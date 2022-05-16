tuple_1 = ('a','b','c','d','e','f')
print(tuple_1)
string = input("Enter the char want to check:")
try:
	index = tuple_1.index(string)
	print("Index of",string,"is",index)
except Exception as e:
	print("Input given is not in tuple")
