import SpeakListen as sl
import webbrowser

#Function to open youtube.
def open_whatsapp():
    url = "https://web.whatsapp.com/"
    webbrowser.open(url)
    sl.speak("Opening what'sapp")
