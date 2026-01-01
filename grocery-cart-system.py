class GrocerySite:
    def __init__(self):
        self.cart_items = {}
        self.catalog = {
            "bananas": 0.60,
            "apples": 1.50,
            "oranges": 1.40,
            "strawberries": 2.50
        }

    def view_grocery_catalog(self):
        catalog = self.catalog

        print("=================================================")
        print("          🍒🍓 GROCERY CATALOG 🍓🍒")
        print("=================================================")

        for item in catalog:
            print("---------------------------------------------")
            print(f"        {item} |  ${catalog[item]}")
            print("---------------------------------------------")
            print("                            + add to cart")
            print()

    def cart_data(self, product, action):
        unit_price = self.catalog[product]

        if action == "add":
            if product not in self.cart_items:
                self.cart_items[product + " quantity"] = 1
                self.cart_items[product] = unit_price * self.cart_items[product + " quantity"]
            else:
                self.cart_items[product + " quantity"] += 1
                self.cart_items[product] = unit_price * self.cart_items[product + " quantity"]

        if action == "unadd":
            self.cart_items[product + " quantity"] -= 1
            self.cart_items[product] = unit_price * self.cart_items[product + " quantity"]

            if self.cart_items[product + " quantity"] == 0:
                del self.cart_items[product]
                del self.cart_items[product + " quantity"]

    def add_to_cart(self, add):
        item = add.lower()

        if item in self.catalog:
            self.cart_data(item, "add")
        else:
            print()
            print("Sorry we don't have this product in stock ('-')")
            print()

    def unadd_from_cart(self, unadd):
        item = unadd.lower()

        if item in self.cart_items:
            self.cart_data(item, "unadd")
        else:
            print()
            print("Sorry we don't have this product in stock ('-')")
            print()

    def view_cart(self):
        print("=================================================")
        print("                    CART 🛒                     ")
        print("=================================================")

        if len(self.cart_items) == 0:
            print("           uh oh! your cart is empty :(")
            return

        for item in self.cart_items:
            if " quantity" in item:
                continue

            quantity_key = item + " quantity"
            quantity = self.cart_items.get(quantity_key, 0)
            price = self.cart_items[item]

            print("---------------------------------------------")
            print(f"        {item} |  ${price}")
            print("---------------------------------------------")
            print(f"                            - [{quantity}] +")
            print()


def main():
    site = GrocerySite()

    site.view_grocery_catalog()

    site.add_to_cart("bananas")
    site.add_to_cart("bananas")
    site.add_to_cart("bananas")
    site.add_to_cart("bananas")

    site.view_cart()

    site.unadd_from_cart("bananas")

    site.view_cart()


main()


