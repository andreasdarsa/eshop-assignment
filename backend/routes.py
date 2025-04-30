from flask import Blueprint, request, jsonify
from bson import ObjectId
from db import products_col
from utils import serialize

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/search')
def search_product():
    q = request.args.get('q', '')
    # search inside the database for the items requested
    # search is case-insensitive in order to make searching products easier for the users
    result = products_col.find({"name":{"$regex":q, "$options":"i"}})
    return jsonify([serialize(p) for p in result])

@routes_blueprint.route('/like', methods=["POST"])
def like_product():
    data = request.get_json()
    product_id = data.get("product_id")
    # increases the like counter by one in the product with the given id
    # if the product doesn't have a like counter, the field is created by the db and the counter is set to 1
    products_col.update_one(
        {"_id": ObjectId(product_id)},
        {"$inc": {"likes":1}}
    )
    return jsonify({"message":"Product liked!"})

@routes_blueprint.route('/popular-products')
def find_popular():
    # the product list is sorted, in decreasing order of likes, in order to find the most liked products
    # limit(5) gets the 5 most liked ones
    results = products_col.find().sort("likes", -1).limit(5)
    return jsonify([serialize(p) for p in results])