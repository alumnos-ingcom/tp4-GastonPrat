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
    
    print(texto == inversa)
        
    
def prueba():
    print("Se indicara si una palabra o frase es un Palindromo")
    es_palindromo(input("Ingrese una palabra o frase: "))
    
if __name__ == "__main__":
    prueba()