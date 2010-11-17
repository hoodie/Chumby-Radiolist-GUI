#!/usr/bin/env python
import gtk
from view import gladeGUI 
from model import streamFileReader 

class controller:
	def __init__(self):
		self.loadFile = './old'
		self.saveFile = './new'
		self.chumbyHost = 'chumby.fritz.box'
		self.dataChanged = False

		model = self.model = streamFileReader(self)
		gui = self.gui = gladeGUI(model, self)
		gtk.main()

	def apply_changes(self, index, name, url, mime):
		model = self.model
		gui = self.gui
		stream = model.newStream(name,url,mime)
		text = gui.entry_name.get_text()
		if(index >= 0):
			model.streams[index] = stream
			gui.cbox_mimes.set_active(model.mimes.index(mime))
			gui.cbox_urls.remove_text(index)
			gui.cbox_urls.insert_text(index,text)
			gui.cbox_urls.set_active(index)
			print model.streams

	
if __name__ == '__main__':
	tool = controller()
