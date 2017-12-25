## Author: Rojigan Gengatharan
## mp3_lyric_tag.py
## December 23, 2017.
## make the final program an executable and not a python script (but you can inc##  that too, can try using pyinstaller)
## make it so that user decides what name of folder to receive lyrics for 

import eyed3
import os 
import requests


## Strategy to avoid imperfect metadata, do an azlyrics for the full artist and
## song name, if that doesn't work shorten song name as much as possible one set of words at a time, if you get empty string, then go back to og string and shorten the artist name (usually isn't messed though)
## if this takes too long, assume song title name is fine, but shouldn't take mroe than two days

def get_lyrics_link(my_song_name, my_artist):
    my_artist = "".join(my_artist.lower().split())
    website_link = "https://www.azlyrics.com/lyrics/" + my_artist + "/"
     
    my_song_name = my_song_name.lower()
    words_in_song_name = my_song_name.split()
    #check just song name first
    for words_kept in range(len(words_in_song_name), 0, -1):
        word_to_check = "".join(words_in_song_name[0:words_kept])
        my_link = website_link + word_to_check + ".html"
        page = requests.get(my_link)
        ## do I have to have an else clause?
        if (str(page.status_code)[0] ==  2):
            return my_link


    return false 
            


os.chdir("test_music")

audiofile = eyed3.load("favorite_song.mp3")

audiofile.tag.lyrics.set(u"Dragon Ball Super Opening 2 hit dragon ball hit vegeta vs jiren super saiyan god super saiyan")
audiofile.tag.save()

song_title  = audiofile.tag.title
artist = audiofile.tag.artist

lyrics_link = get_lyrics_link(song_title, artist)

if(lyrics_link != false):
    



## TODO: Need to configure web scraper
## TODO: Need to search for song on google to get proper song name, if metadata is faulty

## use audiofile.save() to save changes 
