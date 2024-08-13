import webbrowser

def play_song(song_name):
    # Replace spaces with '+' to format the search query
    query = song_name.replace(' ', '+')
    # Construct the YouTube search URL
    url = f"https://www.youtube.com/results?search_query={query}"
    # Open the web browser with the URL
    webbrowser.open(url)
    print(f"Searching for {song_name} on YouTube...")

#Function to remove play from query for searching.
def removeplay(query):
    s=""
    query=query.split(' ')
    query.remove("play")
    for i in query:
        s=s+i+ " "
    query=s
    return query