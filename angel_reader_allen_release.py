#===========================================================================#
#                                                                           #
#    AngelReader: An E-book & Audio-book Loader                             #
#    Copyright (C) 2018  D.A.E. (wayshower.de@gmail.com)                    #
#                                                                           #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or      #
#    (at your option) any later version.                                    #
#                                                                           #
#    This program is distributed in the hope that it will be useful,        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#    GNU General Public License for more details.                           #
#                                                                           #
#    You should have received a copy of the GNU General Public License      #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>. #
#                                                                           #
#===========================================================================#

#! Python 3.6

import tkinter as tk
from pygame import mixer

root = tk.Toplevel()
root.title("ANGEL READER | JAMES ALLEN LIBRARY 1")
root.iconbitmap('icons/angel_icon.ico')

def close(event=None):
    if root:
        root.grab_release()
        root.withdraw()

def open_lib():
    root.deiconify()
    root.tkraise()

def display_infos():    
    global txt_frame2, txt_frame, variable

    if variable.get() == "King James Version Of The Bible":
        bktitle = f_3
    elif variable.get() == "James Allen's As A Man Thinketh":
        bktitle = f_2
    elif variable.get() == "James Allen's All These Things Added":
        bktitle = f_1
    elif variable.get() == "James Allen's The Way Of Peace":
        bktitle = f_4
    elif variable.get() == "James Allen's Byways Of Blessedness":
        bktitle = f_1
      
    txt_frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    # Text widget for ebook infos
    info_txt = tk.Text(txt_frame2, height=30, width=70, wrap=tk.WORD, bg="khaki", font="Courier 12 bold")
    file_obj = open(bktitle, encoding="utf8")
    file_content = file_obj.read()
    file_obj.close()
    info_txt.insert(tk.END, file_content)
    info_txt.config(state=tk.DISABLED)
    info_txt.pack(side=tk.LEFT, fill=tk.X, padx=5)
    # Scrollbar widget for the Text widget
    scrollbar = tk.Scrollbar(txt_frame2, orient=tk.VERTICAL, command=info_txt.yview)
    scrollbar.pack()
    info_txt.configure(yscrollcommand=scrollbar.set)
    txt_frame2.pack(side=tk.TOP)
    

def display_book():
    global txt_frame1, txt_frame, variable
    
    if variable.get() == "King James Version Of The Bible": 
        bktitle = file_5
    elif variable.get() == "James Allen's As A Man Thinketh":
        bktitle = file_4
    elif variable.get() == "James Allen's All These Things Added":
        bktitle = file_1
    elif variable.get() == "James Allen's The Way Of Peace":
        bktitle = file_3
    elif variable.get() == "James Allen's Byways Of Blessedness":
        bktitle = file_2

    
    txt_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    # Text widget for the ebooks
    sh_txt = tk.Text(txt_frame, height=30, width=80, wrap=tk.WORD, bg="khaki", font="Courier 12 bold")
    file_obj = open(bktitle, encoding="utf8")
    file_content = file_obj.read()
    file_obj.close()
    sh_txt.insert(tk.END, file_content)
    sh_txt.config(state=tk.DISABLED)
    sh_txt.pack(side=tk.LEFT, fill=tk.X, padx=5)

    # Scrollbar widget for the Text widget
    xscrollbar = tk.Scrollbar(txt_frame)
    xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    yscrollbar = tk.Scrollbar(txt_frame)
    yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    sh_txt.configure(xscrollcommand=xscrollbar.set,
                     yscrollcommand=yscrollbar.set)
    sh_txt.pack(side=tk.LEFT, fill=tk.X, padx=5)
    txt_frame.pack(side=tk.TOP)

    xscrollbar.config(command=sh_txt.xview)
    yscrollbar.config(command=sh_txt.yview)
    
def push_button1():
    global txt_frame, button_1, button_2
    button_1 = True        
    if button_2 == True:
        txt_frame.destroy()
    else:
        pass
    if button_1 == True:
        txt_button.config(state='normal')        
        display_infos()
        gutenberg_button.config(state='disabled') 
        
def push_button2():
    global txt_frame2, button_1, button_2
    button_2 = True        
    if button_1 == True: 
        txt_frame2.destroy()
    else:
        pass
    if button_2 == True:
        gutenberg_button.config(state='normal')
        display_book()
        txt_button.config(state='disabled')

def push_button3():
    global music_title   

    if audio_var.get() == "James Allen's As A Man Thinketh 01":
        music_title = audio1
        play_audio()
    elif audio_var.get() == "James Allen's As A Man Thinketh 02":
        music_title = audio2
        play_audio()
    elif audio_var.get() == "James Allen's As A Man Thinketh 03":
        music_title = audio3
        play_audio()
    elif audio_var.get() == "James Allen's As A Man Thinketh 04":
        music_title = audio4
        play_audio()
    elif audio_var.get() == "James Allen's As A Man Thinketh 05":
        music_title = audio5
        play_audio()
    elif audio_var.get() == "James Allen's As A Man Thinketh 06":
        music_title = audio6
        play_audio()
    elif audio_var.get() == "James Allen's As A Man Thinketh 07":
        music_title = audio7
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 00":
        music_title = au_0
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 01":
        music_title = au_1
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 02":
        music_title = au_2
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 03":
        music_title = au_3
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 04":
        music_title = au_4
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 05":
        music_title = au_5
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 06":
        music_title = au_6
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 07":
        music_title = au_7
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 08":
        music_title = au_8
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 09":
        music_title = au_9
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 10":
        music_title = au_10
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 11":
        music_title = au_11
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 12":
        music_title = au_12
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 13":
        music_title = au_13
        play_audio()
    elif audio_var.get() == "James Allen's All These Things Added 14":
        music_title = au_14
        play_audio()


def play_audio():
    global music_title
    mixer.init()
    mixer.music.load(music_title)
    mixer.music.play()

def push_button4():
    mixer.music.stop()

def push_button5():
    mixer.music.pause()

def push_button6():
    mixer.music.unpause()
        

button_1 = False
button_2 = False
file_1 = 'ebooks/allen-added.txt'
file_2 = 'ebooks/allen-byways.txt'
file_3 = 'ebooks/allen-peace.txt'
file_4 = 'ebooks/allen-thinketh.txt'
file_5 = 'ebooks/kjv-bible.txt'

f_1 = 'infos/about_allen.txt'
f_2 = 'infos/as_a_man_thinketh_info.txt'
f_3 = 'infos/kjvinfo_2.txt'
f_4 = 'infos/way_of_peace_info.txt'

audio1 = "audiobooks/asamanthinketh_1_allen_64kb.mp3"
audio2 = "audiobooks/asamanthinketh_2_allen_64kb.mp3"
audio3 = "audiobooks/asamanthinketh_3_allen_64kb.mp3"
audio4 = "audiobooks/asamanthinketh_4_allen_64kb.mp3"
audio5 = "audiobooks/asamanthinketh_5_allen_64kb.mp3"
audio6 = "audiobooks/asamanthinketh_6_allen_64kb.mp3"
audio7 = "audiobooks/asamanthinketh_7_allen_64kb.mp3"

au_0 = "audiobooks/allthesethingsadded_00_allen_64kb.mp3"
au_1 = "audiobooks/allthesethingsadded_01_allen_64kb.mp3"
au_2 = "audiobooks/allthesethingsadded_02_allen_64kb.mp3"
au_3 = "audiobooks/allthesethingsadded_03_allen_64kb.mp3"
au_4 = "audiobooks/allthesethingsadded_04_allen_64kb.mp3"
au_5 = "audiobooks/allthesethingsadded_05_allen_64kb.mp3"
au_6 = "audiobooks/allthesethingsadded_06_allen_64kb.mp3"
au_7 = "audiobooks/allthesethingsadded_07_allen_64kb.mp3"
au_8 = "audiobooks/allthesethingsadded_08_allen_64kb.mp3"
au_9 = "audiobooks/allthesethingsadded_09_allen_64kb.mp3"
au_10 = "audiobooks/allthesethingsadded_10_allen_64kb.mp3"
au_11 = "audiobooks/allthesethingsadded_11_allen_64kb.mp3"
au_12 = "audiobooks/allthesethingsadded_12_allen_64kb.mp3"
au_13 = "audiobooks/allthesethingsadded_13_allen_64kb.mp3"
au_14 = "audiobooks/allthesethingsadded_14_allen_64kb.mp3"

# Frame for the decor pix
img_frame = tk.Frame(root, bd=3, relief=tk.SUNKEN)
img_frame.pack(fill=tk.Y, side=tk.LEFT, padx=2, pady=2)
image =['icons/lamp_flip.png']
img_label = tk.Label(img_frame, bd=2, relief=tk.RAISED)
img_label.pack(fill=tk.Y, side=tk.LEFT)
photo_image = tk.PhotoImage(file=image)
img_label['image'] = photo_image

# Ebooks buttons with frame
button_frame = tk.Frame(root, bd=2)
button_frame.pack(fill=tk.X, side=tk.BOTTOM)
gutenberg_button = tk.Button(button_frame, text='E-Book Infos', fg='red', bg='yellow green', disabledforeground='yellow', command=push_button1)
gutenberg_button.pack(fill=tk.X)
txt_button = tk.Button(button_frame, text='CLICK TO LOAD E-BOOK',
                       fg='white', bg='royalblue2', disabledforeground='green', command=push_button2)
txt_button.pack(fill=tk.X)

# Audio buttons with frame
audio_frame = tk.Frame(root, bd=2)
audio_frame.pack(side=tk.BOTTOM)
audio_button = tk.Button(audio_frame, text='CLICK TO LOAD AUDIO-BOOK',
                         fg='red', bg='seagreen1', command=push_button3)
audio_button.pack(fill=tk.X, side=tk.TOP)
stop_button = tk.Button(audio_frame, text='STOP', 
                        fg='white', bg='tan2', disabledforeground='purple3', command=push_button4)
stop_button.pack(side=tk.LEFT, ipadx=12)  # put inner paddings for balanced placement in the frame
pause_button = tk.Button(audio_frame, text='PAUSE', fg='white', bg='tan2', command=push_button5)
pause_button.pack(side=tk.LEFT, ipadx=4)
resume_button = tk.Button(audio_frame, text='RESUME', fg='white', bg='tan2', command=push_button6)
resume_button.pack(side=tk.LEFT)

# Option menu with Label
menu_frame = tk.Frame(root, bd=3, relief=tk.GROOVE)
menu_frame.pack(fill=tk.X, padx=2, pady=2)
variable = tk.StringVar(menu_frame)
variable.set("James Allen's As A Man Thinketh")  # default value
tk.Label(menu_frame, text="E-BOOKS MENU :").pack()
option = tk.OptionMenu(menu_frame, variable, "James Allen's As A Man Thinketh",
                       "James Allen's All These Things Added", "James Allen's The Way Of Peace",
                       "James Allen's Byways Of Blessedness", "King James Version Of The Bible")
option.pack()

# audio option menu with Label
menu_frame2 = tk.Frame(root, bd=3, relief=tk.GROOVE)
menu_frame2.pack(fill=tk.X, side=tk.BOTTOM, padx=2, pady=2)
audio_var = tk.StringVar(menu_frame2)
audio_var.set("James Allen's As A Man Thinketh 01")  # default value
tk.Label(menu_frame2, text="AUDIO-BOOKS MENU:").pack()
audio_option = tk.OptionMenu(menu_frame2, audio_var, "James Allen's As A Man Thinketh 01", "James Allen's As A Man Thinketh 02",
                             "James Allen's As A Man Thinketh 03", "James Allen's As A Man Thinketh 04", "James Allen's As A Man Thinketh 05",
                             "James Allen's As A Man Thinketh 06", "James Allen's As A Man Thinketh 07", "James Allen's All These Things Added 00",
                             "James Allen's All These Things Added 01", "James Allen's All These Things Added 02", "James Allen's All These Things Added 03",
                             "James Allen's All These Things Added 04", "James Allen's All These Things Added 05", "James Allen's All These Things Added 06",
                             "James Allen's All These Things Added 07", "James Allen's All These Things Added 08", "James Allen's All These Things Added 09",
                             "James Allen's All These Things Added 10", "James Allen's All These Things Added 11", "James Allen's All These Things Added 12",
                             "James Allen's All These Things Added 13", "James Allen's All These Things Added 14")


audio_option.pack(side=tk.BOTTOM)
root.protocol("WM_DELETE_WINDOW", close)  # Handles the use of the X button on the Toplevel taskbar

