string = str(input("enter a string : "))
string_lower = string.lower()
rev_string = string_lower[::-1]
if string_lower == rev_string:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
