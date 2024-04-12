
def calcular_cambio(cantidad):
    denominaciones = [10, 5, 1]
    cambio = []
    for moneda in denominaciones:
        num_monedas = cantidad // moneda
        cantidad -= num_monedas * moneda
        cambio.append((moneda, num_monedas))
    return cambio

print("Bienvenido al cajero automático")
while True:
    cantidad = int(input("Introduce la cantidad de dinero a cambiar: ").split(".")[0])
    if cantidad < 0:
        print("Por favor, introduce una cantidad positiva.")
    elif cantidad == 0:
        print("No hay cambio para esta cantidad.")
    else:
        for moneda, num_monedas in calcular_cambio(cantidad):
            if num_monedas > 0:
                print(f"{num_monedas} monedas de {moneda} dólares")
    if input("¿Deseas cambiar otra cantidad? (si/no): ").lower() != "si":
        break
