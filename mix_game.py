# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:37:16 2021

@author: asus
"""
import os
import fnmatch
import random
from pydub import AudioSegment
from pydub.playback import play
import subprocess



def get_music_list_and_sum():
    all_music=[]
    path = 'store'    #路徑
    for files in os.listdir(path):
        if fnmatch.fnmatch(files, '*.mp3'):
            all_music.append(files)
    return all_music,len(all_music)

def space_music():
    time_long =input('請輸入空白音時長 60000ms = 1m:')
    time_long = float(time_long)
    space_silence = AudioSegment.silent(duration =time_long)
    space_silence.export('store//00.wav', format="wav")
    file_name ='store//00.wav'
    subprocess.call('ffmpeg -y -i {} -vn -ar 44100 -ac 2 -ab 192k -f mp3 {}.mp3'.format(file_name,file_name[:-4]),shell=True)
   


   
    


def output_song(ref_list, n):
    sound1 = AudioSegment.from_mp3("store//"+ref_list[0])
    #round_n = random.randint(1, (n-1))想要混幾首
    append_list = random.sample(range(1, n ),3)
    for i in range(len(append_list)):
      print( ref_list[append_list[i]],"\t")  
      temp_music = AudioSegment.from_mp3("store/"+ ref_list[append_list[i]])
      sound1 = sound1.overlay(temp_music)
      sound1.export("mixed_sounds.mp3", format="mp3")
    
    print("mix_ok")
    play(sound1)
    os.system("pause")
    
    
   

def init_music(sound):
    dis = sound.apply_gain(-3.5)
    dis_via  = sound - 3.5
    return sound
    


if __name__ == '__main__':
    space_music()    
    get_list,num =get_music_list_and_sum()
    print(get_list, num)
    output_song(get_list, num)
    
    
    
    


