import datetime

year = int(input())
month = int(input())

days = 0 

if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28

#Using loop to capture every day of the month, and then to judge whether the day is equal to "3" or not.
for i in range (1,(days+1)):
    p1 = datetime.datetime(year,month,i)
    if p1.strftime('%w') == '3': #Change the figure to determine other days of the week.
        print(p1.strftime('%Y-%m-%d'))
