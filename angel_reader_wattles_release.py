#---------------------------------------------------------------------------#
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
#---------------------------------------------------------------------------#

#! Python 3.6

import tkinter as tk
from pygame import mixer

root = tk.Toplevel()
root.title("ANGEL READER | W.D. WATTLES LIBRARY")
root.iconbitmap('icons/angel_icon.ico')

# Functions initialized
def close(event=None):
    if root:
        root.grab_release()
        root.withdraw()

def open_lib():
    root.deiconify()
    root.tkraise()

def display_infos():    
    global txt_frame2, txt_frame, variable


    if variable.get() == "Ralph Waldo Trine - In Tune With The Infinite" :
        bktitle = f_3w
    elif variable.get() == "Wallace D. Wattles - The Science Of Getting Rich":
        bktitle = f_4w
    elif variable.get() == "Wallace D. Wattles - The Science Of Being Great":
        bktitle = f_5w
    elif variable.get() == "Wallace D. Wattles - The Science Of Being Well":
        bktitle = f_8w
    elif variable.get() == "Herman Hesse - Siddharta":
        bktitle = f_9w
    elif variable.get() == "Marcus Aurelius - Meditations" :
        bktitle = f_10w
    elif variable.get() == "Walt Whitman - Leaves Of Grass" :
        bktitle = f_11w
    elif variable.get() == "Harriet Beecher Stowe - Uncle Tom's Cabin":
        bktitle = f_12w
    elif variable.get() == "The Autobiography Of Benjamin Franklin" :
        bktitle = f_13w
    elif variable.get() == "Ralph Waldo Emerson - Essays":
        bktitle = f_14w

    
    txt_frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    # Text widget for ebook infos
    info_txt = tk.Text(txt_frame2, height=30, width=70, wrap=tk.WORD, bg='khaki', font="Courier 12 bold" )
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
    global txt_frame, variable

    if variable.get() == "Ralph Waldo Trine - In Tune With The Infinite" :
        bktitle = file_3w
    elif variable.get() == "Wallace D. Wattles - The Science Of Getting Rich":
        bktitle = file_4w
    elif variable.get() == "Wallace D. Wattles - The Science Of Being Great":
        bktitle = file_5w
    elif variable.get() == "Wallace D. Wattles - The Science Of Being Well":
        bktitle = file_8w
    elif variable.get() == "Herman Hesse - Siddharta" :
        bktitle = file_9w
    elif variable.get() == "Marcus Aurelius - Meditations" :
        bktitle = file_10w
    elif variable.get() == "Walt Whitman - Leaves Of Grass" :
        bktitle = file_11w
    elif variable.get() == "Harriet Beecher Stowe - Uncle Tom's Cabin" :
        bktitle = file_12w
    elif variable.get() == "The Autobiography Of Benjamin Franklin":
        bktitle = file_13w
    elif variable.get() == "Ralph Waldo Emerson - Essays" :
        bktitle = file_14w

        
    
    txt_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    # Text widget for the ebooks
    sh_txt = tk.Text(txt_frame, height=30, width=80, wrap=tk.WORD, bg='khaki', font="Courier 12 bold")
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
    
def infos_button_clicked():
    global txt_frame, infos_button_ON, ebooks_button_ON
    infos_button_ON = True        
    if ebooks_button_ON == True:
        txt_frame.destroy()
    else:
        pass
    if infos_button_ON == True:
        txt_button.config(state='normal')        
        display_infos()
        gutenberg_button.config(state='disabled') 
        
def ebooks_button_clicked():
    global txt_frame2, infos_button_ON, ebooks_button_ON
    ebooks_button_ON = True        
    if infos_button_ON == True: 
        txt_frame2.destroy()
    else:
        pass
    if ebooks_button_ON == True:
        gutenberg_button.config(state='normal')
        display_book()
        txt_button.config(state='disabled')

def audiobooks_button_clicked():
    global music_title   
    if audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 00":
        music_title = au_0w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 01":
        music_title = au_1w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 02":
        music_title = au_2w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 03":
        music_title = au_3w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 04":
        music_title = au_4w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 05":
        music_title = au_5w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 06":
        music_title = au_6w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 07":
        music_title = au_7w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 08":
        music_title = au_8w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 09":
        music_title = au_9w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 10":
        music_title = au_10w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 11":
        music_title = au_11w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 12":
        music_title = au_12w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 13":
        music_title = au_13w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 14":
        music_title = au_14w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 15":
        music_title = au_15w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 16":
        music_title = au_16w
        play_audio()
    elif audio_var.get() == "Wallace D. Wattles' Science Of Getting Rich 17":
        music_title = au_17w
        play_audio()

def play_audio():
    global music_title
    mixer.init()
    mixer.music.load(music_title)
    mixer.music.play()

def stop_button_clicked():
    mixer.music.stop()

def pause_button_clicked():
    mixer.music.pause()

def resume_button_clicked():
    mixer.music.unpause()
        

infos_button_ON = False
ebooks_button_ON = False

# Text files       
file_3w = 'ebooks/trine-tune.txt'                                            
file_4w = 'ebooks/wattles-getting_rich.txt'
file_5w = 'ebooks/wattles-being_great.txt'                            
file_8w = 'ebooks/wattles-being_well.txt'                                      
file_9w = 'ebooks/hesse-siddharta.txt'                                            
file_10w = 'ebooks/aurelius-meditations.txt'                            
file_11w = 'ebooks/whitman-leaves.txt'                 
file_12w = 'ebooks/stowe-cabin.txt'                 
file_13w = 'ebooks/franklin-autobiography.txt' 
file_14w = 'ebooks/emerson-essays.txt'       

f_3w = 'infos/info_3w.txt'
f_4w = 'infos/getting_rich_infos.txt'
f_5w = 'infos/being_great_infos.txt'
f_8w = 'infos/being_well_infos.txt'
f_9w = 'infos/info_9w.txt'
f_10w = 'infos/info_10w.txt'
f_11w = 'infos/info_11w.txt'
f_12w = 'infos/info_12w.txt'
f_13w = 'infos/info_13w.txt'
f_14w = 'infos/info_14w.txt'

# Audio files
au_0w = "audiobooks/scienceofgettingrich_00_wattles_64kb.mp3"
au_1w = "audiobooks/scienceofgettingrich_01_wattles_64kb.mp3"
au_2w = "audiobooks/scienceofgettingrich_02_wattles_64kb.mp3"
au_3w = "audiobooks/scienceofgettingrich_03_wattles_64kb.mp3"
au_4w = "audiobooks/scienceofgettingrich_04_wattles_64kb.mp3"
au_5w = "audiobooks/scienceofgettingrich_05_wattles_64kb.mp3"
au_6w = "audiobooks/scienceofgettingrich_06_wattles_64kb.mp3"
au_7w = "audiobooks/scienceofgettingrich_07_wattles_64kb.mp3"
au_8w = "audiobooks/scienceofgettingrich_08_wattles_64kb.mp3"
au_9w = "audiobooks/scienceofgettingrich_09_wattles_64kb.mp3"
au_10w = "audiobooks/scienceofgettingrich_10_wattles_64kb.mp3"
au_11w = "audiobooks/scienceofgettingrich_11_wattles_64kb.mp3"
au_12w = "audiobooks/scienceofgettingrich_12_wattles_64kb.mp3"
au_13w = "audiobooks/scienceofgettingrich_13_wattles_64kb.mp3"
au_14w = "audiobooks/scienceofgettingrich_14_wattles_64kb.mp3"
au_15w = "audiobooks/scienceofgettingrich_15_wattles_64kb.mp3"
au_16w = "audiobooks/scienceofgettingrich_16_wattles_64kb.mp3"
au_17w = "audiobooks/scienceofgettingrich_17_wattles_64kb.mp3"

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
gutenberg_button = tk.Button(button_frame, text='E-Book Infos', fg='red',
                             bg='yellow green', disabledforeground='yellow', command=infos_button_clicked)
gutenberg_button.pack(fill=tk.X)
txt_button = tk.Button(button_frame, text='CLICK TO LOAD E-BOOK',
                       fg='white', bg='royalblue2', disabledforeground='green', command=ebooks_button_clicked)
txt_button.pack(fill=tk.X)

# Audio buttons with frame
audio_frame = tk.Frame(root, bd=2)
audio_frame.pack(side=tk.BOTTOM)
audio_button = tk.Button(audio_frame, text='CLICK TO LOAD AUDIO-BOOK',
                         fg='red', bg='seagreen1', command=audiobooks_button_clicked)
audio_button.pack(fill=tk.X, side=tk.TOP)
stop_button = tk.Button(audio_frame, text='STOP', 
                        fg='white', bg='tan2', disabledforeground='purple3', command=stop_button_clicked)
stop_button.pack(side=tk.LEFT, ipadx=12)  # put inner paddings for balanced placement in the frame
pause_button = tk.Button(audio_frame, text='PAUSE', fg='white', bg='tan2', command=pause_button_clicked)
pause_button.pack(side=tk.LEFT, ipadx=4)
resume_button = tk.Button(audio_frame, text='RESUME', fg='white', bg='tan2', command=resume_button_clicked)
resume_button.pack(side=tk.LEFT)

# Option menu with Label
menu_frame = tk.Frame(root, bd=3, relief=tk.GROOVE)
menu_frame.pack(fill=tk.X, padx=2, pady=2)
variable = tk.StringVar(menu_frame)
variable.set("Ralph Waldo Trine - In Tune With The Infinite")  # default value
tk.Label(menu_frame, text="E-BOOKS MENU :").pack()
option = tk.OptionMenu(menu_frame, variable, "Ralph Waldo Trine - In Tune With The Infinite",
                             "Wallace D. Wattles - The Science Of Getting Rich", "Wallace D. Wattles - The Science Of Being Great",
                             "Wallace D. Wattles - The Science Of Being Well", "Herman Hesse - Siddharta", "Marcus Aurelius - Meditations",
                             "Walt Whitman - Leaves Of Grass", "Harriet Beecher Stowe - Uncle Tom's Cabin",
                             "The Autobiography Of Benjamin Franklin", "Ralph Waldo Emerson - Essays")
option.pack()

# audio option menu with Label
menu_frame2 = tk.Frame(root, bd=3, relief=tk.GROOVE)
menu_frame2.pack(fill=tk.X, side=tk.BOTTOM, padx=2, pady=2)
audio_var = tk.StringVar(menu_frame2)
audio_var.set("Wallace D. Wattles' Science Of Getting Rich 00")  # default value
tk.Label(menu_frame2, text="AUDIO-BOOKS MENU:").pack()
audio_option = tk.OptionMenu(menu_frame2, audio_var, "Wallace D. Wattles' Science Of Getting Rich 00", "Wallace D. Wattles' Science Of Getting Rich 01",
                             "Wallace D. Wattles' Science Of Getting Rich 02", "Wallace D. Wattles' Science Of Getting Rich 03",
                             "Wallace D. Wattles' Science Of Getting Rich 04", "Wallace D. Wattles' Science Of Getting Rich 05",
                             "Wallace D. Wattles' Science Of Getting Rich 06", "Wallace D. Wattles' Science Of Getting Rich 07",
                             "Wallace D. Wattles' Science Of Getting Rich 08", "Wallace D. Wattles' Science Of Getting Rich 09",
                             "Wallace D. Wattles' Science Of Getting Rich 10", "Wallace D. Wattles' Science Of Getting Rich 11",
                             "Wallace D. Wattles' Science Of Getting Rich 12", "Wallace D. Wattles' Science Of Getting Rich 13",
                             "Wallace D. Wattles' Science Of Getting Rich 14", "Wallace D. Wattles' Science Of Getting Rich 15",
                             "Wallace D. Wattles' Science Of Getting Rich 16", "Wallace D. Wattles' Science Of Getting Rich 17")
audio_option.pack(side=tk.BOTTOM)
root.protocol("WM_DELETE_WINDOW", close)
