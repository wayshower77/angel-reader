#---------------------------------------------------------------------------#
#                                                                           #
#    AngelReader Library Selector                                           #
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

# AngelReader Library Selector
# Date: October 02, 2018. 3:17am
# Author: D.A.E. (wayshower.de@gmail.com)
import tkinter as tk

root = tk.Tk()
root.config(bg="light cyan")
root.title("ANGEL READER LIBRARY SELECTOR | DAE-MAN PROJECT")
root.iconbitmap('icons/angel_icon.ico')

def select_library():
    if variable.get() == "James Allen Library 1":               
        import angel_reader_allen_release
        angel_reader_allen_release.open_lib()
    elif variable.get() == "Wallace D. Wattles Library":              
        import angel_reader_wattles_release
        angel_reader_wattles_release.open_lib()
    elif variable.get() == "KJV NT Collection":
        import angel_reader_kjvnt
        angel_reader_kjvnt.open_lib()

def show_about():
    global l_title, tframe_occupied, l_frame
    if ab_variable.get() == "Angel Reader License":
        if tframe_occupied == False:            
            l_title = title_1
            get_frame()
            tframe_occupied = True
        else:
            l_frame.destroy()
            l_title = title_1
            get_frame()

    elif ab_variable.get() == "The DAE-MAN Project":
        if tframe_occupied == False:            
            l_title = title_2
            get_frame()
            tframe_occupied = True
        else:
            l_frame.destroy()
            l_title = title_2
            get_frame()

 
def get_frame():
    global l_title, l_frame
    l_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    # Text widget for the license text
    lic_txt = tk.Text(l_frame, height=30, width=80, wrap=tk.WORD,
                      bg='light goldenrod', font='Courier 12 bold')
    f_obj = open(l_title, encoding="utf8")
    f_content = f_obj.read()
    f_obj.close()
    lic_txt.insert(tk.END, f_content)
    lic_txt.config(state=tk.DISABLED)  # text editing disabled
    lic_txt.pack(side=tk.LEFT, fill=tk.X, padx=5)

    # Scrollbar widget for the Text widget
    s_bar = tk.Scrollbar(l_frame, orient=tk.VERTICAL, command=lic_txt.yview)
    s_bar.pack()
    lic_txt.configure(yscrollcommand=s_bar.set)
    l_frame.pack(side=tk.TOP)



tframe_occupied = False
title_1 = 'docs/LICENSE.txt'
title_2 = 'docs/DAE-MAN.txt'

# Frame for the decor pix
img_frame = tk.Frame(root, bd=3, relief=tk.SUNKEN)
img_frame.pack(fill=tk.Y, side=tk.LEFT, padx=2, pady=2)
image = ['icons/angel_in_garden.png']
img_label = tk.Label(img_frame, bd=2, bg='ivory', relief=tk.RAISED)
img_label.pack(fill=tk.Y, side=tk.LEFT)
photo_image = tk.PhotoImage(file=image)
img_label['image'] = photo_image

# About button with frame
lbutton_frame = tk.Frame(root, bd=2)
lbutton_frame.pack(fill=tk.X, side=tk.BOTTOM)
l_button = tk.Button(lbutton_frame, text="About", fg='white', bg='turquoise4',
                     command=show_about)
l_button.pack(fill=tk.X)

# Selector button with frame
button_frame = tk.Frame(root, bd=2)
button_frame.pack(fill=tk.X, side=tk.BOTTOM)
selector_button = tk.Button(button_frame, text='Click To Load Library',
                            fg='white', bg='turquoise4', command=select_library)
selector_button.pack(fill=tk.X, side=tk.BOTTOM)

# Library menu with Label
menu_frame = tk.Frame(root, bd=3, bg='royalblue2',  relief=tk.GROOVE)
menu_frame.pack(fill=tk.X, padx=2, pady=2)
variable = tk.StringVar(menu_frame)
variable.set("James Allen Library 1")  # default value
tk.Label(menu_frame, bg='lawn green', fg='deep pink', text="Library Menu:").pack()
lib_option = tk.OptionMenu(menu_frame, variable, "James Allen Library 1", "Wallace D. Wattles Library",
                           "KJV NT Collection")
lib_option.config(bg="dark goldenrod", fg="white")
lib_option.pack()

# About menu with Label
ab_frame = tk.Frame(root, bd=3, bg='royalblue2', relief=tk.GROOVE)
ab_frame.pack(fill=tk.X, padx=2, pady=2)
ab_variable = tk.StringVar(ab_frame)
ab_variable.set("The DAE-MAN Project")  # default value
tk.Label(ab_frame, bg='lawn green', fg='deep pink', text="About:").pack()
ab_option = tk.OptionMenu(ab_frame, ab_variable, "Angel Reader License", "The DAE-MAN Project")
ab_option.config(bg="dark goldenrod", fg="white")
ab_option.pack()

root.mainloop()
