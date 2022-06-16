from crypt import methods
from app import app, db
from app.models import User, Brand, ProductCategory, ProductCondition, Product

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

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
@login_required
def logout():
	logout_user()
	return redirect(url_for("index"))


@app.route("/products")
def viewProducts():
	return render_template("products.html",
		title="Products",
		products=Product.query.all()
	)

@app.route("/products/<id>")
def viewProduct(id):
	p = Product.query.get(id)
	if not p:
		flash("Product not found", "danger")
		return redirect(url_for("viewProducts"))
	return render_template("product.html", title="Product",	product=p)

@app.route("/products/create", methods=["GET", "POST"])
@login_required
def createProduct():
	if request.method == "POST":
		print(request.form.get("freeshipping"))
		try:
			p = Product(
				int(request.form.get("brand")),
				current_user.id,
				request.form.get("name"),
				float(request.form.get("price")),
				int(request.form.get("stock")),
				int(request.form.get("year")),
				bool(request.form.get("freeshipping")), # TODO: arreglar
				ProductCategory(int(request.form.get("category"))),
				ProductCondition(int(request.form.get("condition")))
			)
			db.session.add(p)
			db.session.commit()
			flash("Product created!", "success")
		except Exception as e:
			print(e)
			flash("Error creating product", "danger")
		finally:
			db.session.rollback()

	return render_template("createProduct.html",
		title="Create Product",
		brands=Brand.query.all(),
		categories=list(ProductCategory),
		conditions=list(ProductCondition)
	)
