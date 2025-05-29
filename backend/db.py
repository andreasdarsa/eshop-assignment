from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["eshop_db"]
products_col = db["products"]