def add_time(start_time, duration, start_day=None):
    start_hour, start_minute_period = start_time.split(":")
    start_minute, start_period = start_minute_period.split()
    #def the function that takes into consideration this 3 parameters
    #start_time define AM and PM
    #duratiom define the hours and minutes to be added
    #start_day define the starting day of the week
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    #we split start time in hours and minutes, and convert it into integer
    duration_hour, duration_minute = map(int, duration.split(':'))
    #same thing here
    start_period = start_period.lower()

    if start_period == "pm" and start_hour != 12:
        start_hour += 12
    #if the start period is PM we add 12 to convert it into 24 hour format

    total_start_minutes = start_hour * 60 + start_minute
    total_duration_minutes = duration_hour * 60 + duration_minute
    #we convert to minutes
    total_minutes = total_start_minutes + total_duration_minutes
    #we add them together
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    #we resplit them after the mathematical operation

    new_period = "AM" if new_hour < 12 else "PM"

    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12
#we determine if we are in AM or PM and make the math
    if start_day:
        start_day = start_day.capitalize()
        days_passed = total_minutes // (24 * 60)
        start_index = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].index(start_day.lower().capitalize())
        new_day_index = (start_index + days_passed) % 7
        new_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][new_day_index]
        day_string = f", {new_day}"
    else:
        days_passed = total_minutes // (24 * 60)
        day_string = ""
#optional: we determine the days passed since the start day
    if days_passed == 1:
        next_day_string = " (next day)"
    elif days_passed > 1:
        next_day_string = f" ({days_passed} days later)"
    else:
        next_day_string = ""
#we costruite the output
    output = f"{new_hour}:{str(new_minute).zfill(2)} {new_period}{day_string}{next_day_string}"
    return output
#example to try if this works
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))