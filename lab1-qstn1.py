from datetime import date
name = str(input("Enter your name : "))
age = int(input("Enter your age : "))
todays_date = date.today()
current_year = todays_date.year
hundredth_year = current_year + (100 - age)
print("Hello, ",name," you are ",age," years old and you are turning 100 years in the year ",hundredth_year)