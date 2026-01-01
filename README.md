# Grocery Cart System

A simple Python grocery cart system that allows users to add and remove items while tracking quantity and total price.

## Features
- View a grocery catalog with fixed prices
- Add items to the cart
- Remove (unadd) items from the cart
- Track quantity per item
- Automatically remove items when quantity reaches zero
- Display current cart contents

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- Dictionaries for data storage

## How It Works
- The grocery catalog stores available items and their prices
- The cart tracks items, quantities, and calculated prices
- Users can add or remove items, and the cart updates accordingly

## Example Usage
```python
site = GrocerySite()
site.view_grocery_catalog()
site.add_to_cart("bananas")
site.view_cart()
site.unadd_from_cart("bananas")
site.view_cart()
