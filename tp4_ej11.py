################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):
    str(texto)
    texto = texto.lower()
    texto = texto.replace(" ", "")
    inversa = texto[ : : -1]
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