from menu import products
from collections import Counter

def get_product_by_id (id: int):
    if type(id) != int:
        message = "product id must be an int"
        raise TypeError(message)
    else:
        for product in products:
            if product["_id"] == id:
                return product
        return {}

def get_products_by_type (product_type: str):
    if type(product_type) != str:
        message = "product type must be a str"
        raise TypeError(message)
    else:
        filtered_products = []
        for product in products:
            if product["type"] == product_type:
                filtered_products.append(product)
        return filtered_products

def add_product (menu: list, **new_product: dict):
    new_id = 1

    if len(menu) > 0:
        for product in menu:
            if product["_id"] > new_id:
                new_id = product["_id"]
        new_product["_id"] = new_id + 1
        menu.append(new_product)
        return new_product
    else:
        new_product["_id"] = new_id
        menu.append(new_product)
        return new_product
    
def menu_report ():
    product_count = len(products)

    total_price = 0
    for product in products:
        total_price = product["price"] + total_price
    avg_price = round(total_price/product_count, 2)

    filtered_products = []
    for product in products:
        filtered_products.append(product["type"])
        
    most_common_type = list(Counter(filtered_products))
    
    return f"Products Count: {product_count} - Average Price: ${avg_price} - Most Common Type: {most_common_type[0]}"