from app import db

# Model <-> Tabla <-> Class

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	email = db.Column(db.String(64), unique=True)

	def __init__(self, name, email):
		self.name = name
		self.email = email
	
	def __repr__(self):
		#return "USER" + self.id + " : " + self.name
		return f"USER {self.id} : {self.name}" # format-string


db.create_all()
