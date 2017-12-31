# Author: Rojigan Gengatharan
# mp3_lyric_tag.py
# Start Date: December 23, 2017.

import eyed3
import flask
import os 
import requests
import json
from bs4 import BeautifulSoup
from rauth import OAuth2Service

MAX_RETRIES = 20

def truncate_title(song_title):
    # song_title = (song_title.lower()).replace(" ", "%20")
    false_song_title = song_title.lower()
    if len(song_title) >= 1:
        for i in range(0, len(song_title)):
            if false_song_title[i] == "(" or false_song_title[i] == ")":
                song_title = song_title[:i:]
                break 
    if len(song_title) >= 9:
        for i in range(0, len(song_title)):
            if false_song_title[i:i+8] == "explicit":
                song_title = song_title[:i:]
                break
    if len(song_title) >= 4:
         for i in range(0, len(song_title)):
            if false_song_title[i:i+5] == "feat.":
                song_title = song_title[:i:]
                break
    if len(song_title) >= 3:
         for i in range(0, len(song_title)):
            if false_song_title[i:i+3] == "ft.":
                song_title = song_title[:i:]
                break  
    print(song_title)
    return song_title


def get_song_lyrics(my_song_link):
    if my_song_link != False:
        
        page = requests.get(my_song_link)
        print(page.status_code) #just for debugging and testing
        soup = BeautifulSoup(page.content, 'html.parser')

        mydivs = soup.find_all("div", { "class" : "lyrics" })
        song_lyrics = mydivs[0].get_text().lstrip()
        print(song_lyrics)
        return song_lyrics
    else:
        return ""

def get_song_lyrics_link(song_artist, song_title, access_token, search_url):
    print(song_title)
    song_title = truncate_title(song_title)
    first_word = song_title.split(" ")[0].lower()
    title_length = len(song_title.split(" "))
    print(title_length)
    print("The first word of the title is", first_word)
    if (title_length  > 1):
        second_word = song_title.split(" ")[1].lower()
        print("The second word of the title is", second_word)
    search_string = (truncate_title(song_title) + " " + song_artist).replace(" ", "%20").lower()
    print("This is the search string", search_string)
    r = requests.get((search_url + search_string),
                    headers = {'Authorization': ('Bearer ' + access_token)})
    hits = r.json()["response"]["hits"]
    for i in range(min(len(hits), 5)):
        if first_word in hits[i]["result"]["url"].lower():
            if title_length > 1:
                if second_word in hits[i]["result"]["url"].lower():
                    return hits[i]["result"]["url"]
                    #check if first word in title is in here, then proceed, otherwise don't
            else:   
                return hits[i]["result"]["url"]
                         
    return False 

    

def get_authorize_code(authorize_code_url):
    for i in range(0, len(authorize_code_url)):
        if authorize_code_url[i] == '?':
            authorize_code_url = authorize_code_url[i+6::]
            break
        
        #since after ? in redirect uri there is "code="
    for i in range(0, len(authorize_code_url) - 1):
        if authorize_code_url[i] == '&':
            return authorize_code_url[:i:]
    return authorize_code_url

if __name__ == "__main__":



    # save client secret in local file on this computer

    my_consumer_key = "jymJxl3NxzxFEQGZ5hvWWV7b5L0VNrojGSBVxfAGBmQCQ53F6oVIPhcxQ1Tk_2Ld"

    # if doesn't work check this secret key

    my_consumer_secret = open('secret.txt', 'r').read()
    my_consumer_secret = my_consumer_secret[:len(my_consumer_secret)-1:]
    my_request_token_url = 'https://api.genius.com/oauth/request_token'
    my_access_token_url = 'https://api.genius.com/oauth/access_token'
    my_authorize_url = 'https://api.genius.com/oauth/authorize'
    my_base_url = 'https://api.genius.com/'
    
    genius =  OAuth2Service(
        client_id=my_consumer_key,
        client_secret=my_consumer_secret,
        name='genius',
        authorize_url=my_authorize_url,
        access_token_url=my_access_token_url,
        base_url=my_base_url)

    redirect_uri = 'https://example.com'
    params = {'scope': 'me', 'response_type': 'code', 'state': 'ssg',
              'redirect_uri': redirect_uri}

    url = genius.get_authorize_url(**params)
    authorize_code_url = input("\nPlease visit the following link \n" + url +
                           "\nto authorize the session. Then paste the " +
                           "url you are redirected to. Then press enter \n")
    authorize_code = get_authorize_code(authorize_code_url)

    my_data = {'code': authorize_code, 'client_secret': my_consumer_secret,
               'grant_type': 'authorization_code', 'client_id': my_consumer_key,
               'redirect_uri': redirect_uri, 'response_type': 'code'}

    token_info = requests.post("https://api.genius.com/oauth/token", data=my_data)

    python_token_info = token_info.json()
    access_token = python_token_info["access_token"]
    search_url = "https://api.genius.com/search?q="

    music_folder = input("\n" + "Which folder has all the songs you would like to add lyrics to?" +
                         " Alternatively, you can specify the path from this folder to the folder with those songs." +
                         " Note: All mp3 files in that folder will have lyrics added to it, if possible." + '\n')


    for filename in os.listdir(music_folder):
        if filename.endswith(".mp3"):
            audiofile = eyed3.load(os.path.join(music_folder, filename))
            song_title  = audiofile.tag.title
            artist = audiofile.tag.artist
            print(artist)
            lyrics_link = get_song_lyrics_link(artist, song_title, access_token, search_url)
            print(lyrics_link)
            lyrics = get_song_lyrics(lyrics_link)
            audiofile.tag.lyrics.set(lyrics)
            audiofile.tag.save()

