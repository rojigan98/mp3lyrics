# Author: Rojigan Gengatharan
# mp3_lyric_tag.py
# Start Date: December 23, 2017.
# make the final program an executable and not a python script (but you can inc##  that too, can try using pyinstaller)
# make it so that user decides what name of folder to receive lyrics for


import eyed3
import flask
import os 
import requests
import json
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

def get_song_lyrics_link(song_name, song_title):
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



    # need to set up genius api

    # USE GENIUS API READ THOSE GOOGLE TUTORIALS SO YOU UNDERSTAND HOW OAUTH2.0 ACTUALLY WORKS

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

    search_string = "Cocoa Butter Kisses".replace(" ", "%20").lower()
    search_url = "https://api.genius.com/search?q="
    

    # print(token_info.text + "\n")
    python_token_info = token_info.json()
    access_token = python_token_info["access_token"]
    r = requests.get((search_url + search_string),
                    headers = {'Authorization': ('Bearer ' + access_token)})
    print(r.json()["response"]["hits"][0])

    
    '''
    music_folder = input("\n" + "Which folder has all the songs you would like to add lyrics to?" +
                         " Alternatively, you can specify the path from this folder to the folder with those songs." +
                         " Note: All mp3 files in that folder will have lyrics added to it, if possible." + '\n')
    '''
    '''
    audiofile = eyed3.load("good_ass_intro.mp3")
    song_title  = audiofile.tag.title
    artist = audiofile.tag.artist
    # lyrics = get_song_lyrics(lyrics_link)
        
    # audiofile.tag.lyrics.set(lyrics)
    # audiofile.tag.save()
    '''
