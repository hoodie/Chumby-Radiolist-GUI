import gtk

class gladeGUI:
	def __init__(self,model):
		self.model = model
		
		self.guifile = "streamsgui.glade"
		self.builder = gtk.Builder()
		self.builder.add_from_file(self.guifile)
		self.init_ui()

		self.builder.connect_signals(self)
		self.window.show()
	
	def init_ui(self):
		self.delete_dialog = self.builder.get_object("messagedialog1")
		self.window = self.builder.get_object("window1")
		self.entry_url = self.builder.get_object("entry_url")
		self.cbox_mimes = self.builder.get_object("combobox_mimes")
		self.cbox_urls = self.builder.get_object("combobox_urls")
		
		self.populate_cbox(self.model.mimes,'combobox_mimes')
		self.populate_cbox(self.model.urls,'combobox_urls')


	def populate_cbox(self,values,objectname,active=0):
		liststore = gtk.ListStore(str)
		combobox = self.builder.get_object(objectname)
		combobox.set_model(liststore)
		cell = gtk.CellRendererText()
		combobox.pack_start(cell,True)
		combobox.add_attribute(cell, 'text', 0)
		
		for value in values:
			liststore.append([value])
		combobox.set_active(active)

	def on_button_delete_clicked(self,window):
		self.delete_dialog.run()

	def on_button_save_clicked(self,window):
		print gtk.Entry.get_text(self.entry_url)

	def on_button_add_clicked(self,window):
		stream = {}
		stream['url'] = self.entry_url.get_text()
		stream['mimetype'] = self.cbox_mimes.get_active_text()
		self.model.streams.append(stream)
		self.cbox_urls.set_model()
		self.populate_cbox(self.model.urls,'combobox_urls')

	def on_combobox_urls_changed(self,window):
		active = self.cbox_urls.get_active()
		mime = self.model.streams[active]['mimetype']

		self.entry_url.set_text(self.model.streams[active]['url'])
		self.cbox_mimes.set_active(self.model.mimes.index(mime))

	def on_window1_destroy(self,window):
		exit()
