from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
# The MongoDB we're going to use
db = client["eshop_db"]
# Products saved in our database
products_col = db["products"]