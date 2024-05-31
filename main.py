import os

from usuarios import cargarUsuario

opcion = ''
menu = """
*** Menú ***
1 - Ingresar
2 - Salir
"""

while opcion != "2":
    print(menu)
    opcion = input("Su opción >>> ")
    
    if opcion == "1":
        cargarUsuario()
    elif opcion == "2":
        print("Hasta luego!")
    else:
        print("Opción incorrecta!")
        input("ENTER para continuar.")
        os.system('cls')