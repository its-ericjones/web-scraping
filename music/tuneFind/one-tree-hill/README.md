# Building a One Tree Hill Soundtrack Playlist

The goal of this project is to gather every song featured in the show One Tree Hill and automatically generate a Spotify playlist.

## How It Works
I'm using the BeautifulSoup library to scrape [TuneFind.com](https://www.tunefind.com), which is a great resource for finding out what music was in TV shows and movies - even within a specific scene. The script goes through and gathers the song titles, artists, and albums for One Tree Hill, saving all that data into a CSV file.


The script will then take that CSV file and use the Spotify API to actually build the playlist. It will read each song entry from the CSV, use the API's search functionality to find the correct track in their catalog, create a new playlist in my Spotify account, and then add all the found songs to it systematically. 
