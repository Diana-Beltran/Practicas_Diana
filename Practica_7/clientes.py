def mostrar_menu():
    print("\nBienvenido a la base de datos de la empresa KIA")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

clientes = {}

continuar = "si"
while continuar.lower() == "si":
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ")

    if opcion == '1':
        nif = input("NIF: ")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")
        es_preferente = input("¿Cliente preferente? (si/no): ").strip().lower()
        preferente = True if es_preferente == "si" else False

        clientes[nif] = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'preferente': preferente
        }
        print("Cliente añadido correctamente.")

    elif opcion == '2':
        nif = input("Introduce el NIF del cliente a eliminar: ")
        if nif in clientes:
           del clientes [nif]
           print(f"El cliente con NIF {nif} ha sido eliminado")
        else:
            print("Cliente no encontrado.")


    elif opcion == '3':
        nif = input("Introduce el NIF del cliente que deseas ver: ")
        if nif in clientes:
            cliente = clientes[nif]
            print("Datos del cliente:")
            for clave, valor in cliente.items():
                print(f"{clave}: {valor}")
        else:
            print("Cliente no encontrado.")

    elif opcion == '4':
        print("Lista de todos los clientes:")
        for nif, datos in clientes.items():
            print(f"NIF: {nif}, Nombre: {datos['nombre']}")

    elif opcion == '5':
        print("Clientes preferentes:")
        for nif, datos in clientes.items():
            if datos['preferente']:
                print(f"NIF: {nif}, Nombre: {datos['nombre']}")

    elif opcion == '6':
        print("Programa terminado.")
        break

    else:
        print("Opción no válida. Intenta otra vez.")


    if opcion != '6':
        continuar = input("\n¿Deseas hacer otra acción? (si/no): ")
        if continuar.lower() != "si":
            print("Saliendo del programa.")
            break  