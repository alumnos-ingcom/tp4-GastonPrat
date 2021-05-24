################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def signo(numero):
    if numero > 0:
        msj = f"el numero {numero} es positivo"
        return msj        
    elif numero == 0:
        msj = f"el numero {numero} es cero"
        return msj
    else:
        msj = f"el numero {numero} es negativo"
        return msj

def prueba():
    print("Este programa le dira si el número es Mayor, Menor o Cero")
    numero = ingreso_entero("Ingrese un Número Entero")
    msj = signo(numero)
    print(msj)

if __name__ == "__main__":
    prueba()