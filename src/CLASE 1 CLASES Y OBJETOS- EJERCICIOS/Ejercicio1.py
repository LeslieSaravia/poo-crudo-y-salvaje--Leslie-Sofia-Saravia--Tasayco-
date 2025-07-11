from datetime import datetime

class Product:
    def __init__(self, name, price, year_product):
        self.name = name
        self.price = price
        self.year_product = year_product

    def show(self):
        print(f"\nProducto: {self.name}")
        print(f"Precio: S/. {self.price}")
        print(f"Año de compra: {self.year_product}")

    def expired(self):
        year_current = datetime.now().year
        if year_current - self.year_product > 2:
            print("El producto ya expiró.")
            return True
        else:
            print("El producto está en buen estado.")
            return False


def check_products(*products):
    for product in products:
        product.show()


def insert_products():
    list_products = []
    while True:
        print("\n--- Nuevo producto ---")
        name_product = input("Nombre del producto: ")
        price_product = float(input("Precio: "))
        year_product = int(input("Año de compra: "))
        
        product = Product(name_product, price_product, year_product)  
        list_products.append(product)

        otro = input("¿Deseas ingresar otro producto? (s/n): ").lower()
        if otro != 's':
            break
    return list_products


product1 = Product("Leche Gloria", 4.5, 2022)
product2 = Product("Arroz Costeño", 3.0, 2024)


nuevos = insert_products()
print("--- Estado de productos ---")
check_products(product1, product2, *nuevos)
