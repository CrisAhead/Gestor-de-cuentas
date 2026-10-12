import sys
import json

try:
    with open("usuarios.json", "r") as archivo:
        lista_usuarios = json.load(archivo)
except FileNotFoundError:
    lista_usuarios = []

while True:
    opc = input("Ingrese una opción (1 para agregar usuario, 0 para salir): ")
    match opc:
        case "1":
            usuario = input("Ingrese su usuario: ")
            if usuario in lista_usuarios:
                print("Usuario ya existe.")
            else:
                lista_usuarios.append(usuario)
                with open("usuarios.json", "w") as archivo:
                    json.dump(lista_usuarios, archivo)
                print("Usuario agregado correctamente.")
        case "0":
            print("Saliendo del programa.")
            sys.exit()
        case _:
            print("Opción no válida. Saliendo del programa.")
            sys.exit()    