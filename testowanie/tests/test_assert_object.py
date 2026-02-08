class Order:
    def __init__(self, customer_type):
        self.items = {}  # Change items to a dict
        self.customer_type = customer_type  # 'regular', 'premium', or 'wholesale'

    def add_item(self, product, quantity):
        # Use product name as key for simplicity; real code might use a product id
        self.items[product.name] = {"product": product, "quantity": quantity}

    def calculate_total(self):
        subtotal = sum(item["product"].price * item["quantity"] for item in self.items.values())

        if self.customer_type == "premium":
            return subtotal * 0.9  # 10% discount
        elif self.customer_type == "wholesale":
            return subtotal * 0.75  # 25% discount
        return subtotal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class OrderAssert:
    def __init__(self, order):
        self.order = order

    def has_total_price(self, expected_price):
        assert self.order.calculate_total() == expected_price
        return self

    def has_item_count(self, expected_count):
        assert len(self.order.items) == expected_count
        return self

    def includes_item(self, product_name, quantity):
        assert self.order.items.get(product_name, {}).get("quantity") == quantity
        return self


def test_premium_customer_gets_10_percent_discount():
    # Given
    order = Order(customer_type="premium")

    # When
    order.add_item(Product(name="Product 1", price=100), quantity=1)
    order.add_item(Product(name="Product 2", price=200), quantity=2)

    # Then
    OrderAssert(order) \
        .has_total_price(450) \
        .has_item_count(2) \
        .includes_item("Product 1", 1) \
        .includes_item("Product 2", 2)