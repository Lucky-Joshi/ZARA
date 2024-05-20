import SpeakListen as sl
import webbrowser

#Function for search.
def search(query):
    search_url = "https://www.google.com/search?q="
    final_url = search_url + '+'.join(query.split())
    sl.speak("Searching")
    webbrowser.open(final_url)

#Function to remove search from query for searching.
def removesearch(query):
    s=""
    query=query.split(' ')
    query.remove("search")
    for i in query:
        s=s+i+ " "
    query=s
    return query



