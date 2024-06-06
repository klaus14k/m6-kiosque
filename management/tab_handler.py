from menu import products

def calculate_tab (tab_list: list[dict]):
    subtotal = 0
    for i in products:
        for j in tab_list:
            if i.get("_id") == j.get("_id"):
                subtotal = subtotal + (i.get("price") * j.get("amount"))
    return {"subtotal": f"${round(subtotal, 2)}"}