#!/usr/bin/env python
import gtk
from view import gladeGUI 
from model import streamFileReader 

class controller:
	def __init__(self):
		self.loadFile = './old'
		self.saveFile = './new'
		self.chumbyHost = 'chumby.fritz.box'
		self.editExisting = False
		self.dataChanged = False

		sfr = streamFileReader(self)
		gui = gladeGUI(sfr, self)
		gtk.main()


	
if __name__ == '__main__':
	tool = controller()
