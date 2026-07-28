
class Store:
    """
    Manages the product catalog and processes orders.
    """

    def __init__(self, name: str = "TechPlanet"):
        """
        :param name: Name of the business
        """
        self.name = name
        self.products = []  # List of all Product objects
        self._next_id = 1  # Auxiliary counter for automatic product IDs

    def add_product(self, name: str, price: float, quantity: int) -> Product:
        """
        Adds a new product and returns it.
        The ID is assigned automatically.
        """
        product = Product(self._next_id, name, price, quantity)
        self._next_id += 1
        self.products.append(product)
        return product

    def list_products(self) -> None:
        """
        Outputs all products available in the shop to the console.
        """
        if not self.products:
            print("There are no products in the range yet.")
            return

        print(f"\n--- Range of {self.name} ---")
        for product in self.products:
            print(product)
        print("-" * 40)

    def place_order(self, product_id: int, quantity: int) -> bool:
        """
        Processes an order: If sufficient stock is available,
        inventory is reduced and a confirmation is issued.

        :param product_id: ID of the desired product
        :param quantity: Order quantity
        :return: True, if the order was successful, otherwise False
        """
        # Search for a product
        product = self._find_product_by_id(product_id)
        if not product:
            print(f"Error: No product with the ID {product_id} found.")
            return False

        if quantity <= 0:
            print("Error: The order quantity must be greater than 0.")
            return False

        if product.reduce_quantity(quantity):
            total = product.price * quantity
            print(f"Order successful: {quantity}x '{product.name}' "
                  f"for a total of {total:.2f} €.")
            return True
        else:
            print(f"Order error: Only {product.quantity} units of "
                  f"'{product.name}' in stock.")
            return False

    def _find_product_by_id(self, product_id: int) -> Product | None:
        """
        Internal helper method to find a product by its ID.
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None


class Product:
    """
    Represents a product in the tech shop.
    """

    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        """
        Initializes a new product.

        :param product_id: Unique product ID
        :param name: Product display name
        :param price: Price in euros (gross)
        :param quantity: Available stock
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_quantity(self, amount: int) -> bool:
        """
        Reduces the stock level by the specified quantity,
        provided sufficient copies are available.

        :param amount: Quantity to be deducted
        :return: True, if the reduction was successful, otherwise False
        """
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            return True
        return False

    def __str__(self) -> str:
        """
        Returns a user-friendly representation of the product.
        """
        return (f"ID {self.product_id:04d}: {self.name:<30} "
                f"{self.price:>8.2f} €  ({self.quantity} in stock)")
