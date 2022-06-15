from app import db, loginManager, bcrypt
from flask_login import UserMixin

# Model <-> Tabla <-> Class

@loginManager.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(db.Model, UserMixin):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	email = db.Column(db.String(32), nullable=False, unique=True)
	password = db.Column(db.String(64), nullable=False)

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = bcrypt.generate_password_hash(password).decode("utf-8")

	def check_password(self, password):
		return bcrypt.check_password_hash(self.password, password)
	
	def __repr__(self):
		#return "USER" + self.id + " : " + self.name
		return f"USER {self.id} : {self.name}" # format-string


db.create_all()
