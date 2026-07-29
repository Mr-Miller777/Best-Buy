class Product:
    """
    Represents a product available in the store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new product.
        Raises an exception if the name is empty or
        the price or quantity is negative.
        """
        if not name or not isinstance(name, str):
            raise ValueError("The product name must not be empty.")
        if price < 0:
            raise ValueError("The price must not be negative.")
        if quantity < 0:
            raise ValueError("The quantity must not be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Resets the stock quantity.
        If the quantity reaches 0, the product is deactivated.
        """
        if quantity < 0:
            raise ValueError("The quantity must not be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """
        Outputs a user-friendly representation of the product to the console.
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Purchases a specific quantity of the product.
        Returns the total price (float).
        Reduces the stock level accordingly.
        Raises an exception if:
        - the product is not active,
        - the requested quantity is not positive,
        - there is insufficient stock.
        """
        if not self.active:
            raise ValueError("The product is not active and cannot be purchased.")
        if quantity <= 0:
            raise ValueError("The purchase quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError(f"Insufficient stock."
                             f"Available: {self.quantity}, requested: {quantity}.")

        total_price = self.price * quantity
        self.quantity -= quantity

        # Deactivate product when stock drops to 0
        if self.quantity == 0:
            self.deactivate()

        return total_price


