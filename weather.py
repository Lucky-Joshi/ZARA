import webbrowser
import SpeakListen as sl

def open_weather_website(location):
    location = location.replace(' ', '+')
    # Construct the URL for the weather search
    url = f"https://www.google.com/search?q=weather+{location}"
    # Open the URL in the default web browser
    webbrowser.open(url)
