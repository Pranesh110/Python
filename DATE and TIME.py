#date and time 

import datetime as dt

current_date=dt.date.today()
print(current_date)

#can print as date by giving yr month date

new=dt.date(2025,8,25)
print(new)
print(new.year)
print(new.month)
print(new.day)
#can print seperately also

#--------------

#time

a=dt.time(10,45,5)
print(a)
print(a.hour)
print(a.minute)

#to check current timr

d=dt.datetime.now()
print(d)

#can create our own date and  time

n=dt.datetime(2025,5,31,12,2,10)
print(n)

#to change the format lik wed june 2

s=n.strftime("%A " " %b " " %d " " %Y ")
print(s)