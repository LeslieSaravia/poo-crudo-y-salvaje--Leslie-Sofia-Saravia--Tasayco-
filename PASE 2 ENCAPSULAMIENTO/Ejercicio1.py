class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def show(self):
        print(f"Producto: {self.__name}")
        print(f"Precio: S/. {self.__price}")
        print(f"Stock: {self.__stock} unidades")

    def sell(self, units):
        # TELL DON'T ASK
        if units <= self.__stock:
            self.__stock -= units
            print(f"Se vendieron {units} unidades de {self.__name}")
        else:
            print("Stock insuficiente.")

    def update(self, units_more):
        self.__stock += units_more
        print(f"Se repusieron {units_more} unidades de {self.__name}")

prod1 = Product("Chocolate", 5.0, 20)
prod2 = Product("Rosa Artificial", 3.0, 50)
prod3 = Product("Caja Decorativa", 10.0, 10)


prod1.sell(6)
prod2.update(10)
prod3.show()

