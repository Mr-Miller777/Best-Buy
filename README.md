# 🛒 Tech Store Management System

A simple command-line store management system for a tech shop (like Best Buy).  
Built with Python, it allows you to manage products, view inventory, and place orders.

## 📁 Project Structure

```
Best_Buy/
 ├── products.py # Product class definition
 ├── store.py # Store class definition
 └── main.py # User interface and entry point
 ```

## 📦 Features

- **Product management** – add, remove, activate/deactivate products.
- **Inventory tracking** – view stock levels and total quantities.
- **Order processing** – place orders for multiple products at once.
- **Command-line interface** – simple menu-driven user experience.

## ⚙️ Setup & Running

1. Make sure you have **Python 3.10+** installed.
2. Clone or download the project files.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python main.py
```
5. No external libraries are required.

## 🖥 Usage

When you run main.py, you'll see a menu with four options:

```
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

 - Option 1: Lists all active products with prices and quantities.

 - Option 2: Shows the total number of items in the store (including inactive items).

 - Option 3: Starts an interactive ordering process:

   - Displays available products.

   - Prompts you to enter product numbers and quantities.

   - Leave the input empty to finish the order.

   - Displays the total payment.

 - Option 4: Exits the program.


## 🧱 Class Overview

 - Product (in products.py)
    - Attributes: name, price, quantity, active
    - Key methods: buy(), set_quantity(), activate()/deactivate(), show()
    - Raises ValueError for invalid operations.

 - Store (in store.py)
    - Holds a list of Product objects.
    - Key methods: add_product(), remove_product(), get_total_quantity(), get_all_products(), order()

## 📋 Example Session

```
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: 1
------
1. MacBook Air M2, Price: $1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: $250, Quantity: 500
3. Google Pixel 7, Price: $500, Quantity: 250
------

Please choose a number: 3
...
Which product # do you want? 1
What amount do you want? 1
Product added to list!

Which product # do you want? 2
What amount do you want? 2
Product added to list!

Which product # do you want?
What amount do you want?
********
Order made! Total payment: $1950
```

## 📄 License

This project is for educational purposes. Feel free to modify and extend it.