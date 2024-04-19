import os

class ShoppingCart:
    def _init_(self):
        self.products = {
            "Manzana": {"Nombre": "Manzana", "Precio": 10, "Cantidad": 12},
            "Pera": {"Nombre": "Pera", "Precio": 15, "Cantidad": 8},
            "Mango": {"Nombre": "Mango", "Precio": 8, "Cantidad": 7}
        }
        self.cart = {}
        self.total = 0

    def display_menu(self):
        os.system("clear")
        print("-----------------CARRITO DE COMPRAS--------------------\\n")
        print("             Estos son nuestros productos\\n")
        for product, details in self.products.items():
            print(f"|{product.ljust(8)}| {details['Precio']} COP C/U | {details['Cantidad']} |")
        print("\\n1. Agregar al carrito")
        print("2. Ver estado del carrito")
        print("3. Salir\\n")

    def add_to_cart(self):
        quantity = int(input("Cuantos productos va a comprar\\n"))
        for _ in range(quantity):
            item = input("Elija un artículo\\n")
            if item in self.products and self.products[item]["Cantidad"] >= quantity:
                self.products[item]["Cantidad"] -= quantity
                if item in self.cart:
                    self.cart[item]["Cantidad"] += quantity
                else:
                    self.cart[item] = self.products[item].copy()
                    self.cart[item]["Cantidad"] = quantity
                self.total += self.products[item]["Precio"] * quantity
                print("Producto agregado al carrito")
            else:
                print("Lo siento, este artículo está agotado.")
            input("Para continuar presione enter.")

    def view_cart(self):
        for item, details in self.cart.items():
            print(f"Nombre: {details['Nombre']}, Precio: {details['Precio']}, Cantidad: {details['Cantidad']}")
        print("El total de compra es: ", self.total)
        input("Para continuar presione enter.")

    def run(self):
        while True:
            self.display_menu()
            option = int(input("Elige una opción(1-3)\\n"))
            if option == 1:
                self.add_to_cart()
            elif option == 2:
                self.view_cart()
            elif option == 3:
                break

# Crear una instancia de ShoppingCart y ejecutarla
shopping_cart = ShoppingCart()
shopping_cart.run()