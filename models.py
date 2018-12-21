class Redflag():
	"""docstring for ClassName"""
	def __init__(self, title,desc):
		self.title = title
		self.desc = desc

	def to_json(self,title,desc):
		return {"title":self.title, "desc":self.description}
		