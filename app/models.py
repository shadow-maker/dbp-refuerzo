from app import db, loginManager
from flask_login import UserMixin

# Model <-> Tabla <-> Class

@loginManager.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(db.Model, UserMixin):
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
