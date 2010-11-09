#!/usr/bin/env python
import gtk
from gui import gladeGUI 
from sfr import streamFileReader 
class controller:
	def __init__(self):
		sfr = streamFileReader()
		gui = gladeGUI(sfr)
		gtk.main()


	
if __name__ == '__main__':
	tool = controller()
