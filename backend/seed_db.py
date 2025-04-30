from db import products_col

products_col.delete_many({}) # deletes any previously existing product in the db

# initialization of the database with some products
products = [
    {
        "name": "Nike Air Max 90",
        "category": "shoes",
        "brand": "Nike",
        "price": 120,
        "image_url": "",
        "likes": 0,
        "description": "Classic and comfortable sneakers."
    },
    {
        "name": "Adidas Ultraboost",
        "category": "shoes",
        "brand": "Adidas",
        "price": 150,
        "image_url": "",
        "likes": 0,
        "description": "High-performance running shoes for daily use."
    },
    {
        "name": "Levi's Denim Jacket",
        "category": "jackets",
        "brand": "Levi's",
        "price": 90,
        "image_url": "",
        "likes": 0,
        "description": "Stylish and durable denim jacket for all seasons."
    },
    {
        "name": "North Face Hoodie",
        "category": "hoodies",
        "brand": "The North Face",
        "price": 80,
        "image_url": "",
        "likes": 0,
        "description": "Warm and cozy hoodie perfect for chilly days."
    },
    {
        "name": "Converse Chuck Taylor",
        "category": "shoes",
        "brand": "Converse",
        "price": 75,
        "image_url": "",
        "likes": 1,
        "description": "Timeless canvas sneakers with a classic look."
    }
]

products_col.insert_many(products)

print(f"✅ {len(products)} products were added succesfully.")