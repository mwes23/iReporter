class Incident():
	"""docstring for Incident"""
	def __init__(self,incident_id,createBy,incident_type,location,status,images,videos,comment):
		self.title = title
		self.created_on = created_on
		self.incident_id = incident_id
		self.created_by = created_by
		self.incident_type = incident_type
		self.location = location
		self.status = status
		self.images = images
		self.videos = videos
		self.comment = comment
		
	def to_json(self):
		return {"title":self.title,"created_by":self.created_by,"incident_type":self.incident_type,"location":self.location,"status":self.status,"images":self.images,"videos":self.videos,"comment":self.comment}


class User():
	"""docstring for User"""
	def __init__(self,id,firstname,lastname,othername,email,phone_number,username,registered,is_admin):
		self.id = id
		self.firstname = firstname
		self.lastname = lastname
		self.othername = othername
		self.email = email
		self.phone_number = phone_number
		self.username = username
		self.registered = registered
		self.is_admin = is_admin
		
		

				
		