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
# Angel Reader (An Ebook and Audiobook Loader)
import tkinter as tk
from pygame import mixer

root = tk.Toplevel()
root.title("ANGEL READER | KJV NEW TESTAMENT COLLECTION")
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

    if variable.get() == "King James Version Of The Bible":
        bktitle = f_1t
    elif variable.get() == "Ang Biblia (1905)":
        bktitle = f_2t
    elif variable.get() == "Douay-Rheims Version Of The Bible":
        bktitle = f_3t
    
    txt_frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    # Text widget for ebook infos
    info_txt = tk.Text(txt_frame2, bg='khaki', wrap=tk.WORD, height=30, width=70, font='Courier 12 bold')
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
        bktitle = file_1t
    elif variable.get() == "Ang Biblia (1905)":
        bktitle = file_2t
    elif variable.get() == "Douay-Rheims Version Of The Bible":
        bktitle = file_3t

    
    txt_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    # Text widget for the ebooks
    sh_txt = tk.Text(txt_frame, wrap=tk.WORD, height=30, width=80,
                     fg='black', bg='khaki', font='Courier 12 bold')
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
    global audio_title   
    if audio_var.get() == 'Matthew 1':
        audio_title = a1
        play_audio()
    elif audio_var.get() == 'Matthew 2':
        audio_title = a2
        play_audio()
    elif audio_var.get() == 'Matthew 3':
        audio_title = a3
        play_audio()
    elif audio_var.get() == 'Matthew 4':
        audio_title = a4
        play_audio()
    elif audio_var.get() == 'Matthew 5':
        audio_title = a5
        play_audio()
    elif audio_var.get() == 'Matthew 6':
        audio_title = a6
        play_audio()
    elif audio_var.get() == 'Matthew 7':
        audio_title = a7
        play_audio()
    elif audio_var.get() == 'Matthew 8':
        audio_title = a8
        play_audio()
    elif audio_var.get() == 'Matthew 9':
        audio_title = a9
        play_audio()
    elif audio_var.get() == 'Matthew 10':
        audio_title = a10
        play_audio()
    elif audio_var.get() == 'Matthew 11':
        audio_title = a11
        play_audio()
    elif audio_var.get() == 'Matthew 12':
        audio_title = a12
        play_audio()
    elif audio_var.get() == 'Matthew 13':
        audio_title = a13
        play_audio()
    elif audio_var.get() == 'Matthew 14':
        audio_title = a14
        play_audio()
    elif audio_var.get() == 'Matthew 15':
        audio_title = a15
        play_audio()
    elif audio_var.get() == 'Matthew 16':
        audio_title = a16
        play_audio()
    elif audio_var.get() == 'Matthew 17':
        audio_title = a17
        play_audio()
    elif audio_var.get() == 'Matthew 18':
        audio_title = a18
        play_audio()
    elif audio_var.get() == 'Matthew 19':
        audio_title = a19
        play_audio()
    elif audio_var.get() == 'Matthew 20':
        audio_title = a20
        play_audio()
    elif audio_var.get() == 'Matthew 21':
        audio_title = a21
        play_audio()
    elif audio_var.get() == 'Matthew 22':
        audio_title = a22
        play_audio()
    elif audio_var.get() == 'Matthew 23':
        audio_title = a23
        play_audio()
    elif audio_var.get() == 'Matthew 24':
        audio_title = a24
        play_audio()
    elif audio_var.get() == 'Matthew 25':
        audio_title = a25
        play_audio()
    elif audio_var.get() == 'Matthew 26':
        audio_title = a26
        play_audio()
    elif audio_var.get() == 'Matthew 27':
        audio_title = a27
        play_audio()
    elif audio_var.get() == 'Matthew 28':
        audio_title = a28
        play_audio()
    elif audio_var.get() == 'Mark 1':
        audio_title = b1
        play_audio()
    elif audio_var.get() == 'Mark 2':
        audio_title = b2
        play_audio()
    elif audio_var.get() == 'Mark 3':
        audio_title = b3
        play_audio()
    elif audio_var.get() == 'Mark 4':
        audio_title = b4
        play_audio()
    elif audio_var.get() == 'Mark 5':
        audio_title = b5
        play_audio()
    elif audio_var.get() == 'Mark 6':
        audio_title = b6
        play_audio()
    elif audio_var.get() == 'Mark 7':
        audio_title = b7
        play_audio()
    elif audio_var.get() == 'Mark 8':
        audio_title = b8
        play_audio()
    elif audio_var.get() == 'Mark 9':
        audio_title = b9
        play_audio()
    elif audio_var.get() == 'Mark 10':
        audio_title = b10
        play_audio()
    elif audio_var.get() == 'Mark 11':
        audio_title = b11
        play_audio()
    elif audio_var.get() == 'Mark 12':
        audio_title = b12
        play_audio()
    elif audio_var.get() == 'Mark 13':
        audio_title = b13
        play_audio()
    elif audio_var.get() == 'Mark 14':
        audio_title = b14
        play_audio()
    elif audio_var.get() == 'Mark 15':
        audio_title = b15
        play_audio()
    elif audio_var.get() == 'Mark 16':
        audio_title = b16
        play_audio()
    elif audio_var.get() == 'Luke 1':
        audio_title = c1
        play_audio()
    elif audio_var.get() == 'Luke 2':
        audio_title = c2
        play_audio()
    elif audio_var.get() == 'Luke 3':
        audio_title = c3
        play_audio()
    elif audio_var.get() == 'Luke 4':
        audio_title = c4
        play_audio()
    elif audio_var.get() == 'Luke 5':
        audio_title = c5
        play_audio()
    elif audio_var.get() == 'Luke 6':
        audio_title = c6
        play_audio()
    elif audio_var.get() == 'Luke 7':
        audio_title = c7
        play_audio()
    elif audio_var.get() == 'Luke 8':
        audio_title = c8
        play_audio()
    elif audio_var.get() == 'Luke 9':
        audio_title = c9
        play_audio()
    elif audio_var.get() == 'Luke 10':
        audio_title = c10
        play_audio()
    elif audio_var.get() == 'Luke 11':
        audio_title = c11
        play_audio()
    elif audio_var.get() == 'Luke 12':
        audio_title = c12
        play_audio()
    elif audio_var.get() == 'Luke 13':
        audio_title = c13
        play_audio()
    elif audio_var.get() == 'Luke 14':
        audio_title = c14
        play_audio()
    elif audio_var.get() == 'Luke 15':
        audio_title = c15
        play_audio()
    elif audio_var.get() == 'Luke 16':
        audio_title = c16
        play_audio()
    elif audio_var.get() == 'Luke 17':
        audio_title = c17
        play_audio()
    elif audio_var.get() == 'Luke 18':
        audio_title = c18
        play_audio()
    elif audio_var.get() == 'Luke 19':
        audio_title = c19
        play_audio()
    elif audio_var.get() == 'Luke 20':
        audio_title = c20
        play_audio()
    elif audio_var.get() == 'Luke 21':
        audio_title = c21
        play_audio()
    elif audio_var.get() == 'Luke 22':
        audio_title = c22
        play_audio()
    elif audio_var.get() == 'Luke 23':
        audio_title = c23
        play_audio()
    elif audio_var.get() == 'Luke 24':
        audio_title = c24
        play_audio()
    elif audio_var.get() == 'John 1':
        audio_title = d1
        play_audio()
    elif audio_var.get() == 'John 2':
        audio_title = d2
        play_audio()
    elif audio_var.get() == 'John 3':
        audio_title = d3
        play_audio()
    elif audio_var.get() == 'John 4':
        audio_title = d4
        play_audio()
    elif audio_var.get() == 'John 5':
        audio_title = d5
        play_audio()
    elif audio_var.get() == 'John 6':
        audio_title = d6
        play_audio()
    elif audio_var.get() == 'John 7':
        audio_title = d7
        play_audio()
    elif audio_var.get() == 'John 8':
        audio_title = d8
        play_audio()
    elif audio_var.get() == 'John 9':
        audio_title = d9
        play_audio()
    elif audio_var.get() == 'John 10':
        audio_title = d10
        play_audio()
    elif audio_var.get() == 'John 11':
        audio_title = d11
        play_audio()
    elif audio_var.get() == 'John 12':
        audio_title = d12
        play_audio()
    elif audio_var.get() == 'John 13':
        audio_title = d13
        play_audio()
    elif audio_var.get() == 'John 14':
        audio_title = d14
        play_audio()
    elif audio_var.get() == 'John 15':
        audio_title = d15
        play_audio()
    elif audio_var.get() == 'John 16':
        audio_title = d16
        play_audio()
    elif audio_var.get() == 'John 17':
        audio_title = d17
        play_audio()
    elif audio_var.get() == 'John 18':
        audio_title = d18
        play_audio()
    elif audio_var.get() == 'John 19':
        audio_title = d19
        play_audio()
    elif audio_var.get() == 'John 20':
        audio_title = d20
        play_audio()
    elif audio_var.get() == 'John 21':
        audio_title = d21
        play_audio()
    elif audio_var.get() == 'Acts 1':
        audio_title = e1
        play_audio()
    elif audio_var.get() == 'Acts 2':
        audio_title = e2
        play_audio()
    elif audio_var.get() == 'Acts 3':
        audio_title = e3
        play_audio()
    elif audio_var.get() == 'Acts 4':
        audio_title = e4
        play_audio()
    elif audio_var.get() == 'Acts 5':
        audio_title = e5
        play_audio()
    elif audio_var.get() == 'Acts 6':
        audio_title = e6
        play_audio()
    elif audio_var.get() == 'Acts 7':
        audio_title = e7
        play_audio()
    elif audio_var.get() == 'Acts 8':
        audio_title = e8
        play_audio()
    elif audio_var.get() == 'Acts 9':
        audio_title = e9
        play_audio()
    elif audio_var.get() == 'Acts 10':
        audio_title = e10
        play_audio()
    elif audio_var.get() == 'Acts 11':
        audio_title = e11
        play_audio()
    elif audio_var.get() == 'Acts 12':
        audio_title = e12
        play_audio()
    elif audio_var.get() == 'Acts 13':
        audio_title = e13
        play_audio()
    elif audio_var.get() == 'Acts 14':
        audio_title = e14
        play_audio()
    elif audio_var.get() == 'Acts 15':
        audio_title = e15
        play_audio()
    elif audio_var.get() == 'Acts 16':
        audio_title = e16
        play_audio()
    elif audio_var.get() == 'Acts 17':
        audio_title = e17
        play_audio()
    elif audio_var.get() == 'Acts 18':
        audio_title = e18
        play_audio()
    elif audio_var.get() == 'Acts 19':
        audio_title = e19
        play_audio()
    elif audio_var.get() == 'Acts 20':
        audio_title = e20
        play_audio()
    elif audio_var.get() == 'Acts 21':
        audio_title = e21
        play_audio()
    elif audio_var.get() == 'Acts 22':
        audio_title = e22
        play_audio()
    elif audio_var.get() == 'Acts 23':
        audio_title = e23
        play_audio()
    elif audio_var.get() == 'Acts 24':
        audio_title = e24
        play_audio()
    elif audio_var.get() == 'Acts 25':
        audio_title = e25
        play_audio()
    elif audio_var.get() == 'Acts 26':
        audio_title = e26
        play_audio()
    elif audio_var.get() == 'Acts 27':
        audio_title = e27
        play_audio()
    elif audio_var.get() == 'Acts 28':
        audio_title = e28
        play_audio()
    elif audio_var.get() == 'Romans 1':
        audio_title = f1
        play_audio()
    elif audio_var.get() == 'Romans 2':
        audio_title = f2
        play_audio()
    elif audio_var.get() == 'Romans 3':
        audio_title = f3
        play_audio()
    elif audio_var.get() == 'Romans 4':
        audio_title = f4
        play_audio()
    elif audio_var.get() == 'Romans 5':
        audio_title = f5
        play_audio()
    elif audio_var.get() == 'Romans 6':
        audio_title = f6
        play_audio()
    elif audio_var.get() == 'Romans 7':
        audio_title = f7
        play_audio()
    elif audio_var.get() == 'Romans 8':
        audio_title = f8
        play_audio()
    elif audio_var.get() == 'Romans 9':
        audio_title = f9
        play_audio()
    elif audio_var.get() == 'Romans 10':
        audio_title = f10
        play_audio()
    elif audio_var.get() == 'Romans 11':
        audio_title = f11
        play_audio()
    elif audio_var.get() == 'Romans 12':
        audio_title = f12
        play_audio()
    elif audio_var.get() == 'Romans 13':
        audio_title = f13
        play_audio()
    elif audio_var.get() == 'Romans 14':
        audio_title = f14
        play_audio()
    elif audio_var.get() == 'Romans 15':
        audio_title = f15
        play_audio()
    elif audio_var.get() == 'Romans 16':
        audio_title = f16
        play_audio()
    elif audio_var.get() == '1 Corinthians 1':
        audio_title = g1
        play_audio()
    elif audio_var.get() == '1 Corinthians 2':
        audio_title = g2
        play_audio()
    elif audio_var.get() == '1 Corinthians 3':
        audio_title = g3
        play_audio()
    elif audio_var.get() == '1 Corinthians 4':
        audio_title = g4
        play_audio()
    elif audio_var.get() == '1 Corinthians 5':
        audio_title = g5
        play_audio()
    elif audio_var.get() == '1 Corinthians 6':
        audio_title = g6
        play_audio()
    elif audio_var.get() == '1 Corinthians 7':
        audio_title = g7
        play_audio()
    elif audio_var.get() == '1 Corinthians 8':
        audio_title = g8
        play_audio()
    elif audio_var.get() == '1 Corinthians 9':
        audio_title = g9
        play_audio()
    elif audio_var.get() == '1 Corinthians 10':
        audio_title = g10
        play_audio()
    elif audio_var.get() == '1 Corinthians 11':
        audio_title = g11
        play_audio()
    elif audio_var.get() == '1 Corinthians 12':
        audio_title = g12
        play_audio()
    elif audio_var.get() == '1 Corinthians 13':
        audio_title = g13
        play_audio()
    elif audio_var.get() == '1 Corinthians 14':
        audio_title = g14
        play_audio()
    elif audio_var.get() == '1 Corinthians 15':
        audio_title = g15
        play_audio()
    elif audio_var.get() == '1 Corinthians 16':
        audio_title = g16
        play_audio()

    elif audio_var.get() == '2 Corinthians 1':
        audio_title = h1
        play_audio()
    elif audio_var.get() == '2 Corinthians 2':
        audio_title = h2
        play_audio()
    elif audio_var.get() == '2 Corinthians 3':
        audio_title = h3
        play_audio()
    elif audio_var.get() == '2 Corinthians 4':
        audio_title = h4
        play_audio()
    elif audio_var.get() == '2 Corinthians 5':
        audio_title = h5
        play_audio()
    elif audio_var.get() == '2 Corinthians 6':
        audio_title = h6
        play_audio()
    elif audio_var.get() == '2 Corinthians 7':
        audio_title = h7
        play_audio()
    elif audio_var.get() == '2 Corinthians 8':
        audio_title = h8
        play_audio()
    elif audio_var.get() == '2 Corinthians 9':
        audio_title = h9
        play_audio()
    elif audio_var.get() == '2 Corinthians 10':
        audio_title = h10
        play_audio()
    elif audio_var.get() == '2 Corinthians 11':
        audio_title = h11
        play_audio()
    elif audio_var.get() == '2 Corinthians 12':
        audio_title = h12
        play_audio()
    elif audio_var.get() == '2 Corinthians 13':
        audio_title = h13
        play_audio()

    elif audio_var.get() == 'Galatians 1':
        audio_title = i1
        play_audio()
    elif audio_var.get() == 'Galatians 2':
        audio_title = i2
        play_audio()
    elif audio_var.get() == 'Galatians 3':
        audio_title = i3
        play_audio()
    elif audio_var.get() == 'Galatians 4':
        audio_title = i4
        play_audio()
    elif audio_var.get() == 'Galatians 5':
        audio_title = i5
        play_audio()
    elif audio_var.get() == 'Galatians 6':
        audio_title = i6
        play_audio()

    elif audio_var.get() == 'Ephesians 1':
        audio_title = j1
        play_audio()
    elif audio_var.get() == 'Ephesians 2':
        audio_title = j2
        play_audio()
    elif audio_var.get() == 'Ephesians 3':
        audio_title = j3
        play_audio()
    elif audio_var.get() == 'Ephesians 4':
        audio_title = j4
        play_audio()
    elif audio_var.get() == 'Ephesians 5':
        audio_title = j5
        play_audio()
    elif audio_var.get() == 'Ephesians 6':
        audio_title = j6
        play_audio()

    elif audio_var.get() == 'Philippians 1':
        audio_title = k1
        play_audio()
    elif audio_var.get() == 'Philippians 2':
        audio_title = k2
        play_audio()
    elif audio_var.get() == 'Philippians 3':
        audio_title = k3
        play_audio()
    elif audio_var.get() == 'Philippians 4':
        audio_title = k4
        play_audio()

    elif audio_var.get() == 'Colossians 1':
        audio_title = l1
        play_audio()
    elif audio_var.get() == 'Colossians 2':
        audio_title = l2
        play_audio()
    elif audio_var.get() == 'Colossians 3':
        audio_title = l3
        play_audio()
    elif audio_var.get() == 'Colossians 4':
        audio_title = l4
        play_audio()

    elif audio_var.get() == '1 Thessalonians 1':
        audio_title = m1
        play_audio()
    elif audio_var.get() == '1 Thessalonians 2':
        audio_title = m2
        play_audio()
    elif audio_var.get() == '1 Thessalonians 3':
        audio_title = m3
        play_audio()
    elif audio_var.get() == '1 Thessalonians 4':
        audio_title = m4
        play_audio()
    elif audio_var.get() == '1 Thessalonians 5':
        audio_title = m5
        play_audio()

    elif audio_var.get() == '2 Thessalonians 1':
        audio_title = n1
        play_audio()
    elif audio_var.get() == '2 Thessalonians 2':
        audio_title = n2
        play_audio()
    elif audio_var.get() == '2 Thessalonians 3':
        audio_title = n3
        play_audio()

    elif audio_var.get() == '1 Timothy 1':
        audio_title = o1
        play_audio()
    elif audio_var.get() == '1 Timothy 2':
        audio_title = o2
        play_audio()
    elif audio_var.get() == '1 Timothy 3':
        audio_title = o3
        play_audio()
    elif audio_var.get() == '1 Timothy 4':
        audio_title = o4
        play_audio()
    elif audio_var.get() == '1 Timothy 5':
        audio_title = o5
        play_audio()
    elif audio_var.get() == '1 Timothy 6':
        audio_title = o6
        play_audio()

    elif audio_var.get() == '2 Timothy 1':
        audio_title = p1
        play_audio()
    elif audio_var.get() == '2 Timothy 2':
        audio_title = p2
        play_audio()
    elif audio_var.get() == '2 Timothy 3':
        audio_title = p3
        play_audio()
    elif audio_var.get() == '2 Timothy 4':
        audio_title = p4
        play_audio()

    elif audio_var.get() == 'Titus 1':
        audio_title = q1
        play_audio()
    elif audio_var.get() == 'Titus 2':
        audio_title = q2
        play_audio()
    elif audio_var.get() == 'Titus 3':
        audio_title = q3
        play_audio()

    elif audio_var.get() == 'Philemon 1':
        audio_title = r1
        play_audio()

    elif audio_var.get() == 'Hebrews 1':
        audio_title = s1
        play_audio()
    elif audio_var.get() == 'Hebrews 2':
        audio_title = s2
        play_audio()
    elif audio_var.get() == 'Hebrews 3':
        audio_title = s3
        play_audio()
    elif audio_var.get() == 'Hebrews 4':
        audio_title = s4
        play_audio()
    elif audio_var.get() == 'Hebrews 5':
        audio_title = s5
        play_audio()
    elif audio_var.get() == 'Hebrews 6':
        audio_title = s6
        play_audio()
    elif audio_var.get() == 'Hebrews 7':
        audio_title = s7
        play_audio()
    elif audio_var.get() == 'Hebrews 8':
        audio_title = s8
        play_audio()
    elif audio_var.get() == 'Hebrews 9':
        audio_title = s9
        play_audio()
    elif audio_var.get() == 'Hebrews 10':
        audio_title = s10
        play_audio()
    elif audio_var.get() == 'Hebrews 11':
        audio_title = s11
        play_audio()
    elif audio_var.get() == 'Hebrews 12':
        audio_title = s12
        play_audio()
    elif audio_var.get() == 'Hebrews 13':
        audio_title = s13
        play_audio()

    elif audio_var.get() == 'James 1':
        audio_title = t1
        play_audio()
    elif audio_var.get() == 'James 2':
        audio_title = t2
        play_audio()
    elif audio_var.get() == 'James 3':
        audio_title = t3
        play_audio()
    elif audio_var.get() == 'James 4':
        audio_title = t4
        play_audio()
    elif audio_var.get() == 'James 5':
        audio_title = t5
        play_audio()

    elif audio_var.get() == '1 Peter 1':
        audio_title = u1
        play_audio()
    elif audio_var.get() == '1 Peter 2':
        audio_title = u2
        play_audio()
    elif audio_var.get() == '1 Peter 3':
        audio_title = u3
        play_audio()
    elif audio_var.get() == '1 Peter 4':
        audio_title = u4
        play_audio()
    elif audio_var.get() == '1 Peter 5':
        audio_title = u5
        play_audio()

    elif audio_var.get() == '2 Peter 1':
        audio_title = v1
        play_audio()
    elif audio_var.get() == '2 Peter 2':
        audio_title = v2
        play_audio()
    elif audio_var.get() == '2 Peter 3':
        audio_title = v3
        play_audio()

    elif audio_var.get() == '1 John 1':
        audio_title = w1
        play_audio()
    elif audio_var.get() == '1 John 2':
        audio_title = w2
        play_audio()
    elif audio_var.get() == '1 John 3':
        audio_title = w3
        play_audio()
    elif audio_var.get() == '1 John 4':
        audio_title = w4
        play_audio()
    elif audio_var.get() == '1 John 5':
        audio_title = w5
        play_audio()

    elif audio_var.get() == '2 John 1':
        audio_title = w_1
        play_audio()

    elif audio_var.get() == '3 John 1':
        audio_title = ww1
        play_audio()

    elif audio_var.get() == 'Jude 1':
        audio_title = x1
        play_audio()


    elif audio_var.get() == 'Revelation 1':
        audio_title = y1
        play_audio()
    elif audio_var.get() == 'Revelation 2':
        audio_title = y2
        play_audio()
    elif audio_var.get() == 'Revelation 3':
        audio_title = y3
        play_audio()
    elif audio_var.get() == 'Revelation 4':
        audio_title = y4
        play_audio()
    elif audio_var.get() == 'Revelation 5':
        audio_title = y5
        play_audio()
    elif audio_var.get() == 'Revelation 6':
        audio_title = y6
        play_audio()
    elif audio_var.get() == 'Revelation 7':
        audio_title = y7
        play_audio()
    elif audio_var.get() == 'Revelation 8':
        audio_title = y8
        play_audio()
    elif audio_var.get() == 'Revelation 9':
        audio_title = y9
        play_audio()
    elif audio_var.get() == 'Revelation 10':
        audio_title = y10
        play_audio()
    elif audio_var.get() == 'Revelation 11':
        audio_title = y11
        play_audio()
    elif audio_var.get() == 'Revelation 12':
        audio_title = y12
        play_audio()
    elif audio_var.get() == 'Revelation 13':
        audio_title = y13
        play_audio()
    elif audio_var.get() == 'Revelation 14':
        audio_title = y14
        play_audio()
    elif audio_var.get() == 'Revelation 15':
        audio_title = y15
        play_audio()
    elif audio_var.get() == 'Revelation 16':
        audio_title = y16
        play_audio()
    elif audio_var.get() == 'Revelation 17':
        audio_title = y17
        play_audio()
    elif audio_var.get() == 'Revelation 18':
        audio_title = y18
        play_audio()
    elif audio_var.get() == 'Revelation 19':
        audio_title = y19
        play_audio()
    elif audio_var.get() == 'Revelation 20':
        audio_title = y20
        play_audio()
    elif audio_var.get() == 'Revelation 21':
        audio_title = y21
        play_audio()
    elif audio_var.get() == 'Revelation 22':
        audio_title = y22
        play_audio()


def play_audio():
    global audio_title
    mixer.init()
    mixer.music.load(audio_title)
    mixer.music.play()

def stop_button_clicked():
    mixer.music.stop()

def pause_button_clicked():
    mixer.music.pause()

def resume_button_clicked():
    mixer.music.unpause()
        

infos_button_ON = False
ebooks_button_ON = False

# Text Files
file_1t = 'ebooks/kjv-bible.txt'
file_2t = 'ebooks/ang_biblia_1905.txt'
file_3t = 'ebooks/douay-bible.txt'

f_1t = 'infos/kjvinfo_2.txt'
f_2t = 'infos/tagbible_info.txt'
f_3t = 'infos/douay-info.txt'

# Audio Files
a1 = "KJV-NT/40_KJV_MAT001.mp3"
a2 = "KJV-NT/40_KJV_MAT002.mp3"
a3 = "KJV-NT/40_KJV_MAT003.mp3"
a4 = "KJV-NT/40_KJV_MAT004.mp3"
a5 = "KJV-NT/40_KJV_MAT005.mp3"
a6 = "KJV-NT/40_KJV_MAT006.mp3"
a7 = "KJV-NT/40_KJV_MAT007.mp3"
a8 = "KJV-NT/40_KJV_MAT008.mp3"
a9 = "KJV-NT/40_KJV_MAT009.mp3"
a10 = "KJV-NT/40_KJV_MAT010.mp3"
a11 = "KJV-NT/40_KJV_MAT011.mp3"
a12 = "KJV-NT/40_KJV_MAT012.mp3"
a13 = "KJV-NT/40_KJV_MAT013.mp3"
a14 = "KJV-NT/40_KJV_MAT014.mp3"
a15 = "KJV-NT/40_KJV_MAT015.mp3"
a16 = "KJV-NT/40_KJV_MAT016.mp3"
a17 = "KJV-NT/40_KJV_MAT017.mp3"
a18 = "KJV-NT/40_KJV_MAT018.mp3"
a19 = "KJV-NT/40_KJV_MAT019.mp3"
a20 = "KJV-NT/40_KJV_MAT020.mp3"
a21 = "KJV-NT/40_KJV_MAT021.mp3"
a22 = "KJV-NT/40_KJV_MAT022.mp3"
a23 = "KJV-NT/40_KJV_MAT023.mp3"
a24 = "KJV-NT/40_KJV_MAT024.mp3"
a25 = "KJV-NT/40_KJV_MAT025.mp3"
a26 = "KJV-NT/40_KJV_MAT026.mp3"
a27 = "KJV-NT/40_KJV_MAT027.mp3"
a28 = "KJV-NT/40_KJV_MAT028.mp3"
b1 = "KJV-NT/41_KJV_MRK001.mp3"
b2 = "KJV-NT/41_KJV_MRK002.mp3"
b3 = "KJV-NT/41_KJV_MRK003.mp3"
b4 = "KJV-NT/41_KJV_MRK004.mp3"
b5 = "KJV-NT/41_KJV_MRK005.mp3"
b6 = "KJV-NT/41_KJV_MRK006.mp3"
b7 = "KJV-NT/41_KJV_MRK007.mp3"
b8 = "KJV-NT/41_KJV_MRK008.mp3"
b9 = "KJV-NT/41_KJV_MRK009.mp3"
b10 = "KJV-NT/41_KJV_MRK010.mp3"
b11 = "KJV-NT/41_KJV_MRK011.mp3"
b12 = "KJV-NT/41_KJV_MRK012.mp3"
b13 = "KJV-NT/41_KJV_MRK013.mp3"
b14 = "KJV-NT/41_KJV_MRK014.mp3"
b15 = "KJV-NT/41_KJV_MRK015.mp3"
b16 = "KJV-NT/41_KJV_MRK016.mp3"
c1 = "KJV-NT/42_KJV_LUK001.mp3"
c2 = "KJV-NT/42_KJV_LUK002.mp3"
c3 = "KJV-NT/42_KJV_LUK003.mp3"
c4 = "KJV-NT/42_KJV_LUK004.mp3"
c5 = "KJV-NT/42_KJV_LUK005.mp3"
c6 = "KJV-NT/42_KJV_LUK006.mp3"
c7 = "KJV-NT/42_KJV_LUK007.mp3"
c8 = "KJV-NT/42_KJV_LUK008.mp3"
c9 = "KJV-NT/42_KJV_LUK009.mp3"
c10 = "KJV-NT/42_KJV_LUK010.mp3"
c11 = "KJV-NT/42_KJV_LUK011.mp3"
c12 = "KJV-NT/42_KJV_LUK012.mp3"
c13 = "KJV-NT/42_KJV_LUK013.mp3"
c14 = "KJV-NT/42_KJV_LUK014.mp3"
c15 = "KJV-NT/42_KJV_LUK015.mp3"
c16 = "KJV-NT/42_KJV_LUK016.mp3"
c17 = "KJV-NT/42_KJV_LUK017.mp3"
c18 = "KJV-NT/42_KJV_LUK018.mp3"
c19 = "KJV-NT/42_KJV_LUK019.mp3"
c20 = "KJV-NT/42_KJV_LUK020.mp3"
c21 = "KJV-NT/42_KJV_LUK021.mp3"
c22 = "KJV-NT/42_KJV_LUK022.mp3"
c23 = "KJV-NT/42_KJV_LUK023.mp3"
c24 = "KJV-NT/42_KJV_LUK024.mp3"
d1 = "KJV-NT/43_KJV_JHN001.mp3"
d2 = "KJV-NT/43_KJV_JHN002.mp3"
d3 = "KJV-NT/43_KJV_JHN003.mp3"
d4 = "KJV-NT/43_KJV_JHN004.mp3"
d5 = "KJV-NT/43_KJV_JHN005.mp3"
d6 = "KJV-NT/43_KJV_JHN006.mp3"
d7 = "KJV-NT/43_KJV_JHN007.mp3"
d8 = "KJV-NT/43_KJV_JHN008.mp3"
d9 = "KJV-NT/43_KJV_JHN009.ogg"
d10 = "KJV-NT/43_KJV_JHN010.mp3"
d11 = "KJV-NT/43_KJV_JHN011.mp3"
d12 = "KJV-NT/43_KJV_JHN012.mp3"
d13 = "KJV-NT/43_KJV_JHN013.mp3"
d14 = "KJV-NT/43_KJV_JHN014.mp3"
d15 = "KJV-NT/43_KJV_JHN015.mp3"
d16 = "KJV-NT/43_KJV_JHN016.mp3"
d17 = "KJV-NT/43_KJV_JHN017.mp3"
d18 = "KJV-NT/43_KJV_JHN018.mp3"
d19 = "KJV-NT/43_KJV_JHN019.mp3"
d20 = "KJV-NT/43_KJV_JHN020.mp3"
d21 = "KJV-NT/43_KJV_JHN021.mp3"
e1 = "KJV-NT/44_KJV_ACT001.mp3"
e2 = "KJV-NT/44_KJV_ACT002.mp3"
e3 = "KJV-NT/44_KJV_ACT003.mp3"
e4 = "KJV-NT/44_KJV_ACT004.mp3"
e5 = "KJV-NT/44_KJV_ACT005.mp3"
e6 = "KJV-NT/44_KJV_ACT006.mp3"
e7 = "KJV-NT/44_KJV_ACT007.mp3"
e8 = "KJV-NT/44_KJV_ACT008.mp3"
e9 = "KJV-NT/44_KJV_ACT009.mp3"
e10 = "KJV-NT/44_KJV_ACT010.mp3"
e11 = "KJV-NT/44_KJV_ACT011.mp3"
e12 = "KJV-NT/44_KJV_ACT012.mp3"
e13 = "KJV-NT/44_KJV_ACT013.mp3"
e14 = "KJV-NT/44_KJV_ACT014.mp3"
e15 = "KJV-NT/44_KJV_ACT015.mp3"
e16 = "KJV-NT/44_KJV_ACT016.ogg"
e17 = "KJV-NT/44_KJV_ACT017.mp3"
e18 = "KJV-NT/44_KJV_ACT018.mp3"
e19 = "KJV-NT/44_KJV_ACT019.mp3"
e20 = "KJV-NT/44_KJV_ACT020.mp3"
e21 = "KJV-NT/44_KJV_ACT021.mp3"
e22 = "KJV-NT/44_KJV_ACT022.mp3"
e23 = "KJV-NT/44_KJV_ACT023.mp3"
e24 = "KJV-NT/44_KJV_ACT024.mp3"
e25 = "KJV-NT/44_KJV_ACT025.mp3"
e26 = "KJV-NT/44_KJV_ACT026.mp3"
e27 = "KJV-NT/44_KJV_ACT027.mp3"
e28 = "KJV-NT/44_KJV_ACT028.mp3"
f1 = "KJV-NT/45_KJV_ROM001.mp3"
f2 = "KJV-NT/45_KJV_ROM002.mp3"
f3 = "KJV-NT/45_KJV_ROM003.mp3"
f4 = "KJV-NT/45_KJV_ROM004.mp3"
f5 = "KJV-NT/45_KJV_ROM005.mp3"
f6 = "KJV-NT/45_KJV_ROM006.mp3"
f7 = "KJV-NT/45_KJV_ROM007.mp3"
f8 = "KJV-NT/45_KJV_ROM008.mp3"
f9 = "KJV-NT/45_KJV_ROM009.mp3"
f10 = "KJV-NT/45_KJV_ROM010.mp3"
f11 = "KJV-NT/45_KJV_ROM011.mp3"
f12 = "KJV-NT/45_KJV_ROM012.mp3"
f13 = "KJV-NT/45_KJV_ROM013.mp3"
f14 = "KJV-NT/45_KJV_ROM014.mp3"
f15 = "KJV-NT/45_KJV_ROM015.mp3"
f16 = "KJV-NT/45_KJV_ROM016.mp3"
g1 = "KJV-NT/46_KJV_1CO001.mp3"
g2 = "KJV-NT/46_KJV_1CO002.mp3"
g3 = "KJV-NT/46_KJV_1CO003.mp3"
g4 = "KJV-NT/46_KJV_1CO004.mp3"
g5 = "KJV-NT/46_KJV_1CO005.mp3"
g6 = "KJV-NT/46_KJV_1CO006.mp3"
g7 = "KJV-NT/46_KJV_1CO007.mp3"
g8 = "KJV-NT/46_KJV_1CO008.mp3"
g9 = "KJV-NT/46_KJV_1CO009.mp3"
g10 = "KJV-NT/46_KJV_1CO010.mp3"
g11 = "KJV-NT/46_KJV_1CO011.mp3"
g12 = "KJV-NT/46_KJV_1CO012.mp3"
g13 = "KJV-NT/46_KJV_1CO013.mp3"
g14 = "KJV-NT/46_KJV_1CO014.mp3"
g15 = "KJV-NT/46_KJV_1CO015.mp3"
g16 = "KJV-NT/46_KJV_1CO016.mp3"
h1 = "KJV-NT/47_KJV_2CO001.mp3"
h2 = "KJV-NT/47_KJV_2CO002.mp3"
h3 = "KJV-NT/47_KJV_2CO003.mp3"
h4 = "KJV-NT/47_KJV_2CO004.mp3"
h5 = "KJV-NT/47_KJV_2CO005.mp3"
h6 = "KJV-NT/47_KJV_2CO006.mp3"
h7 = "KJV-NT/47_KJV_2CO007.mp3"
h8 = "KJV-NT/47_KJV_2CO008.mp3"
h9 = "KJV-NT/47_KJV_2CO009.mp3"
h10 = "KJV-NT/47_KJV_2CO010.mp3"
h11 = "KJV-NT/47_KJV_2CO011.mp3"
h12 = "KJV-NT/47_KJV_2CO012.mp3"
h13 = "KJV-NT/47_KJV_2CO013.mp3"
i1 = "KJV-NT/48_KJV_GAL001.mp3"
i2 = "KJV-NT/48_KJV_GAL002.mp3"
i3 = "KJV-NT/48_KJV_GAL003.mp3"
i4 = "KJV-NT/48_KJV_GAL004.mp3"
i5 = "KJV-NT/48_KJV_GAL005.mp3"
i6 = "KJV-NT/48_KJV_GAL006.mp3"
j1 = "KJV-NT/49_KJV_EPH001.mp3"
j2 = "KJV-NT/49_KJV_EPH002.mp3"
j3 = "KJV-NT/49_KJV_EPH003.mp3"
j4 = "KJV-NT/49_KJV_EPH004.mp3"
j5 = "KJV-NT/49_KJV_EPH005.mp3"
j6 = "KJV-NT/49_KJV_EPH006.mp3"
k1 = "KJV-NT/50_KJV_PHP001.mp3"
k2 = "KJV-NT/50_KJV_PHP002.mp3"
k3 = "KJV-NT/50_KJV_PHP003.mp3"
k4 = "KJV-NT/50_KJV_PHP004.mp3"
l1 = "KJV-NT/51_KJV_COL001.mp3"
l2 = "KJV-NT/51_KJV_COL002.mp3"
l3 = "KJV-NT/51_KJV_COL003.mp3"
l4 = "KJV-NT/51_KJV_COL004.mp3"
m1 = "KJV-NT/52_KJV_1TH001.mp3"
m2 = "KJV-NT/52_KJV_1TH002.mp3"
m3 = "KJV-NT/52_KJV_1TH003.mp3"
m4 = "KJV-NT/52_KJV_1TH004.mp3"
m5 = "KJV-NT/52_KJV_1TH005.mp3"
n1 = "KJV-NT/53_KJV_2TH001.mp3"
n2 = "KJV-NT/53_KJV_2TH002.mp3"
n3 = "KJV-NT/53_KJV_2TH003.mp3"
o1 = "KJV-NT/54_KJV_1TI001.mp3"
o2 = "KJV-NT/54_KJV_1TI002.mp3"
o3 = "KJV-NT/54_KJV_1TI003.mp3"
o4 = "KJV-NT/54_KJV_1TI004.mp3"
o5 = "KJV-NT/54_KJV_1TI005.ogg"
o6 = "KJV-NT/54_KJV_1TI006.mp3"
p1 = "KJV-NT/55_KJV_2TI001.mp3"
p2 = "KJV-NT/55_KJV_2TI002.mp3"
p3 = "KJV-NT/55_KJV_2TI003.mp3"
p4 = "KJV-NT/55_KJV_2TI004.mp3"
q1 = "KJV-NT/56_KJV_TIT001.ogg"
q2 = "KJV-NT/56_KJV_TIT002.mp3"
q3 = "KJV-NT/56_KJV_TIT003.mp3"
r1 = "KJV-NT/57_KJV_PHM001.mp3"
s1 = "KJV-NT/58_KJV_HEB001.mp3"
s2 = "KJV-NT/58_KJV_HEB002.mp3"
s3 = "KJV-NT/58_KJV_HEB003.mp3"
s4 = "KJV-NT/58_KJV_HEB004.mp3"
s5 = "KJV-NT/58_KJV_HEB005.mp3"
s6 = "KJV-NT/58_KJV_HEB006.mp3"
s7 = "KJV-NT/58_KJV_HEB007.mp3"
s8 = "KJV-NT/58_KJV_HEB008.mp3"
s9 = "KJV-NT/58_KJV_HEB009.mp3"
s10 = "KJV-NT/58_KJV_HEB010.mp3"
s11 = "KJV-NT/58_KJV_HEB011.mp3"
s12 = "KJV-NT/58_KJV_HEB012.mp3"
t1 = "KJV-NT/59_KJV_JAS001.mp3"
t2 = "KJV-NT/59_KJV_JAS002.mp3"
t3 = "KJV-NT/59_KJV_JAS003.mp3"
t4 = "KJV-NT/59_KJV_JAS004.mp3"
t5 = "KJV-NT/59_KJV_JAS005.mp3"
u1 = "KJV-NT/60_KJV_1PE001.mp3"
u2 = "KJV-NT/60_KJV_1PE002.mp3"
u3 = "KJV-NT/60_KJV_1PE003.mp3"
u4 = "KJV-NT/60_KJV_1PE004.mp3"
u5 = "KJV-NT/60_KJV_1PE005.mp3"
v1 = "KJV-NT/61_KJV_2PE001.mp3"
v2 = "KJV-NT/61_KJV_2PE002.mp3"
v3 = "KJV-NT/61_KJV_2PE003.mp3"
w1 = "KJV-NT/62_KJV_1JN001.mp3"
w2 = "KJV-NT/62_KJV_1JN002.mp3"
w3 = "KJV-NT/62_KJV_1JN003.mp3"
w4 = "KJV-NT/62_KJV_1JN004.mp3"
w5 = "KJV-NT/62_KJV_1JN005.mp3"
w_1 = "KJV-NT/63_KJV_2JN001.mp3"
ww1 = "KJV-NT/64_KJV_3JN001.mp3"
x1 = "KJV-NT/65_KJV_JUD001.mp3"
y1 = "KJV-NT/66_KJV_REV001.mp3"
y2 = "KJV-NT/66_KJV_REV002.mp3"
y3 = "KJV-NT/66_KJV_REV003.mp3" 
y4 = "KJV-NT/66_KJV_REV004.mp3"
y5 = "KJV-NT/66_KJV_REV005.mp3"
y6 = "KJV-NT/66_KJV_REV006.mp3"
y7 = "KJV-NT/66_KJV_REV007.mp3"
y8 = "KJV-NT/66_KJV_REV008.mp3"
y9 = "KJV-NT/66_KJV_REV009.mp3"
y10 = "KJV-NT/66_KJV_REV010.mp3"
y11 = "KJV-NT/66_KJV_REV011.mp3"
y12 = "KJV-NT/66_KJV_REV012.mp3"
y13 = "KJV-NT/66_KJV_REV013.mp3"
y14 = "KJV-NT/66_KJV_REV014.mp3"
y15 = "KJV-NT/66_KJV_REV015.mp3"
y16 = "KJV-NT/66_KJV_REV016.mp3"
y17 = "KJV-NT/66_KJV_REV017.mp3"
y18 = "KJV-NT/66_KJV_REV018.mp3"
y19 = "KJV-NT/66_KJV_REV019.mp3"
y20 = "KJV-NT/66_KJV_REV020.mp3"
y21 = "KJV-NT/66_KJV_REV021.mp3"
y22 = "KJV-NT/66_KJV_REV022.mp3"

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
gutenberg_button = tk.Button(button_frame, text='E-Book Infos', fg='red', bg='yellow green', disabledforeground='yellow', command=infos_button_clicked)
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
variable.set("King James Version Of The Bible")  # default value
tk.Label(menu_frame, text="E-BOOKS MENU :").pack()
option = tk.OptionMenu(menu_frame, variable, "King James Version Of The Bible", "Ang Biblia (1905)",
                       "Douay-Rheims Version Of The Bible")
option.pack()

# audio option menu with Label
menu_frame3 = tk.Frame(root, bd=3, relief=tk.GROOVE)
menu_frame3.pack(fill=tk.X, side=tk.BOTTOM, padx=2, pady=2)
menu_frame2 = tk.Frame(root, bd=3)
menu_frame2.pack(fill=tk.X, side=tk.BOTTOM, padx=2, pady=0)
audio_var = tk.StringVar(menu_frame3)
audio_var.set("John 1")  # default value
tk.Label(menu_frame2, text="AUDLIB1").pack(side='left', padx=15, fill=tk.BOTH, expand=1)
tk.Label(menu_frame2, text="AUDLIB2").pack(side='left', padx=15, fill=tk.BOTH, expand=1)
tk.Label(menu_frame2, text="AUDLIB3").pack(side='left', padx=15, fill=tk.BOTH, expand=1)
tk.Label(menu_frame2, text="AUDLIB4").pack(side='left', padx=15, fill=tk.BOTH, expand=1)
audio_option1 = tk.OptionMenu(menu_frame3, audio_var, 'Matthew 1', 'Matthew 2', 'Matthew 3', 'Matthew 4',
                             'Matthew 5', 'Matthew 6', 'Matthew 7', 'Matthew 8', 'Matthew 9', 'Matthew 10',
                             'Matthew 11', 'Matthew 12', 'Matthew 13', 'Matthew 14', 'Matthew 15', 'Matthew 16',
                             'Matthew 17', 'Matthew 18', 'Matthew 18', 'Matthew 19', 'Matthew 20', 'Matthew 21',
                             'Matthew 22', 'Matthew 23', 'Matthew 24', 'Matthew 25', 'Matthew 26', 'Matthew 27',
                             'Matthew 28', 'Mark 1', 'Mark 2', 'Mark 3', 'Mark 4', 'Mark 5',
                             'Mark 6', 'Mark 7', 'Mark 8', 'Mark 9', 'Mark 10', 'Mark 11',
                             'Mark 12', 'Mark 13', 'Mark 14', 'Mark 15', 'Mark 16',
                             'Luke 1', 'Luke 2', 'Luke 3', 'Luke 4', 'Luke 5', 'Luke 6',
                             'Luke 7', 'Luke 8', 'Luke 9', 'Luke 10', 'Luke 11', 'Luke 12',
                             'Luke 13', 'Luke 14', 'Luke 15', 'Luke 16', 'Luke 17', 'Luke 18',
                             'Luke 19', 'Luke 20', 'Luke 21', 'Luke 22', 'Luke 23', 'Luke 24',
                             'John 1', 'John 2', 'John 3', 'John 4', 'John 5', 'John 6', 'John 7',
                             'John 8', 'John 9', 'John 10', 'John 11', 'John 12', 'John 13', 'John 14',
                             'John 15', 'John 16', 'John 17', 'John 18', 'John 19', 'John 20', 'John 21')

audio_option2 = tk.OptionMenu(menu_frame3, audio_var, 'Acts 1', 'Acts 2', 'Acts 3', 'Acts 4', 'Acts 5', 'Acts 6', 'Acts 7',
                             'Acts 8', 'Acts 9', 'Acts 10', 'Acts 11', 'Acts 12', 'Acts 13', 'Acts 14',
                             'Acts 15', 'Acts 16', 'Acts 17', 'Acts 18', 'Acts 19', 'Acts 20', 'Acts 21',
                             'Acts 22', 'Acts 23', 'Acts 24', 'Acts 25', 'Acts 26', 'Acts 27', 'Acts 28',
                             'Romans 1', 'Romans 2', 'Romans 3', 'Romans 4', 'Romans 5', 'Romans 6', 'Romans 7',
                             'Romans 8', 'Romans 9', 'Romans 10', 'Romans 11', 'Romans 12', 'Romans 13', 'Romans 14',
                             'Romans 15', 'Romans 16', '1 Corinthians 1', '1 Corinthians 2', '1 Corinthians 3',
                             '1 Corinthians 4', '1 Corinthians 5', '1 Corinthians 6', '1 Corinthians 7', '1 Corinthians 8',
                             '1 Corinthians 9', '1 Corinthians 10', '1 Corinthians 11', '1 Corinthians 12',
                             '1 Corinthians 13', '1 Corinthians 14', '1 Corinthians 15', '1 Corinthians 16',
                             '2 Corinthians 1', '2 Corinthians 2', '2 Corinthians 3', '2 Corinthians 4', '2 Corinthians 5',
                             '2 Corinthians 6', '2 Corinthians 7', '2 Corinthians 8', '2 Corinthians 9',
                             '2 Corinthians 10', '2 Corinthians 11', '2 Corinthians 12', '2 Corinthians 13',
                             'Galatians 1', 'Galatians 2', 'Galatians 3', 'Galatians 4', 'Galatians 5',
                             'Galatians 6')

audio_option3 = tk.OptionMenu(menu_frame3, audio_var, 'Ephesians 1', 'Ephesians 2', 'Ephesians 3', 'Ephesians 4', 'Ephesians 5',
                             'Ephesians 6', 'Philippians 1', 'Philippians 2', 'Philippians 3', 'Philippians 4',
                             'Colossians 1', 'Colossians 2', 'Colossians 3', 'Colossians 4', '1 Thessalonians 1',
                             '1 Thessalonians 2', '1 Thessalonians 3', '1 Thessalonians 4', '1 Thessalonians 5',
                             '2 Thessalonians 1', '2 Thessalonians 2', '2 Thessalonians 3', '1 Timothy 1',
                             '1 Timothy 2', '1 Timothy 3', '1 Timothy 4', '1 Timothy 5', '1 Timothy 6',
                             '2 Timothy 1','2 Timothy 2', '2 Timothy 3', '2 Timothy 4', 'Titus 1',
                             'Titus 2', 'Titus 3', 'Philemon 1', 'Hebrews 1', 'Hebrews 2', 'Hebrews 3',
                             'Hebrews 4', 'Hebrews 5', 'Hebrews 6', 'Hebrews 7', 'Hebrews 8',
                             'Hebrews 9', 'Hebrews 10', 'Hebrews 11', 'Hebrews 12', 'Hebrews 13')

audio_option4 = tk.OptionMenu(menu_frame3, audio_var, 'James 1', 'James 2', 'James 3', 'James 4', 'James 5',
                             '1 Peter 1', '1 Peter 2', '1 Peter 3', '1 Peter 4', '1 Peter 5', '2 Peter 1', '2 Peter 2', '2 Peter 3',
                             '1 John 1', '1 John 2', '1 John 3', '1 John 4', '1 John 5',
                             '2 John 1', '3 John 1', 'Jude 1', 'Revelation 1', 'Revelation 2',
                             'Revelation 3', 'Revelation 4', 'Revelation 5', 'Revelation 6',
                             'Revelation 7', 'Revelation 8', 'Revelation 9', 'Revelation 10',
                             'Revelation 11', 'Revelation 12', 'Revelation 13', 'Revelation 14',
                             'Revelation 15', 'Revelation 16', 'Revelation 17',
                             'Revelation 18', 'Revelation 19', 'Revelation 20', 'Revelation 21',
                             'Revelation 22')
                             
audio_option1.pack(side='left', fill=tk.BOTH, expand=1)
audio_option2.pack(side='left', fill=tk.BOTH, expand=1)
audio_option3.pack(side='left', fill=tk.BOTH, expand=1)
audio_option4.pack(side='left', fill=tk.BOTH, expand=1)
root.protocol("WM_DELETE_WINDOW", close)

