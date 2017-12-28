# Author: Rojigan Gengatharan
# mp3_lyric_tag.py
# Start Date: December 23, 2017.
# make the final program an executable and not a python script (but you can inc##  that too, can try using pyinstaller)
# make it so that user decides what name of folder to receive lyrics for


import eyed3
import os 
import requests
from bs4 import BeautifulSoup
from rauth import OAuth2Service

MAX_RETRIES = 20

def get_song_lyrics(my_song_link):
    if my_song_link != False:
        
        page = requests.get(my_song_link)
        print(page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')

        mydivs = soup.find_all("div", { "class" : "lyrics" })
        song_lyrics = mydivs[0].get_text().lstrip()
        return song_lyrics
    else:
        return False

# after you can get the lyrics for any song then work on iteration for songs in general
def get_song_lyrics_link(song_name, song_title):
    return False


if __name__ == "__main__":

    music_folder = input("Which folder has all the songs you would like to add lyrics to?" +
                         "Alternatively, you can specify the path from this folder to the folder with those songs." +
                         "Note: All mp3 files in that folder will have lyrics added to it, if possible." + '\n')
    
    os.chdir(music_folder)

    # need to set up genius api

    # USE GENIUS API READ THOSE GOOGLE TUTORIALS SO YOU UNDERSTAND HOW OAUTH2.0 ACTUALLY WORKS

    # save client secret in local file on this computer

    my_consumer_key  = "jymJxl3NxzxFEQGZ5hvWWV7b5L0VNrojGSBVxfAGBmQCQ53F6oVIPhcxQ1Tk_2Ld"

    # if doesn't work check this secret key

    my_consumer_secret = open('secret.txt', 'r').read()
    my_consumer_secret = my_consumer_secret[:len(my_consumer_secret)-1:]
    my_request_token_url = 'https://api.genius.com/oauth/request_token'
    my_access_token_url = 'https://api.genius.com/oauth/access_token'
    my_authorize_url = 'https://api.genius.com/oauth/authorize'
    my_base_url = 'https://api.genius.com/'
    genius = OAuth2Service(
        name='genius',
        client_id = my_consumer_key,
        client_secret = my_consumer_secret,
        access_token_url = my_access_token_url,
        authorize_url = my_authorize_url,
        base_url = my_base_url
    )

    redirect_uri = 'http://example.com'
    # if doesn't work check scope
    params = {'scope': 'me', 'response_type': 'code',
              'redirect_uri': redirect_uri
              }
    

    audiofile = eyed3.load("good_ass_intro.mp3")
    song_title  = audiofile.tag.title
    artist = audiofile.tag.artist
    # lyrics = get_song_lyrics(lyrics_link)
        
    # audiofile.tag.lyrics.set(lyrics)
    # audiofile.tag.save()
