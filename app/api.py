from app import app
from app.models import Brand, Product

from flask import Blueprint, request

#
# API ROUTES
#

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

@api_blueprint.route("/brands")
def apiBrands():
	page = request.args.get("page", 1, type=int)
	query = Brand.query.paginate(per_page=2, page=page)

	brands = [{
		"id": b.id,
		"name": b.name,
		"country": b.country
	} for b in query.items]

	return {
		"brands": brands,
		"page": query.page,
		"pages": query.pages,
		"total": query.total
	}

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
	page = request.args.get("page", 1, type=int)
	query = Product.query.paginate(per_page=2, page=page)

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
	} for p in query.items]

	return {
		"products": products,
		"page": query.page,
		"pages": query.pages,
		"total": query.total
	}

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
