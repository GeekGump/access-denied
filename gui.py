'''
github.com/razyar

there is no any access denied here :) 
edit anything you want.
'''

import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import sys
import os
#import win32gui, win32con (if you want to hide terminal - cmd get this module and uncomment it.)
import pyttsx3 as spk


#ForceHideLogger = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(ForceHideLogger , win32con.SW_HIDE)


root = Tkinter.Tk(className="Force access denied")
root.geometry('750x480')
textPad = ScrolledText(root, width=100, height=80)

def open_command():
	file= tkFileDialog.askopenfile(parent=root, mode='rb', title='Select any file ')
	if file != None:
		contents = file.read()
		textPad.insert('1.0', contents)
		file.close()
	
def save_command():
	file = tkFileDialog.asksaveasfile(mode='w')
	if file != None:
		data = textPad.get('1.0', END+'-1c')
		file.write(data)
		file.close()

def exit_command():
	if tkMessageBox.askokcancel("Quit", "Do you want to close? "):
		root.destroy()

		
def about_command():
	r = spk.Engine()
	r.say('more repositores in github.com/razyar')
	r.runAndWait()
	Label = tkMessageBox.showinfo("About", "Force access denied notepad (you will not see any access denied here :) \n Download from: github.com/razyar \n more repo in github and khoderazyar.ir \n https://khoderazyar.ir")
	
def cmd_command():
	os.system('start cmd')
	r = spk.Engine()
	r.say('CMD Runned.')
	r.runAndWait()
	
def dummy():
	filename = sys.argv[0]
	os.system('call %s' % str(filename))
	
	


	
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)




optmenu = Menu(menu)
menu.add_cascade(label="Options", menu=optmenu)
optmenu.add_command(label="CMD", command=cmd_command)





root.iconbitmap('resources/icon.ico')
W = Label(root, text="Force access denied", fg="black")
W.pack()
textPad.pack()
root.mainloop()

