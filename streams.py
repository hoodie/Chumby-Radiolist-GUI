#!/usr/bin/env python
import gtk
from gui import gladeGUI 
from sfr import streamFileReader 
class controller:
	def __init__(self):
		self.streamsfile = './url_streams'
		self.chumbyhost = 'chumby.fritz.box'

		sfr = streamFileReader(self)
		gui = gladeGUI(sfr, self)
		gtk.main()


	
if __name__ == '__main__':
	tool = controller()
