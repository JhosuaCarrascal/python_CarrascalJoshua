# Diccionario de productos disponibles
productos = {
    "Manzana": {"Precio": 10, "Cantidad": 12},
    "Pera": {"Precio": 15, "Cantidad": 8},
    "Mango": {"Precio": 8, "Cantidad": 7}
}

# Carrito de compras y total inicial
carrito = {}
total = 0

# Función para agregar productos al carrito
def agregar_al_carrito(producto, cantidad):
    global total
    if producto in productos and productos[producto]["Cantidad"] >= cantidad:
        productos[producto]["Cantidad"] -= cantidad
        if producto in carrito:
            carrito[producto] += cantidad
        else:
            carrito[producto] = cantidad
        total += productos[producto]["Precio"] * cantidad
        print("Producto agregado")
    else:
        print("Producto no disponible")

# Función para mostrar el carrito
def mostrar_carrito():
    for producto, cantidad in carrito.items():
        print(f"{producto}: {cantidad} unidades")
    print(f"Total a pagar: {total}")

# Ejemplo de uso
agregar_al_carrito("Manzana", 3)
mostrar_carrito()