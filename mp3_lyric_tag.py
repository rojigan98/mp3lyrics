## Author: Rojigan Gengatharan
## mp3_lyric_tag.py
## December 23, 2017.
## make the final program an executable and not a python script (but you can inc##  that too, can try using pyinstaller)
## make it so that user decides what name of folder to receive lyrics for 


import eyed3
import os 

os.chdir("test_music")





audiofile = eyed3.load("ultralight_beam.mp3")

## use audiofile.save() to save changes 
