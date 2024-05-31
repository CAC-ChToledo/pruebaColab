"""
Módulo para ingreso y validación de usuarios.
"""


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
    return validarUsuario(nombre, clave, usuario_prueba)   