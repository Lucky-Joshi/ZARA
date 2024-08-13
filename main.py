import SpeakListen as sl
import Greet as g
from processer import main

wake_up= sl.listen().upper()
if "ZARA" in wake_up:
    sl.speak(g.greeting())
    main()