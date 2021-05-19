################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto
class IngresoIncorrecto(Exception):
    pass

def compara(numero1, numero2):
    numero1 = ingreso_entero(numero1)
    numero2 = ingreso_entero(numero2)
    if numero1 < numero2:
        return -1
    elif numero1 == numero2:
        return 0
    else:
        return 1


def prueba():
    print(compara("Ingrese un numero entero", "ingrese otro numero entero"))

if __name__ == "__main__":
    prueba()