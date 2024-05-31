import os

usuario_prueba = {
    "nombre": "Christian",
    "clave": "1234abcd"
}

def validarUsuario(nombre, clave):
    pass

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
    