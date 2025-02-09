import time
from calendar import isleap

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("Enter your name : ")
dob = input("Enter your date of birth in  dd/mm/yyyy : ")
lis = dob.split("/")
localtime = time.localtime(time.time())


month = (localtime.tm_year - int(lis[2]) - 1) * 12 + localtime.tm_mon + (12 - int(lis[1]))

day = 0
begin_year = int(lis[2]) + 1 
end_year = localtime.tm_year
leap_year = isleap(localtime.tm_year)
for y in range(begin_year, end_year ):
    if (isleap(y)):
        day = day + 366
    else:
        day = day + 365

for i in range(1 , localtime.tm_mon):
    day = day + month_days(i , leap_year)

day = day + localtime.tm_mday 

if(int(lis[1]) < 12 ):
    for m in range(int(lis[1]) + 1, 12+1):
        day = day + month_days(m , isleap(int(lis[2])))
day = day + (month_days(m , isleap(int(lis[2]))) - int(lis[0]))    

print(f"{name}'s age is {int(month/12)} years.")
print(f"In months : {month} months")
print(f"In days : {day} days")






    
    
    