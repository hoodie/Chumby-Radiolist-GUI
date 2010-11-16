import gtk

class gladeGUI:
	active_url = active_mime = 0 # did this just because python lets me

	def __init__(self,model, controller):
		self.model = model
		self.controller = controller
		
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
		self.entry_name = self.builder.get_object("entry_name")
		self.cbox_mimes = self.builder.get_object("combobox_mimes")
		self.cbox_urls = self.builder.get_object("combobox_urls")
		

	def init_cbox(self,values,objectname,active=0):
		combobox = self.builder.get_object(objectname)
		liststore = gtk.ListStore(str)
		combobox.set_model(liststore)
		cell = gtk.CellRendererText()
		combobox.pack_start(cell,True)
		combobox.add_attribute(cell, 'text', 0)
		self.populate_cbox(values,liststore)
		combobox.set_active(active)

	def populate_cbox(self,values,liststore):
		liststore.clear()
		for value in values:
			liststore.append([value])

	def update_urls(self):
		self.populate_cbox(self.model.urls,self.cbox_urls.get_model())

	def on_button_delete_clicked(s,window):
		s.delete_dialog.run()

	def on_button_del_ok_clicked(s,dlg):
		s.model.delete(s.active_url)
		s.cbox_urls.remove_text(s.active_url)
		s.delete_dialog.hide()

	def on_button_del_abort_clicked(s,dlg):
		s.delete_dialog.hide()

	def on_button_add_clicked(self,window):
	#TODO abfragen, ob url nicht schon in liste ist, dann ueberschreiben
	#TODO abfragen ob eingabe leer
		self.active_url = active = self.cbox_urls.get_active()    
		url = self.entry_url.get_text()
		name = self.entry_name.get_text()
		mime = self.cbox_mimes.get_active_text()
		self.model.add_stream(name, url,mime)

	def on_button_save_clicked(self,window):
		self.model.toXML()
	
	def on_button_load_clicked(self,window):
		self.model.loadStream()
		self.init_cbox(self.model.mimes,'combobox_mimes')
		self.init_cbox(self.model.names,'combobox_urls')


	def on_combobox_urls_changed(self,window):
		self.active_url = active = self.cbox_urls.get_active()    
		name = self.model.get(active)['name']
		mime = self.model.get(active)['mimetype']
		url  = self.model.get(active)['url']
		self.entry_name.set_text(name)
		self.entry_url.set_text(url)
		self.cbox_mimes.set_active(self.model.mimes.index(mime))

	def on_window1_destroy(self,window):
		exit()
