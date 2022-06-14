#!/usr/bin/env python
# coding: utf-8

# In[74]:


from pydub import AudioSegment as audio
import tkinter as tk
from tkinter import filedialog, dialog
import os.path
import glob
import pygame as pg
import shutil
import threading
pg.mixer.init()


# In[75]:


files = audio.from_file("test_1.wav", "wave")
print(files)


# In[76]:


pg.mixer.init()
F = 'temp.wav'
G = 'output.mp3'
global pau
pau = False


# In[77]:


def load_file(load): 
    name = os.path.basename(load)
    root, extension = name.split(".")[0], name.split(".")[1]
    if (extension == 'wav'):
        file_load = audio.from_file(name, "wave")
    elif (extension == 'mp3'):
        file_load = audio.from_file(name, "mp3")
    shutil.copy(name, F)

def load():
    lo_path = filedialog.askopenfilename(title = "Choose Music", initialdir = 'C:\jupyter_notebook\numerical method\Final project')
    load_file(lo_path)  
    output_path.set(lo_path)   

def play1():  
    pg.mixer.music.load(F)
    pg.mixer.music.play()
    
def play2():  
    pg.mixer.music.load(G)
    pg.mixer.music.play()
        
def pause():
    global pau
    if pau == False:
        pau = True
        pg.mixer.music.pause()
    else:
        pau = False
        pg.mixer.music.unpause()   
    
def stop():
    pg.mixer.music.stop()
    
def dB_turn_up():
    up_file = audio.from_file(F, "wave")
    increase = text_increase.get('1.0', 'end-1c')
    increase_change = int(increase)
    in_file = up_file.apply_gain(increase_change)
    file_store_in = in_file.export(G, "mp3")
    output_change.set(f'Volume Increase file')
    
def dB_turn_down():
    down_file = audio.from_file(F, "wave")
    decrease = text_decrease.get('1.0', 'end-1c')
    decrease_change = int(decrease) * -1
    de_file = down_file.apply_gain(decrease_change)
    file_store_de = de_file.export(G, "mp3")
    output_change.set(f'Volume decrease file')  


# In[81]:


interface = tk.Tk()
interface.geometry('600x300')
interface.title('Volume Adjustment')

output_path = tk.StringVar()
botton_load = tk.Button(interface, text = "choose music", font = ('Arial', 10), command = load)
label_path = tk.Label(interface, textvariable = output_path, font = ('Arial', 10))
botton_load.place(x = 10, y = 10)
label_path.place(x = 120, y = 10)

label_current = tk.Label(interface, text = "Current File", font = ('Arial', 10))
botton_play = tk.Button(interface, text = "play", font = ('Arial', 10), command = play1)
botton_pause = tk.Button(interface, text = "pause", font = ('Arial', 10), command = pause)
botton_stop = tk.Button(interface, text = "stop", font = ('Arial', 10), command = stop)
label_current.place(x = 10, y = 75)
botton_play.place(x = 130, y = 70)
botton_pause.place(x = 200, y = 70)
botton_stop.place(x = 270, y = 70)

label_increase = tk.Label(interface, text = "Increase", font = ('Arial', 10))
label_decrease = tk.Label(interface, text = "/ decrease", font = ('Arial', 10))
text_increase = tk.Text(interface, width = 7, height = 2)
text_decrease = tk.Text(interface, width = 7, height = 2)
label_dB1 = tk.Label(interface, text = "dB", font = ('Arial', 10))
label_dB2 = tk.Label(interface, text = "dB", font = ('Arial', 10))
botton_click1 = tk.Button(interface, text = "click", font = ('Arial', 10), command = dB_turn_up)
botton_click2 = tk.Button(interface, text = "click", font = ('Arial', 10), command = dB_turn_down)
label_increase.place(x = 10, y = 140)
text_increase.place(x = 70, y = 137)
label_dB1.place(x = 130, y = 140)
botton_click1.place(x = 160, y = 140)
label_decrease.place(x = 225, y = 137)
text_decrease.place(x = 300, y = 137)
label_dB2.place(x = 360, y = 140)
botton_click2.place(x = 390, y = 137)

output_change = tk.StringVar()
label_change = tk.Label(interface, textvariable = output_change , font = ('Arial', 10))
botton_play_ch = tk.Button(interface, text = "play", font = ('Arial', 10), command = play2)
botton_pause_ch = tk.Button(interface, text = "pause", font = ('Arial', 10), command = pause)
botton_stop_ch = tk.Button(interface, text = "stop", font = ('Arial', 10), command = stop)
label_change.place(x = 10, y = 200)
botton_play_ch.place(x = 180, y = 200)
botton_pause_ch.place(x = 250, y = 200)
botton_stop_ch.place(x = 320, y = 200)


# In[82]:


interface.mainloop()