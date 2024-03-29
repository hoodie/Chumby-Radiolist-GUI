import gtk

class gladeGUI:
	def __init__(self,model, controller):
		self.model = model
		self.c = controller
		self.guifile = "gui.glade"
		self.builder = gtk.Builder()
		self.builder.add_from_file(self.guifile)
		self.connect_ui_elements()
		self.entry_host.set_text(self.c.chumbyHost)
		self.builder.connect_signals(self)
		self.window.show()
	
	def connect_ui_elements(self):
		self.window = self.builder.get_object("window1")
		self.dialog_delete = self.builder.get_object("dialog_delete")
		self.dialog_warn = self.builder.get_object("dialog_warn")
		self.label_warn = self.builder.get_object("label_warn")
		self.button_warn = self.builder.get_object("button_warn")
		self.entry_url = self.builder.get_object("entry_url")
		self.entry_name = self.builder.get_object("entry_name")
		self.cbox_mimes = self.builder.get_object("combobox_mimes")
		self.cbox_urls = self.builder.get_object("combobox_urls")
		self.entry_host = self.builder.get_object("entry_host")

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
		s.dialog_delete.run()

	def on_button_del_ok_clicked(s,dlg):
		s.model.delete(s.active_url)
		s.cbox_urls.remove_text(s.active_url)
		s.dialog_delete.hide()

	def on_button_del_abort_clicked(s,dlg):
		s.dialog_delete.hide()

	def on_button_apply_clicked(self,window):
		active = self.c.editing
		url = self.entry_url.get_text()
		name = self.entry_name.get_text()
		mime = self.cbox_mimes.get_active_text()
		if url == "" or name == "":
			self.warn("leere Eingabe")
		else:
			self.c.apply_changes(active,name,url,mime)

	def warn(self, message):
		self.dialog_warn.show()
		self.dialog_warn.set_markup = message
	
	def	on_button_warn_clicked(self,window):
		self.dialog_warn.hide()

	def	on_button_new_clicked(self,window):
		self.active = active = -1
		self.cbox_urls.set_active(active)
		self.entry_url.set_text("")
		self.entry_name.set_text("")

	def on_button_save_clicked(self,window):
		content = self.model.toXML()
		self.model.saveStreams(content)
	
	def on_button_load_clicked(self,window):
		self.model.loadStreams()
		self.init_cbox(self.model.mimes,'combobox_mimes')
		self.init_cbox(self.model.names,'combobox_urls')

	def on_combobox_urls_changed(self,window):
		self.active_url = active = self.cbox_urls.get_active()    
		c = self.c
		name = self.model.get(active)['name']
		mime = self.model.get(active)['mimetype']
		url  = self.model.get(active)['url']
		self.entry_name.set_text(name)
		self.entry_url.set_text(url)
		self.cbox_mimes.set_active(self.model.mimes.index(mime))
		c.editing = active

	def on_window1_destroy(self,window):
		exit()
