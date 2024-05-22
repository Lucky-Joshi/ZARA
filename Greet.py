import datetime

#Function to wish.
def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 6 <= hour < 12:
        return "Good morning Boss!"
    elif 12 <= hour < 18:
        return "Good afternoon Boss!"
    elif 18 <= hour < 22:
        return "Good evening Boss!"
    else:
        return "Hello Boss!"
