from db import products_col

products_col.delete_many({})
products = [
    {
        "name": "Nike Air Max 90",
        "category": "shoes",
        "brand": "Nike",
        "price": 120,
        "image_url": "images/nike-air-max-90.jpg",
        "likes": 4,
        "description": "Classic and comfortable sneakers."
    },
    {
        "name": "Adidas Ultraboost",
        "category": "shoes",
        "brand": "Adidas",
        "price": 150,
        "image_url": "images/adidas-ultraboost.jpg",
        "likes": 2,
        "description": "High-performance running shoes for daily use."
    },
    {
        "name": "Levi's Denim Jacket",
        "category": "jackets",
        "brand": "Levi's",
        "price": 90,
        "image_url": "images/levis-denim.jpg",
        "likes": 3,
        "description": "Stylish and durable denim jacket for all seasons."
    },
    {
        "name": "North Face Hoodie",
        "category": "hoodies",
        "brand": "The North Face",
        "price": 80,
        "image_url": "images/north-face-hoodie.jpg",
        "likes": 6,
        "description": "Warm and cozy hoodie perfect for chilly days."
    },
    {
        "name": "Converse Chuck Taylor",
        "category": "shoes",
        "brand": "Converse",
        "price": 75,
        "image_url": "images/converse-chuck-taylor.jpg",
        "likes": 1,
        "description": "Timeless canvas sneakers with a classic look."
    },
    {
        "name": "Puma RS-X",
        "category": "shoes",
        "brand": "Puma",
        "price": 110,
        "image_url": "images/puma-rs-x.jpg",
        "likes": 5,
        "description": "Futuristic sneakers with bold design and comfort."
    },
    {
        "name": "Under Armour Charged",
        "category": "shoes",
        "brand": "Under Armour",
        "price": 100,
        "image_url": "images/under-armour-charged.jpg",
        "likes": 5,
        "description": "Performance running shoes with Charged Cushioning."
    },
    {
        "name": "Columbia Rain Jacket",
        "category": "jackets",
        "brand": "Columbia",
        "price": 85,
        "image_url": "images/columbia-rain-jacket.jpg",
        "likes": 1,
        "description": "Waterproof and breathable jacket for rainy days."
    },
    {
        "name": "Champion Classic Hoodie",
        "category": "hoodies",
        "brand": "Champion",
        "price": 65,
        "image_url": "images/champion-hoodie.jpg",
        "likes": 5,
        "description": "Everyday hoodie with soft cotton blend and iconic logo."
    },
    {
        "name": "New Balance 574",
        "category": "shoes",
        "brand": "New Balance",
        "price": 95,
        "image_url": "images/new-balance-574.jpg",
        "likes": 3,
        "description": "Retro-style sneaker known for comfort and durability."
    },
    {
        "name": "Vans Old Skool",
        "category": "shoes",
        "brand": "Vans",
        "price": 70,
        "image_url": "images/vans-old-skool.jpg",
        "likes": 5,
        "description": "Classic skate shoe with durable canvas and suede."
    },
    {
        "name": "Nike Windrunner Jacket",
        "category": "jackets",
        "brand": "Nike",
        "price": 100,
        "image_url": "images/nike-windrunner.jpg",
        "likes": 1,
        "description": "Lightweight jacket with iconic chevron design."
    },
    {
        "name": "Adidas Trefoil Hoodie",
        "category": "hoodies",
        "brand": "Adidas",
        "price": 75,
        "image_url": "images/adidas-trefoil.jpg",
        "likes": 5,
        "description": "Comfortable hoodie featuring the classic trefoil logo."
    },
    {
        "name": "Timberland 6-Inch Boots",
        "category": "shoes",
        "brand": "Timberland",
        "price": 180,
        "image_url": "images/timberland-6-inch.jpg",
        "likes": 6,
        "description": "Waterproof leather boots built for durability and style."
    },
    {
        "name": "Patagonia Better Sweater",
        "category": "jackets",
        "brand": "Patagonia",
        "price": 120,
        "image_url": "images/patagonia-better-sweater.jpg",
        "likes": 2,
        "description": "Warm, stylish fleece jacket made from recycled materials."
    },
    {
        "name": "Reebok Classic Leather",
        "category": "shoes",
        "brand": "Reebok",
        "price": 80,
        "image_url": "images/reebok-classic.jpg",
        "likes": 2,
        "description": "Versatile sneakers with a clean, classic design."
    },
    {
        "name": "H&M Zip Hoodie",
        "category": "hoodies",
        "brand": "H&M",
        "price": 35,
        "image_url": "images/hnm-zip-hoodie.jpg",
        "likes": 4,
        "description": "Affordable everyday zip hoodie with soft lining."
    },
    {
        "name": "Zara Lightweight Jacket",
        "category": "jackets",
        "brand": "Zara",
        "price": 60,
        "image_url": "images/zara-lightweight.jpg",
        "likes": 3,
        "description": "Stylish lightweight jacket for spring and fall."
    },
    {
        "name": "Fila Disruptor II",
        "category": "shoes",
        "brand": "Fila",
        "price": 85,
        "image_url": "images/fila-disruptor-ii.jpg",
        "likes": 1,
        "description": "Chunky retro sneakers for bold streetwear style."
    },
    {
        "name": "GAP Pullover Hoodie",
        "category": "hoodies",
        "brand": "GAP",
        "price": 50,
        "image_url": "images/gap-pull-hoodie.jpg",
        "likes": 3,
        "description": "Soft and classic pullover hoodie with front logo."
    }
]

products_col.insert_many(products)

print(f"✅ {len(products)} products were added succesfully.")