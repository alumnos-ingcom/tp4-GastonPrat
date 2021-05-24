################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 4
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def compara(numero1, numero2):
    if numero1 < numero2:
        resultado = -1
        return resultado
    elif numero1 == numero2:
        resultado = 0
        return resultado
    else:
        resultado = 1
        return resultado

def prueba():
    print("Este programa compara dos números ingresados")
    numero1 = ingreso_entero("Ingrese un Número Entero")
    numero2 = ingreso_entero("Ingrese otro Número Entero")
    resultado = compara(numero1, numero2)
    print(resultado)

if __name__ == "__main__":
    prueba()
