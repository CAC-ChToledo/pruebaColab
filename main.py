import os

usuario_prueba = {
    "nombre": "Christian",
    "clave": "1234abcd"
}

def validarUsuario(nombre, clave, usuarios):
    
    if nombre == usuarios.values()[0] and clave == usuarios.values()[1]:
        return True
    
    return False
    

def cargarUsuario():
    nombre = input("Ingrese su nombre: ")
    clave = input("Ingrese su clave: ")
    

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