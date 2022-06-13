from datetime import datetime


currentDateTime = datetime.now()
year,week_num,day_of_week = currentDateTime.isocalendar()
currentMonth = currentDateTime.month
day_of_year = currentDateTime.timetuple().tm_yday
day_of_month = currentDateTime.timetuple().tm_mday
day_of_week = currentDateTime.timetuple().tm_wday

print("Current date and time is ",currentDateTime,"\n")
print("Current year is ",year,"\n")
print("Week number of the year is",week_num,"\n")
print("Weekday of the week is ",day_of_week,"\n")
print("Day of year is ",day_of_year,"\n")
print("Day of month is ",day_of_month,"\n")
print("Day of week is ",day_of_week,"\n")