def format_price(price):
    """Format the price to two decimal places."""
    return f"${price:.2f}"

def parse_product_data(product_data):
    """Parse product data from JSON and return a list of products."""
    products = []
    for item in product_data:
        products.append({
            "name": item.get("name"),
            "price": format_price(item.get("price")),
            "description": item.get("description", "")
        })
    return products

def validate_email(email):
    """Validate the email format."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def generate_unique_id():
    """Generate a unique identifier for products or users."""
    import uuid
    return str(uuid.uuid4())