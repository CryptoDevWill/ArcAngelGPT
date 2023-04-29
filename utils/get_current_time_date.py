



import datetime

def get_current_time_date():
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time as strings
    date = now.strftime("%A, %B %d, %Y")
    time = now.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
    time_of_day_str = "AM" if now.hour < 12 else "PM"

    # Construct the formatted time and date strings
    formatted_time = "{} {} on {}".format(time, time_of_day_str, date)
    time = "{} {}".format(time, time_of_day_str)

    # Return the time and date as a tuple
    return (time, date)
