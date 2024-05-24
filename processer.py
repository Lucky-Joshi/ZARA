import SpeakListen as sl
import googlesearch as gs
import youtubefile
import weather
import song 
import whatsapp

# Main function.
def main():
    sl.speak("How can I help you ?")
    while True:
        query = sl.listen().lower()

        if "hello" in query:
            sl.speak("Hello! How can I assist you today?")

        elif "what is your name" in query:
            sl.speak("I am Zealous Artificial Responsive Assistant or you can call me ZARA.")

        elif "for what zara stands for" in query:
            sl.speak(" It stands for Zealous Artificial Responsive Assistant.")

        elif "search" in query:
            gs.search(gs.removesearch(query))

        elif "open youtube" in query:
             youtubefile.open_youtube()

        elif "weather" in query:
            sl.speak("Here is the weather report!")
            weather.open_weather_website(weather.remove(query))
        
        elif "play" in query:
            sl.speak("select video you want!")
            song.play_song(song.removeplay(query))

        elif "open what'sapp" in query or "open whatsapp" in query:
            whatsapp.open_whatsapp()

        elif "exit" in query or "quit" in query:
            sl.speak("Goodbye Boss!")
            break