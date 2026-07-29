import products
import store


def start(store_obj):
    """
    Launches the user interface for the store.
    Displays a menu and processes user input.
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            active_products = store_obj.get_all_products()
            if not active_products:
                print("No active products available.")
            else:
                print("------")
                for i, product in enumerate(active_products, start=1):
                    print(f"{i}. {product.name}, Price: ${product.price}, "
                          f"Quantity: {product.quantity}")
                print("------")

        elif choice == "2":
            total_qty = store_obj.get_total_quantity()
            print(f"Total of {total_qty} items in store")

        elif choice == "3":
            active_products = store_obj.get_all_products()
            if not active_products:
                print("No active products available for ordering.")
                continue

            print("------")
            for i, product in enumerate(active_products, start=1):
                print(f"{i}. {product.name}, Price: ${product.price}, "
                      f"Quantity: {product.quantity}")
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []
            while True:
                product_num_str = input("Which product # do you want? ").strip()
                if product_num_str == "":
                    break

                quantity_str = input("What amount do you want? ").strip()
                if quantity_str == "":
                    break

                # Validation of inputs
                try:
                    product_index = int(product_num_str) - 1
                    quantity = int(quantity_str)
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    continue

                if product_index < 0 or product_index >= len(active_products):
                    print("Invalid product number. Please try again.")
                    continue

                selected_product = active_products[product_index]

                if quantity <= 0:
                    print("Quantity must be positive. Please try again.")
                    continue

                if quantity > selected_product.quantity:
                    print(f"Not enough stock. Available: {selected_product.quantity}. "
                          f"Please try again.")
                    continue

                # All valid → add to cart
                shopping_list.append((selected_product, quantity))
                print("Product added to list!\n")

            # Submit order if the shopping cart is not empty.
            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${total_price}")
                except ValueError as e:
                    print(f"Error processing order: {e}")
            else:
                print("No products ordered.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-4.")



if __name__ == "__main__":
    # Create test products
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
