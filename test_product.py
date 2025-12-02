# test_product.py

from product import format_product_details

def test_format_product_details():
    result = format_product_details(101, "Keyboard", 5, 499.99)

    expected = (
        "Product Details:\n"
        "Product ID: 101\n"
        "Product Name: Keyboard\n"
        "Quantity: 5\n"
        "Price: ₹499.99"
    )

    assert result == expected
