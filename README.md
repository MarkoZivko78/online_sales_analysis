# Online Sales Analysis

Python projekat za analizu prodajnih podataka online prodavnice.

## Klase

### Product (`product.py`)
- Atributi: name, price, quantity
- Metodi: display_info(), update_quantity()

### ProductManager (`product_manager.py`)
- Atribut: products (lista)
- Metodi: add_product(), display_all_products(), total_inventory_value(), remove_product()

### Cart (`cart.py`)
- Atribut: cart_items (lista)
- Metodi: add_to_cart(), total_cart_value(), display_cart()

## Pokretanje
```bash
python main.py