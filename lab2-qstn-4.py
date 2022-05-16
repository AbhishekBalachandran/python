str = str(input("Enter the string to count repeated characters \n"))
print("Repeated characters and their count are : \n")
for i in range (0,len(str)):
    count = 1
    for j in range (i+1,len(str)):
        if(str[i]) == str[j] and str[i] != " ":
            count = count + 1
            str = str[:j]+ '0'+ str[j+1:]
    if(count > 1 and str[i] != '0'):
        print(str[i], "-" , count)
