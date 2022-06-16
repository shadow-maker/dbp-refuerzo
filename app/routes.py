from app import app, db
from app.models import User

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

@app.route("/")
def index():
	numero = 123
	return render_template("index.html", var=numero)

@app.route("/users")
def users():
	return render_template("users.html",
		title="Users",
		users=User.query.all()
	)

@app.route("/signup", methods=["GET", "POST"])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for("index"))

	if request.method == "POST":
		try: # exception handling
			u = User(
				request.form.get("name"),
				request.form.get("email"),
				request.form.get("password")
			)
			db.session.add(u)
			db.session.commit()
		except:
			flash("Error creating user", "danger")

	return render_template("signup.html", title="Signup")

@app.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("index"))

	if request.method == "POST":
		u = User.query.filter_by(email=request.form["email"]).first()

		if u:
			if u.check_password(request.form["password"]):
				login_user(u)
				return redirect(url_for("index"))
			else:
				flash("Wrong password", "danger")
		else:
			flash("User with this email does not exist", "danger")

	return render_template("login.html", title="Login")

@app.route("/logout")
def logout():
	if not current_user.is_authenticated:
		return redirect(url_for("login"))
	logout_user()
	return redirect(url_for("index"))
