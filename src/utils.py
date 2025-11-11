thonimport json

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def filter_products_by_price(products, max_price):
    return [product for product in products if product['price'] <= max_price]