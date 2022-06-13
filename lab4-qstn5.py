from datetime import date, timedelta


date1 = date(2000, 2, 28)
date2 = date(2001, 2, 28)
print("\nDays between ",date1," and ",date2," are \n")
daysbtwn = date2 - date1
for i in range (daysbtwn.days + 1):
    day = date1 + timedelta(days=i)
    print(day)