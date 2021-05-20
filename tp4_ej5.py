################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto
class IngresoIncorrecto(Exception):
    pass

def signo(numero):
    numero = ingreso_entero(numero)
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
    print(signo("Ingrese un numero entero"))

if __name__ == "__main__":
    prueba()