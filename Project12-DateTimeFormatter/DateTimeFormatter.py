from datetime import datetime
import pytz
from tzlocal import get_localzone


time1 = input(f"Enter current date and time (YYYY-MM-DD HH:MM): ")

try:
    dt = datetime.strptime(time1, "%Y-%m-%d %H:%M")
    datetime_us = datetime.now(pytz.timezone('US/Central'))
    datetime_ca = datetime.now(pytz.timezone('Canada/Central'))
    datetime_eu = datetime.now(pytz.timezone('Europe/Amsterdam'))
    datetime_du = datetime.now(pytz.timezone('Asia/Dubai'))
    datetime_in = datetime.now(pytz.timezone('Asia/Kolkata'))
    local_timezone = get_localzone()

    print(f"local_timezone: ", local_timezone)
    print(f"Choose a format: ")
    print(f"1. USA time ")
    print(f"2. Canada time")
    print(f"3. London time ")
    print(f"4. UAE time ")



    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("US Central Time :", datetime_us.strftime("%Y-%m-%d %I:%M %p %Z"))
    elif choice == '2':
        print("Canada Time :", datetime_ca.strftime("%Y-%m-%d %I:%M %p %Z"))
    elif choice == '3':
        print("London Time :", datetime_eu.strftime("%Y-%m-%d %I:%M %p %Z"))
    elif choice == '4':
        print("Dubai Time :", datetime_du.strftime("%Y-%m-%d %I:%M %p %Z"))
    else:
        print("UAE Time :", datetime_in.strftime("%Y-%m-%d %I:%M %p %Z"))

except ValueError:
    print("Invalid format! Please use 'YYYY-MM-DD HH:MM'")
