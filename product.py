class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Proizvod: {self.name}, Cena: {self.price}, Kolicina: {self.quantity}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Kolicina proizvoda '{self.name}' azurirana na {self.quantity}.")