def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def menu():
    print("¡Bienvenido al verificador de números primos!")
    print("Seleccione una opción:")
    print("1. Verificar un número")
    print("2. Detener el programa")
    print("3. Obtener información adicional")

def obtener_info_adicional():
    print("Los números primos son aquellos que solo son divisibles por 1 y por sí mismos.")
    print("Este aplicativo fue creado por [Javy Jhosua].")

def main():
    while True:
        menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            numero = int(input("Ingrese el número que desea verificar: "))
            if es_primo(numero):
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
        elif opcion == "2":
            print("Gracias por usar el verificador de números primos. ¡Adiós!")
            break
        elif opcion == "3":
            obtener_info_adicional()
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if _name_ == "_main_":
    main()





import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Bienvenido al Generador de Contraseñas Seguras.")
    print("Este programa te permite generar contraseñas seguras según tus preferencias.")

    while True:
        try:
            length = int(input("Ingresa la longitud de la contraseña deseada: "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido para la longitud.")

    use_uppercase = input("¿Deseas incluir mayúsculas en la contraseña? (s/n): ").lower() == 's'
    use_lowercase = input("¿Deseas incluir minúsculas en la contraseña? (s/n): ").lower() == 's'
    use_digits = input("¿Deseas incluir números en la contraseña? (s/n): ").lower() == 's'
    use_symbols = input("¿Deseas incluir símbolos en la contraseña? (s/n): ").lower() == 's'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    print("Contraseña generada:", password)

    while True:
        choice = input("¿Deseas generar otra contraseña? (s/n): ").lower()
        if choice == 'n':
            print("¡Hasta luego!")
            break
        elif choice != 's':
            print("Por favor, ingresa 's' para generar otra contraseña o 'n' para salir.")

if _name_ == "_main_":
    main()