countries = ("INDIA","USA","CHINA","PAKISTAN","UK")
print("The sample tuple is \n",countries)
input = input("Enter the country : ").upper()
index = countries.index(input)
print("The index of ",input ,"is ",index)