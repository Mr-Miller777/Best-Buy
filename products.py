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
