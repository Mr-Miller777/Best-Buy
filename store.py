import products


class Store:
    """
    Manages a collection of Product objects and
    allows ordering multiple products at once.
    """

    def __init__(self, product_list):
        """
        Initializes the store with a list of products.

        :param product_list: List of products.Product objects
        """
        self.products = product_list

    def add_product(self, product):
        """
        Adds a new product to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.
        Raises a ValueError if the product does not exist.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total number of all items in the store (active and inactive).
        """
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self):
        """
        Returns a list of all active products in the store.
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        """
        Accepts a list of tuples (product, quantity),
        purchases the products, and returns the total price.

        May raise exceptions from the Product.buy() method if, for example,
        a product is inactive or the quantity is unavailable.

        :param shopping_list: List of (products.Product, int)
        :return: Total price (float)
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity) # buy can raise a ValueError.
        return total_price
