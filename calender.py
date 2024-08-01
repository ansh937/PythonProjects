import calendar

year=int(input("Enter the year for which you want the calendar for: "))
months=int(input("Enter the months ypu want the calender for: "))

calender=calendar.month(year,months)
print(calender)