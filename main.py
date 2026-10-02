from product import Product
from product_manager import ProductManager

pm = ProductManager()

p1 = Product("Laptop", 1200, 3)
p2 = Product("Mis", 25, 50)
p3 = Product("Tastatura", 80, 30)

pm.add_product(p1)
pm.add_product(p2)
pm.add_product(p3)