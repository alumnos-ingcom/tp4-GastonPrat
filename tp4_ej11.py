################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import IngresoIncorrecto

def es_palindromo(texto, ignorar_espacios=False, ignorar_mayusculas=False):
    str(texto)
    if ignorar_espacios:
        return texto
    else:
        texto = texto.replace(" ", "")
    if ignorar_mayusculas:
        return texto
    else:
        texto = texto.lower()
    inversa = texto[::-1]
    palindromo = inversa == texto
    return palindromo    
    
def prueba():
    texto = input("Ingrese una frase o palabra: ")
    palindromo = es_palindromo(texto)
    if palindromo == True:
        print(f"la palabra o frase {texto} es un Palíndromo")
    else:
        print(f"{texto} no es un Palíndromo")

    
if __name__ == "__main__":
    prueba()