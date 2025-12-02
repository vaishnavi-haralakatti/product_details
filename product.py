# product.py

def format_product_details(product_id, name, quantity, price):
    """
    Returns product information in a well-formatted string.
    """
    return (
        f"Product Details:\n"
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: rs {price:.2f}"
    )


# Example usage (optional)
if __name__ == "__main__":
    print(format_product_details(101, "Keyboard", 5, 499.99))
