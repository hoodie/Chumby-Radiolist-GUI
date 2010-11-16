import xml.parsers.expat

class streamFileReader:
	streams = []
	mimes = ['audio/x-mpegurl','audio/mpeg','audio/x-scpls','application/ogg']
	urls = []

	def __init__(self):
		self.p = xml.parsers.expat.ParserCreate()
		self.file = self.loadStream()
		self.p.StartElementHandler = self.s_e_h
		
		if self.file:
			self.p.Parse(self.file)
			
			for stream in self.streams:
				self.urls.append(stream['url'])
		else:
			print 'couldn\'t load'

	def s_e_h(self, name, attrs):
		if name == 'stream':
			self.streams.append(attrs)
	
	def append(self,stream):
		# TODO fill empty fields
		self.streams.append(stream)
		self.urls.append(stream['url'])

	def add_stream(s, name, url, mime):
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
	
	def get_mimes(self):
		mimes = []
		for s in self.streams:
			mimes.append(s['mimetype'])
		return mimes

	def loadStream(self):
		with open('./url_streams') as file:
			print 'file loaded'
			return file.read()
	
	def toXML(self):
		for stream in self.streams:
			print self.toTAG(stream)

	def toTAG(self, stream):
		tag = '<stream '
		for key,value in stream.iteritems():
			tag += key + '="' + value +'" '
		tag += ' />'
		return tag 
