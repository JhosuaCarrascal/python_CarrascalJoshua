import json #Importar Json
from os import system # Importar system para limpiar pantalla
pacientes = [] # Variable que guarda los datos de los pacientes

# Leer archivos Json
with open('doctores.json','r') as openfile:
    doctor = json.load(openfile)

with open('pacientes.json','r') as openfile:
    pacientes = json.load(openfile)


print("------------------------------------------------")
print("      CENTRO MEDICO CARLOS ARDILA LULLE         ")
print("------------------------------------------------")

# Opciones de menú
menu = int(input("¿Qué desea hacer?\n\n1. Iniciar Sesión\n2. Gestionar Cita\n\n"))
print("")

if menu == 1:
    system("cls")

    # Elección de rol
    selec = int(input("Estimado usuario, elija su rol:\n\n1. Paciente\n2. Doctor\n\n"))

    if selec == 1:
        system("cls") # Limpiar pantalla

        print("--------------------------------------------------------------------")
        print("                    Bienvenido a nuestra clínica                    ")
        print("--------------------------------------------------------------------")
        print("")

        print("        Aquí podrás revisar información de tu consulta médica        ")
        print("")

        # Se repite hasta que ingrese un ID correcto o el usuario desee salir
        booleanito = True
        while booleanito == True:

            # Bloques try y except para el manejo de errores
            try:
                print("")
                id_paciente = input("Por favor, ingrese su número de identificación. En caso de querer salir, escriba salir\n")
            
                if id_paciente.lower() == 'salir':
                    break

                id_paciente = int(id_paciente)

            except ValueError:
                print("")
                print("Eso no es un número válido.")

            # Bucle para recorrer pacientes y hacer la validación de datos
            for i in pacientes:

                # Si encuentra el ID realiza los siguientes procedimientos
                if i["identificacion"] == id_paciente:
                    system("cls")

                    print("Identificación: ",i["identificacion"])
                    print("Nombre y Apellido: ",i["nomApe"])
                    print("Número Telefonico: ",i["nfijo"])
                    print("Número Celular: ",i["ncelular"])
                    print("Fecha de Nacimiento: ",i["fnacim"])
                    print("Edad: ",i["age"])
                    print("Género: ",i["genner"])
                    print("Doctor: ",i["doctor"])
                    print("Cita: ",i["fechita"])
                    
                    if 'diagnostico' in i:
                        print("Diagnóstico: ",i["diagnostico"])
                    else:
                        print("Diagnóstico: Aún no disponible")

                    if 'tratamiento' in i:
                        print("Tratamiento: ",i["tratamiento"])
                    else:
                        print("Tratamiento: Aún no disponible")
                    break

            else: #Sino, envía un mensaje
                print("")
                print("El número de identificación no está registrado. Intentalo de nuevo\n")

    if selec == 2:
        system("cls")

        print("---------------------------------------------------------------------")
        print("                          Bienvenido Doctor                          ")
        print("---------------------------------------------------------------------")
        print("")

        print("         Generación de diagnóstico y tratamiento a pacientes         ")
        print("")

        # Se repite hasta que ingrese un ID correcto o el usuario desee salir
        booleanito = True
        while booleanito == True:

            # Bloques try y except para el manejo de errores
            try:
                id_doctor = input("Por favor, ingrese su número de identificación. En caso de querer salir, escriba salir\n")
                print("")

                if id_doctor.lower() == 'salir':
                    break

                id_doctor = int(id_doctor)

            except ValueError:
                print("Eso no es un número válido.")

            # Booleano que cambia su valor una vez encuentra el ID (esto para que no me muestre los no encontrados en cada ciclo que haga)
            find = False
            
            # Bucle para recorrer los datos dentro de "doctores" y hacer la validación de datos
            for i in doctor:
                for x in i["doctores"]:

                    # Si encuentra el ID realiza los siguientes procedimientos
                    if x["id"] == id_doctor:
                        system("cls")
                        print("Bienvenido DR.", x["nombre"])
                        print("")

                        # El nombre del doctor será el relacionado al ID ingresado
                        name_doc = (x["nombre"])

                        # Buscar las citas del doctor
                        citas_doctor = [cita for cita in pacientes if cita["doctor"] == name_doc]

                        # Imprimir las citas del doctor
                        print(f"Citas para el doctor {name_doc}:\n")
                        for i, cita in enumerate(citas_doctor, start=1):
                            print("---------------------------------------------------------------")
                            print(f"{i}. Paciente: {cita['nomApe']}, Fecha: {cita['fechita']}")
                            print("---------------------------------------------------------------")
                            print("")

                        # Solicitar al doctor que elija una cita para diagnosticar
                        print("")
                        eleccion = int(input("Ingrese el número de la cita que desea diagnosticar: "))
                        cita_elegida = citas_doctor[eleccion-1]

                        # Solicitar al doctor que ingrese el diagnóstico
                        diagnostico = input("Por favor, ingrese el diagnóstico para el paciente: ")
                        print("")
                        # Solicitar al doctor que ingrese el tratamiento
                        tratamiento = input("Por favor, ingrese el tratamiento del paciente: ")

                        # Guardar el diagnóstico y tratamiento en la cita
                        cita_elegida["diagnostico"] = diagnostico
                        cita_elegida["tratamiento"] = tratamiento

                        # Guardar las citas en el archivo JSON
                        with open('pacientes.json', 'w') as openfile:
                            json.dump(pacientes, openfile, indent=4)

            # Si no encuentra el ID envía un mensaje            
            if not find:
                print("No hay doctores con esta identificación")
                print("")
                

# Gestión de citas
if menu == 2:
    system("cls")

    # Este bucle se repite mientras "pregunta" sea "si"
    pregunta = "si"
    while pregunta.lower() == "si":

        # Lista de doctores disponibles
        print("Por favor, elija un doctor de la lista:")
        print("")

        # Bucle con dos acumuladores para clave y valor
        for i, especialidad in enumerate(doctor):
            for j, doctorcito in enumerate(especialidad["doctores"]):
                print(f"{i+1}.{j+1}. {doctorcito['nombre']} ({especialidad['especialidad']})")

        print("")
        # Selección de doctor
        eleccion = input("Ingrese el número del doctor que desea elegir: ")

        # Ingreso de número de doctor en formato i.j - i representa el número de especialidad del doctor y j el número del doctor dentro de esa especialidad
        i, j = map(int, eleccion.split(".")) 

        # -1 porque python inicializa desde 0
        doctor_elegido = doctor[i-1]["doctores"][j-1]

        # Ingreso de datos del paciente
        print("Por favor, ingrese los siguientes datos\n")

        id = int(input("Número de identificación\n"))
        print("")
        nameLast = str(input("Nombre y Apellido\n"))
        print("")
        fijo = input("Número telefónico\n")
        print("")
        celular = input("Número Celular\n")
        print("")
        born = input("Fecha de Nacimiento (dd/mm/aaaa)\n")
        print("")
        edad = input("Edad\n")
        print("")
        genero = str(input("Género\n"))
        print("")
        fechita = input("Fecha de la cita\n")
        print("")

        # Diccionario con los datos del nuevo paciente
        citas = {

            "identificacion": id,
            "nomApe": nameLast,
            "nfijo": fijo,
            "ncelular": celular,
            "fnacim": born,
            "age": edad,
            "genner": genero,
            "fechita": fechita,
            "doctor": doctor_elegido["nombre"]
        }

        # Guardar el diccionario dentro de la variable pacientes. Dato: "+=" puede ser un equivalente de ".append"
        pacientes += [citas]

        # Guardar en el archivo Json
        with open('pacientes.json', 'w') as openfile:
            json.dump(pacientes, openfile, indent=4)

        # En caso de ser diferente de si, cierra el programa
        pregunta = input("\n¿Desea agendar otra cita?(si/no)\n")
        if pregunta.lower() != "si":
            bool = False
        break

# Desarrollado por Jhosua Carracal
