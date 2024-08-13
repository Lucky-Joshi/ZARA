import SpeakListen as sl
import googlesearch as gs
import youtubefile
import weather
import song 
import whatsapp
import openfile
import CodeSuggestor
import Summariser
import VirusDetector

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

        elif "open file" in query:
            sl.speak("Enter File name")
            filename=input("Enter File name")
            openfile.open_file(filename)
        
        elif "give me suggestion for a code" in query:
            sl.speak("Sure boss! Just provide me the required inputs")
            CodeSuggestor.main()
        
        elif "summarise the pdf file" in query:
            sl.speak("Sure boss! Just provide me the required inputs")
            Summariser.require()
        
        elif "detect virus in the link" in query:
            sl.speak("Sure boss! Just provide me the required inputs")
            VirusDetector.main()
            
        elif "exit" in query or "quit" in query:
            sl.speak("Goodbye Boss!")
            break