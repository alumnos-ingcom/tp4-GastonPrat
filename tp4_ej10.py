################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def factores_primos(numero):
    primos = []
    for i in range(2, numero+1):
        while numero % i == 0:
            primos.append(i)
            numero = numero / i
    primos = tuple(primos)
    return primos

def prueba():
    print("El siguiente programa arroja los factores primos")
    numero = ingreso_entero("Ingrese un Número entero")
    primos = factores_primos(numero)
    print(f"los Factores primos de {numero} son {primos}")
    
if __name__ == "__main__":
    prueba()

