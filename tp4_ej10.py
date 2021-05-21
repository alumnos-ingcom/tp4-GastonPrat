################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def factores_primos(numero):
    numero = ingreso_entero(numero)
    primos = []
    for i in range(2, numero+1):
        while numero % i == 0:
            primos.append(i)
            numero = numero / i
    return tuple(primos)

def prueba():
    print("El siguiente programa arroja los factores primos")
    print(factores_primos("Ingrese un Número Entero"))
    
if __name__ == "__main__":
    prueba()

