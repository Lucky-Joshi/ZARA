import SpeakListen as sl
import googlesearch as gs
import youtubefile
import weather

# Main function.
def main():
    sl.speak("How can I help you")
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
             sl.speak("Opening Youtube")
             youtubefile.open_youtube()

        elif "weather" in query:
            sl.speak("Here is the weather report")
            weather.open_weather_website(query)


        elif "exit" in query or "quit" in query:
            sl.speak("Goodbye Boss!")
            break