import SpeakListen as sl
import webbrowser

#Function to open youtube.
def open_youtube():
    url = "https://www.youtube.com"
    webbrowser.open(url)


# #Function for opening video  by title.
# def open_youtube_video_by_title(video_title):
#     # Construct the YouTube search URL.
#     search_query = '+'.join(video_title.split())
#     youtube_url = f"https://www.youtube.com/results?search_query={search_query}"

#     # Open the search URL in a web browser.
#     webbrowser.open(youtube_url)

# sl.speak("Tell me the title of the video you want to watch. ")
# video_title = sl.listen()


# #unction search youtube channel.
# def open_youtube_channel(channel_name):
#     base_url = "https://www.youtube.com/"
#     channel_url = f"{base_url}/user/{channel_name}"
#     webbrowser.open(channel_url)

# sl.speak("Tell me channel name")
# channel_name = sl.listen()

