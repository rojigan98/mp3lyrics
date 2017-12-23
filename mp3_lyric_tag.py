## Author: Rojigan Gengatharan
## mp3_lyric_tag.py
## December 23, 2017.
## make the final program an executable and not a python script (but you can inc##  that too, can try using pyinstaller)


import eyed3
import os 

os.chdir("test_music")

audiofile = eyed3.load("favorite_song.mp3")

print(audiofile.tag.artist)
print(audiofile.tag.album)
