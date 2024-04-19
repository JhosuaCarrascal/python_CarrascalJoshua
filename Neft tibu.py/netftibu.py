from os import system


usuario = []
contraseña = []
precio = [144.00]

sel=0 # Le damos valor a nuestra varible sel-eccion para asi poder ejecutarla en nuestro while 
while sel!=4: # Hacemos un while para hacer un bucle a nuestras tres opciones 
    system("cls") # Colocamos un limpiar pantalla



    print(
      "----------Bienvenido a Neftibu-----------"
    "Que deseas hacer?"
 "1. iniciar sesion."
 "2. comprar una credencial."
 "3. añadir el dinero a la cuenta bancaria."
 "4. ¿desea terminar el programa."
    )


    sel=int(input("digita el numero de lo primero que deseaas hacer:/n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opciones.

    print("")
    print("--------SUBCRIPCIONES--------")
    print("subcripcion:premium")
    print("resumen:año")
    print("precio=144.000")

    oferta = {
     
         "subcripcion":"premium",
         "resumen":"esta subcripcion tiene beneficio por un año",
         "precio": 144.000
   }
