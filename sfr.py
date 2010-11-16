import xml.parsers.expat

class streamFileReader:
	streams = []
	mimes = ['audio/x-mpegurl','audio/mpeg','audio/x-scpls','application/ogg']
	urls = []
	names = []

	def __init__(self, controller):
		self.controller = controller
		self.p = xml.parsers.expat.ParserCreate()
		self.p.StartElementHandler = self.elementHandler
		#self.file = self.loadStream()

	def loadStream(self):
		with open(self.controller.streamsfile) as file:
			if file:
				self.p.Parse(file.read())
				for stream in self.streams:
					self.urls.append(stream['url'])
					self.names.append(stream['name'])
	
	def elementHandler(self, name, attrs):
		if name == 'stream':
			self.streams.append(attrs)
	
	def append(self,stream):
		# TODO fill empty fields
		self.streams.append(stream)
		self.urls.append(stream['url'])
		self.names.append(stream['name'])

	def addStream(s, name, url, mime):
		# TODO need prettier hashs
		stream = {}
		stream['url'] = url
		stream['mimetype'] = mime
		stream['id'] = hash(url+mime)
		stream['name'] = name
		print stream

	def get(s, index):
		return s.streams[index]

	def delete(s, id):
		s.streams.pop(id)
		for stream in s.streams:
			s.urls.append(stream['url'])
	
	def getMimes(self):
		mimes = []
		for s in self.streams:
			mimes.append(s['mimetype'])
		return mimes

	def toXML(self):
		xml = '<streams>'
		for stream in self.streams:
			xml += self.toTAG(stream)
		xml += '</streams>'
		print xml

	def toTAG(self, stream):
		tag = '<stream '
		for key,value in stream.iteritems():
			tag += key + '="' + value +'" '
		tag += ' />'
		return tag 
