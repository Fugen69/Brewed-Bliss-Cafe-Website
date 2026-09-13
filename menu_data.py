"""
Menu data for the Brewed Bliss Café website.
Contains all product categories, items, prices, descriptions, and ratings.
"""

# ─── Coffee Menu ─────────────────────────────────────────────────────────────

COFFEE_MENU = [
    {
        "name": "Classic Espresso",
        "price": 350,
        "description": "A bold, concentrated shot of pure coffee essence with a rich crema.",
        "rating": 4.8,
        "image": "☕",
        "tags": ["Hot", "Strong"],
    },
    {
        "name": "Cappuccino",
        "price": 450,
        "description": "Equal parts espresso, steamed milk, and velvety foam — a timeless classic.",
        "rating": 4.9,
        "image": "☕",
        "tags": ["Hot", "Creamy"],
    },
    {
        "name": "Café Latte",
        "price": 480,
        "description": "Smooth espresso blended with steamed milk and a light layer of foam.",
        "rating": 4.7,
        "image": "☕",
        "tags": ["Hot", "Smooth"],
    },
    {
        "name": "Iced Americano",
        "price": 420,
        "description": "Chilled espresso over ice with cold water — refreshing and robust.",
        "rating": 4.6,
        "image": "🧊",
        "tags": ["Cold", "Refreshing"],
    },
    {
        "name": "Caramel Macchiato",
        "price": 550,
        "description": "Vanilla-infused latte topped with a buttery caramel drizzle.",
        "rating": 4.9,
        "image": "☕",
        "tags": ["Hot", "Sweet"],
    },
    {
        "name": "Mocha Frappe",
        "price": 580,
        "description": "A frozen blend of espresso, chocolate, milk, and whipped cream.",
        "rating": 4.8,
        "image": "🥤",
        "tags": ["Cold", "Chocolate"],
    },
    {
        "name": "Cold Brew",
        "price": 500,
        "description": "Slow-steeped for 18 hours, delivering a smooth, low-acid flavour.",
        "rating": 4.7,
        "image": "🧊",
        "tags": ["Cold", "Strong"],
    },
    {
        "name": "Flat White",
        "price": 470,
        "description": "Velvety microfoam over a double ristretto for the true coffee lover.",
        "rating": 4.8,
        "image": "☕",
        "tags": ["Hot", "Creamy"],
    },
]

# ─── Cashew Flow (Beverages & Fresh Juices) ──────────────────────────────────

CASHFLOW_MENU = [
    {
        "name": "Fresh Orange Juice",
        "price": 380,
        "description": "Freshly squeezed oranges, served chilled with a hint of sunshine.",
        "rating": 4.7,
        "image": "🍊",
        "tags": ["Fresh", "Citrus"],
    },
    {
        "name": "Mango Smoothie",
        "price": 450,
        "description": "Ripe mangoes blended with yogurt and a drizzle of honey.",
        "rating": 4.9,
        "image": "🥭",
        "tags": ["Fresh", "Tropical"],
    },
    {
        "name": "Passion Fruit Cooler",
        "price": 420,
        "description": "Tangy passion fruit mixed with sparkling water and mint leaves.",
        "rating": 4.6,
        "image": "🧃",
        "tags": ["Fresh", "Tangy"],
    },
    {
        "name": "Berry Blast Shake",
        "price": 520,
        "description": "Mixed berries, banana, and almond milk for a nutrient-packed treat.",
        "rating": 4.8,
        "image": "🫐",
        "tags": ["Healthy", "Sweet"],
    },
    {
        "name": "Lime Mint Soda",
        "price": 350,
        "description": "Zesty lime and fresh mint over sparkling soda — ultimate refreshment.",
        "rating": 4.5,
        "image": "🍋",
        "tags": ["Fresh", "Fizzy"],
    },
    {
        "name": "Watermelon Juice",
        "price": 320,
        "description": "Pure watermelon bliss, cold-pressed and naturally sweet.",
        "rating": 4.6,
        "image": "🍉",
        "tags": ["Fresh", "Light"],
    },
    {
        "name": "Avocado Shake",
        "price": 550,
        "description": "Creamy avocado blended with condensed milk — rich and indulgent.",
        "rating": 4.7,
        "image": "🥑",
        "tags": ["Creamy", "Rich"],
    },
    {
        "name": "Iced Lemon Tea",
        "price": 300,
        "description": "Brewed Ceylon tea chilled with fresh lemon and a touch of sugar.",
        "rating": 4.4,
        "image": "🍋",
        "tags": ["Cold", "Classic"],
    },
]

# ─── Short Eats (Snacks & Pastries) ──────────────────────────────────────────

SHORT_EATS_MENU = [
    {
        "name": "Chicken Croissant",
        "price": 480,
        "description": "Flaky butter croissant filled with seasoned chicken and fresh greens.",
        "rating": 4.8,
        "image": "🥐",
        "tags": ["Savoury", "Filling"],
    },
    {
        "name": "Fish Patty",
        "price": 250,
        "description": "Golden-fried pastry stuffed with spiced fish and caramelised onions.",
        "rating": 4.6,
        "image": "🥟",
        "tags": ["Savoury", "Crispy"],
    },
    {
        "name": "Vegetable Samosa",
        "price": 200,
        "description": "Crispy triangles packed with spiced potatoes and garden vegetables.",
        "rating": 4.5,
        "image": "🔺",
        "tags": ["Vegetarian", "Spicy"],
    },
    {
        "name": "Club Sandwich",
        "price": 650,
        "description": "Triple-decker with grilled chicken, bacon, lettuce, and tomato.",
        "rating": 4.9,
        "image": "🥪",
        "tags": ["Filling", "Classic"],
    },
    {
        "name": "Chocolate Muffin",
        "price": 350,
        "description": "Rich, moist chocolate muffin with a molten centre and cocoa dust.",
        "rating": 4.7,
        "image": "🧁",
        "tags": ["Sweet", "Baked"],
    },
    {
        "name": "Egg Mayo Bun",
        "price": 280,
        "description": "Soft bread roll with creamy egg mayonnaise and fresh herbs.",
        "rating": 4.4,
        "image": "🍞",
        "tags": ["Light", "Classic"],
    },
    {
        "name": "Cheese Scone",
        "price": 320,
        "description": "Buttery scone loaded with sharp cheddar and a hint of paprika.",
        "rating": 4.6,
        "image": "🧀",
        "tags": ["Savoury", "Baked"],
    },
    {
        "name": "Butter Cake Slice",
        "price": 300,
        "description": "Classic golden butter cake — dense, buttery, and utterly comforting.",
        "rating": 4.8,
        "image": "🍰",
        "tags": ["Sweet", "Classic"],
    },
]

# ─── Ice Cream ────────────────────────────────────────────────────────────────

ICE_CREAM_MENU = [
    {
        "name": "Vanilla Bean",
        "price": 350,
        "description": "Madagascar vanilla bean ice cream — simple, pure, and irresistible.",
        "rating": 4.7,
        "image": "🍦",
        "tags": ["Classic", "Creamy"],
    },
    {
        "name": "Belgian Chocolate",
        "price": 400,
        "description": "Intense dark chocolate gelato made with real Belgian couverture.",
        "rating": 4.9,
        "image": "🍫",
        "tags": ["Rich", "Chocolate"],
    },
    {
        "name": "Strawberry Swirl",
        "price": 380,
        "description": "Creamy strawberry ice cream with ribbons of real berry compote.",
        "rating": 4.6,
        "image": "🍓",
        "tags": ["Fruity", "Sweet"],
    },
    {
        "name": "Mango Sorbet",
        "price": 350,
        "description": "Dairy-free mango sorbet — refreshing, light, and bursting with flavour.",
        "rating": 4.8,
        "image": "🥭",
        "tags": ["Vegan", "Fruity"],
    },
    {
        "name": "Cookies & Cream",
        "price": 420,
        "description": "Vanilla ice cream packed with chunks of chocolate sandwich cookies.",
        "rating": 4.9,
        "image": "🍪",
        "tags": ["Crunchy", "Classic"],
    },
    {
        "name": "Salted Caramel",
        "price": 450,
        "description": "Buttery caramel gelato with a delicate sea-salt finish.",
        "rating": 4.8,
        "image": "🍮",
        "tags": ["Rich", "Sweet-Salty"],
    },
    {
        "name": "Pistachio",
        "price": 480,
        "description": "Luxurious pistachio gelato made with roasted Sicilian pistachios.",
        "rating": 4.7,
        "image": "🟢",
        "tags": ["Nutty", "Premium"],
    },
    {
        "name": "Sundae Supreme",
        "price": 680,
        "description": "Three scoops, whipped cream, brownie bits, hot fudge, and a cherry on top.",
        "rating": 5.0,
        "image": "🍨",
        "tags": ["Sharing", "Indulgent"],
    },
]

# ─── Testimonials ────────────────────────────────────────────────────────────

TESTIMONIALS = [
    {
        "name": "Amaya P.",
        "role": "Regular Customer",
        "text": "Brewed Bliss is my happy place! The cappuccino is perfection and the short eats are always fresh. I come here every morning without fail.",
        "rating": 5,
    },
    {
        "name": "Dinesh K.",
        "role": "Food Blogger",
        "text": "The attention to detail is incredible — from the latte art to the homemade pastries. Their cold brew is the best in the city, hands down.",
        "rating": 5,
    },
    {
        "name": "Sarah M.",
        "role": "Freelancer",
        "text": "Perfect work-from-cafe spot! Great WiFi, amazing coffee, and the mango smoothie keeps me going through long afternoons.",
        "rating": 5,
    },
    {
        "name": "Ravindu J.",
        "role": "Student",
        "text": "Best ice cream sundaes I've ever had. The Sundae Supreme is absolutely worth every penny. Great vibe for hanging out with friends!",
        "rating": 4,
    },
    {
        "name": "Tanya W.",
        "role": "Architect",
        "text": "The interior design alone is worth the visit, but the food and drinks are what keep me coming back. Love the caramel macchiato!",
        "rating": 5,
    },
]

# ─── Category metadata ───────────────────────────────────────────────────────

CATEGORIES = {
    "coffee": {
        "title": "☕ Coffee",
        "subtitle": "Handcrafted with passion, served with love",
        "description": "From single-origin pour-overs to creamy lattes, every cup is brewed to perfection using ethically sourced beans roasted in-house.",
        "items": COFFEE_MENU,
        "icon": "☕",
        "color": "#C8A27A",
    },
    "cashflow": {
        "title": "🥤 Cash Flow",
        "subtitle": "Fresh juices & refreshing beverages",
        "description": "A flowing selection of freshly squeezed juices, smoothies, and artisan beverages to keep you refreshed and energised all day.",
        "items": CASHFLOW_MENU,
        "icon": "🥤",
        "color": "#7BC67E",
    },
    "short_eats": {
        "title": "🥐 Short Eats",
        "subtitle": "Savoury bites & sweet treats",
        "description": "Freshly baked pastries, crispy snacks, and satisfying sandwiches — perfect for a quick bite or a leisurely afternoon tea.",
        "items": SHORT_EATS_MENU,
        "icon": "🥐",
        "color": "#E8A87C",
    },
    "ice_cream": {
        "title": "🍨 Ice Cream",
        "subtitle": "Scoops of pure happiness",
        "description": "Artisanal gelato and sorbets made fresh daily with premium ingredients. From classic flavours to exotic creations.",
        "items": ICE_CREAM_MENU,
        "icon": "🍨",
        "color": "#D4A5FF",
    },
}
