## Author: Rojigan Gengatharan
## mp3_lyric_tag.py
## December 23, 2017.
## make the final program an executable and not a python script (but you can inc##  that too, can try using pyinstaller)
## make it so that user decides what name of folder to receive lyrics for 

## look up how to get these libraries, if needed
import eyed3
import os 
import requests
from bs4 import BeautifulSoup

MAX_RETRIES = 20


## use google search/genius search API with search example: chance the rapper lyrics favorite song azlyrics, take out all brackets since prod datpiff and feat will mess with azlyrics

def get_song_lyrics(song_name, song_artist):
    return 0







if __name__ == "__main__":
    
    os.chdir("test_music")

    audiofile = eyed3.load("favorite_song.mp3")

  

    song_title  = audiofile.tag.title
    artist = audiofile.tag.artist

    #lyrics_link = get_lyrics_link(song_title, artist)
    #work on getting one song working then generalize the case using the google search api and test for that
    lyrics_link = "https://genius.com/Chance-the-rapper-favorite-song-lyrics"

    if(lyrics_link != False):


        '''
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('https://', adapter)
        r = session.get(lyrics_link)
        '''
    
        page = requests.get(lyrics_link)
        print(page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        ## html = list(soup.children)[2]

        mydivs = soup.find_all("div", { "class" : "lyrics" })
        lyrics = mydivs[0].get_text().lstrip()
        ## lyrics_u = unicode(lyrics, "utf-8")


        
        
        audiofile.tag.lyrics.set(lyrics)
        audiofile.tag.save()
        ## need to generalize this now, how do i find the lyrics on google?
        
    


    

## use audiofile.save() to save changes 
