from app import db, loginManager, bcrypt
from flask import flash, redirect, url_for
from flask_login import UserMixin

from enum import Enum
from datetime import date

# Model <-> Tabla <-> Class

@loginManager.user_loader
def load_user(id):
	return User.query.get(int(id))


@loginManager.unauthorized_handler
def unauthorized():
	flash("You need to log in first", "warning")
	return redirect(url_for("login"))


class User(db.Model, UserMixin):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	email = db.Column(db.String(32), nullable=False, unique=True)
	password = db.Column(db.String(64), nullable=False)

	products = db.relationship("Product", backref="user")

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = bcrypt.generate_password_hash(password).decode("utf-8")

	def check_password(self, password):
		return bcrypt.check_password_hash(self.password, password)
	
	def __repr__(self):
		#return "USER" + self.id + " : " + self.name
		return f"USER {self.id} : {self.name}" # format-string


class Brand(db.Model):
	__tablename__ = "brands"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), nullable=False)
	country = db.Column(db.String(32), nullable=False)
	
	products = db.relationship("Product", backref="brand")

	def __init__(self, name, country):
		self.name = name
		self.country = country

	def __repr__(self):
		return  f"BRAND {self.id} : {self.name}"


class ProductCategory(Enum):
	TECH = 1
	SPORT = 2
	FASHION = 3
	ART = 4


class ProductCondition(Enum):
	NEW = 1
	USED = 2
	REFURBISHED = 3


class Product(db.Model):
	__tablename__ = "products"
	id = db.Column(db.Integer, primary_key=True)
	brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
	name = db.Column(db.String(32), nullable=False)
	price = db.Column(db.Numeric(8, 2), nullable=False)
	stock = db.Column(db.Integer, nullable=False)
	year = db.Column(db.Integer, nullable=False, default=date.today().year)
	freeshipping = db.Column(db.Boolean, nullable=False, default=False)
	category = db.Column(db.Enum(ProductCategory))
	condition = db.Column(db.Enum(ProductCondition), default=ProductCondition.NEW)

	def __init__(self, brand_id, user_id, name, price, stock, year, freeshipping, category, condition):
		self.brand_id = brand_id
		self.user_id = user_id
		self.name = name
		self.price = price
		self.stock = stock
		self.year = year
		self.freeshipping = freeshipping
		self.category = category
		self.condition = condition

	def __repr__(self):
		return f"PRODUCT {self.id} : {self.name}"

db.create_all()
