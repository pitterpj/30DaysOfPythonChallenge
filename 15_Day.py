# Exercises - Day 15
# Día 15 - 30DaysOfPythonChallenge

### DATES ###

# 💻 Exercises: Day 15
# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
from datetime import date

now = datetime.now()
now_day = now.day
now_month = now.month
now_year = now.year
now_hour = now.hour
now_minute = now.minute
now_timestamp = now.timestamp()
# print(now_year)
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(current_date)
# Today is 5 December, 2019. Change this time string to time.
today = datetime( 2019, 12, 5)
# print(today)
# Calculate the time difference between now and new year.
new_year = date(2024, 1, 1)
diff =  new_year - now.date() 
# print(diff)
# Calculate the time difference between 1 January 1970 and now.
january_1970 = date(1970, 1, 1)
diff = now.date() - january_1970
# print(diff)
# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# 🎉 CONGRATULATIONS ! 🎉