class model():
	"""docstring for ClassName"""
	def __init__(self, title,description):
		self.title = title
		self.description = description

	def to_json(self,title,description):
		return {title:self.title,description:self.description}
		