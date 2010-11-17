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

	def loadStreams(self):
		with open(self.controller.loadFile,'r') as file:
			if file:
				self.p.Parse(file.read())
				for stream in self.streams:
					self.urls.append(stream['url'])
					self.names.append(stream['name'])

	def saveStreams(self,s):
		with open(self.controller.saveFile,'w') as file:
			file.write(s)


	def elementHandler(self, name, attrs):
		if name == 'stream':
			self.streams.append(attrs)
	
	def append(self,stream):
		# TODO fill empty fields
		if "" not in stream:
			self.streams.append(stream)
			self.urls.append(stream['url'])
			self.names.append(stream['name'])
		else : print 'leere Eingabe'

	def newStream(s, name, url, mime):
		# TODO need prettier hashs
		stream = {}
		stream['url'] = url
		stream['mimetype'] = mime
		stream['id'] = repr(hash(url+mime))
		stream['name'] = name
		return stream

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
		xml = '<streams>\n'
		for stream in self.streams:
			xml += self.toTAG(stream)
		xml += '</streams>'
		return xml

	def toTAG(self, stream):
		tag = '<stream '
		for key,value in stream.iteritems():
			tag += key + '="' + value +'" '
		tag += ' />\n'
		return tag 
