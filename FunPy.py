from tkinter import *
from tkinter import messagebox
import time as t
import random as r 

def FakeMining():
	'''The function creates a mining effect'''
	print('MINIG STARTED!')
	while True:
		time = t.localtime() 
		current_time = t.strftime("%H:%M:%S", time)
		print(current_time + ' new job from https://github.com/DedInsult2008')
		for i in range(r.randint(7, 12)):
			time = t.localtime()
			print(t.strftime("%H:%M:%S", time) + ' code: <' + str(hex(r.randint(35, 89))) + '>')
			t.sleep(1)

def WinLocker(title, text, update_cycles):
	'''The function creates a WinLocker effect'''
	for i in range(update_cycles):
		messagebox.showwarning(title = title, message = text)

