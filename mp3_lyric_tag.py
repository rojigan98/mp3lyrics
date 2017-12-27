## Author: Rojigan Gengatharan
## mp3_lyric_tag.py
## Start Date: December 23, 2017.
## make the final program an executable and not a python script (but you can inc##  that too, can try using pyinstaller)
## make it so that user decides what name of folder to receive lyrics for 


import eyed3
import os 
import requests
from bs4 import BeautifulSoup
import urllib.parse
from rauth import OAuth2Service

MAX_RETRIES = 20




def get_song_lyrics(my_song_link):
    if(lyrics_link != False):
        
        page = requests.get(lyrics_link)
        print(page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')

        mydivs = soup.find_all("div", { "class" : "lyrics" })
        lyrics = mydivs[0].get_text().lstrip()
        return lyrics
    else:
        return False

## after you can get the lyrics for any song then work on being able to iterate through all mp3's in the folder, and getting lyrics to each
def get_song_lyrics_link(song_name, song_title):
    return false






if __name__ == "__main__":

    music_folder = input("Which folder has all the songs you would like to add lyrics to? Alternatively, you can specify the path from this folder to the folder with those songs.  Note: All mp3 files in that folder will have lyrics added to it, if possible.\n")
    
    os.chdir(music_folder)


    ## need to set up genius api
    
    audiofile = eyed3.load("good_ass_intro.mp3")

    
    song_title  = audiofile.tag.title
    artist = audiofile.tag.artist

    
    client_id  = input("Enter genius api client id")
 


    secret_key = input("Enter genius api secret key")

    access_token = input("Enter genius api access token")


    

    url = 'https://api.genius.com/search?access_token=' + access_token + '&q=' + search_term
    genius = OAuth2Service(
        name='genius',
        consumer_key=client_id, #kinda yoloing this step
        consumer_secret=secret_key,
        
    

    ## lyrics_link = "https://genius.com/Chance-the-rapper-good-ass-intro-lyrics"


    
    lyrics = get_song_lyrics(lyrics_link)
        
        
    audiofile.tag.lyrics.set(lyrics)
    audiofile.tag.save()
