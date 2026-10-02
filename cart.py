class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Proizvod '{product.name}' dodatu u korpu.")

    def total_cart_value(self):
        total = sum(p.price * p.quantity for p in self.cart_items)
        print(f"\nUkupna vrednost korpe: {total}")
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        print("n\--- Sadržaj korpe ---")
        for p in self.cart_items:
            p.display_info() 
