from app import app
from app.models import User
from flask import render_template

@app.route("/")
def index():
	numero = 123
	return render_template("index.html", var=numero)

@app.route("/users")
def users():
	return render_template("users.html",
		users=[] # TODO
	)

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/signup")
def signup():
	return render_template("signup.html")


