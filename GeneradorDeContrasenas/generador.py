import string
import random


def generar_contrasena(longitud):
    #caracteres = string.ascii_letters + string.digits + string.punctuation
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*@_"
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
        #print(contrasena)
    return contrasena

longitud = int(input("Cual es la longitud de la contrasena que deseas generar: "))

nueva_contrasena = generar_contrasena(longitud)
print(f"Tu nueva contrasena es: {nueva_contrasena}") 