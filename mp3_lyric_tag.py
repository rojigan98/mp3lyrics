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
import urllib.parse

MAX_RETRIES = 20


## use google search/genius search API with search example: chance the rapper lyrics favorite song azlyrics, take out all brackets since prod datpiff and feat will mess with azlyrics

def get_song_lyrics(my_song_link):
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
        return lyrics
    else:
        return False

## after you can get the lyrics for any song then work on being able to iterate through all mp3's in the folder, and getting lyrics to each
def get_song_lyrics_link(song_name, song_title):
    






if __name__ == "__main__":

    ## TODO: Test if this path thing actually works, otherwise add your code in by splitting at the /, test if / even works in mac (and maybe windows)
    music_folder = input("Which folder has all the songs you would like to add lyrics to? Alternatively, you can specify the path from this folder to the folder with those songs.  Note: All mp3 files in that folder will have lyrics added to it, if possible.\n")
    
    os.chdir(music_folder)
    
    audiofile = eyed3.load("good_ass_intro.mp3")

  

    song_title  = audiofile.tag.title
    artist = audiofile.tag.artist

    #lyrics_link = get_lyrics_link(song_title, artist)
    #work on getting one song working then generalize the case using the google search api and test for that
    lyrics_link = "https://genius.com/Chance-the-rapper-good-ass-intro-lyrics"


    ## need to set up genius api
    ## THIS IS JUST THE TOKEN
    genius_token = "JjVbw2WmoW5jYxQGG7uPAqu4og62hfBUZz67QpVte4XFMuQf1qHBJ4VlEE9162FZ"
   
    lyrics = get_song_lyrics(lyrics_link)
        
        
    audiofile.tag.lyrics.set(lyrics)
    audiofile.tag.save()
    ## need to generalize this now, how do i find the lyrics on google?
        
    


    

## use audiofile.save() to save changes 
