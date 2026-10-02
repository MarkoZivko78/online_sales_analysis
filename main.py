from product import Product
from product_manager import ProductManager
from cart import Cart

pm = ProductManager()

p1 = Product("Laptop", 1200, 3)
p2 = Product("Mis", 25, 50)
p3 = Product("Tastatura", 80, 30)


pm.add_product(p1)
pm.add_product(p2)

pm.add_product(p3)

pm.add_product(p3)

pm.display_all_products()
pm.total_inventory_value()

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.display_cart()
cart.total_cart_value()

