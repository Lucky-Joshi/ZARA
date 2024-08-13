import webbrowser
import SpeakListen as sl

def open_weather_website(location):
    location = location.replace(' ', '+')
    # Construct the URL for the weather search
    url = f"https://www.google.com/search?q=weather+{location}"
    # Open the URL in the default web browser
    webbrowser.open(url)

#Function to remove search from query for searching.
def remove(query):
    s=""
    query=query.split(' ');query.remove("tell");query.remove("me");query.remove("weather");query.remove("of");query.remove("weather")
    for i in query:
        s=s+i+ " "
    query=s
    return query