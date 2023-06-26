### DATES ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.hour)
    print(date.day)
    print(date.min)
    print(date.minute)
    print(date.year)
    print(date.month)

#print_date(now)

year_2023 = datetime(2023,1,1)


#print_date(year_2023)

from datetime import time

current_time =  time()

print(current_time.max)

