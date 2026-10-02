from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod '{product.name}' dodat.")

    def display_all_products(self):
        if not self.products:
            print("Nema dostupnih proizvoda.")
            return
        print("\n--- Svi proizvodi ---")
        for p in self.products:
            p.display_info()

    def total_inventory_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"\nUkupna vrednost inventara: {total}")
        return total

    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f"Proizvod '{name}' uklonjen.")
                return
        print(f"Proizvod '{name}' nije pronaden.")