from flask import Blueprint, request, jsonify
from bson import ObjectId
from db import products_col
from utils import serialize

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/search')
def search_product():
    q = request.args.get('q', '')
    result = products_col.find({"name":{"$regex":q, "$options":"i"}})
    return jsonify([serialize(p) for p in result])

@routes_blueprint.route('/like', methods=["POST"])
def like_product():
    data = request.get_json()
    product_id = data.get("product_id")
    products_col.update_one(
        {"_id": ObjectId(product_id)},
        {"$inc": {"likes":1}}
    )
    return jsonify({"message":"Product liked!"})

@routes_blueprint.route('/popular-products')
def find_popular():
    results = products_col.find().sort("likes", -1).limit(5)
    return jsonify([serialize(p) for p in results])