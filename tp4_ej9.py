################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 9
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def es_primo(numero_in):
    numero_in = ingreso_entero(numero_in)
    mitad = int(numero_in / 2)
    resto = True
    while mitad > 1:
        resto = numero_in % mitad != 0
        mitad = mitad - 1
    else:
        return resto


def prueba():
    print("Este programa le indicara si el numero ingresado es "
          "un Número Primo")
    print(es_primo("Ingrese un Número Entero"))
    
if __name__ == "__main__":
    prueba()
