from app import app
from app.models import Brand, Product

from flask import Blueprint

#
# API ROUTES
#

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

@api_blueprint.route("/brands")
def apiBrands():
	brands = [{
		"id": b.id,
		"name": b.name,
		"country": b.country
	} for b in Brand.query.all()]
	return {"brands": brands}

@api_blueprint.route("/brands/<id>")
def apiBrand(id):
	b = Brand.query.get(id)
	if not b:
		return {"error": "Brand not found"}, 404 # 404 Not Found
	return {
		"id": b.id,
		"name": b.name,
		"country": b.country
	}


@api_blueprint.route("/products")
def apiProducts():
	products = [{
		"id": p.id,
		"name": p.name,
		"brand_id": p.brand_id,
		"seller_id": p.user_id,
		"category": p.category.name,
		"condition": p.condition.name,
		"price": float(p.price),
		"stock": p.stock,
		"year": p.year,
	} for p in Product.query.all()]
	return {"products": products}

@api_blueprint.route("/products/<id>")
def apiProduct(id):
	p = Product.query.get(id)
	if not p:
		return {"error": "Product not found"}, 404 # 404 Not Found
	return {
		"id": p.id,
		"name": p.name,
		"brand_id": p.brand_id,
		"seller_id": p.user_id,
		"category": p.category.name,
		"condition": p.condition.name,
		"price": float(p.price),
		"stock": p.stock,
		"year": p.year,
	}
