################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 7
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def division_lenta(dividendo, divisor):
    dividendo = ingreso_entero(dividendo)
    divisor = ingreso_entero(divisor)
    if divisor > 0 and dividendo > divisor:
        cociente = 0
        resto = dividendo
        while divisor <= resto:
            resto = resto - divisor
            cociente = cociente +1
            msj = f"Resto={resto} --- Cociente={cociente}"
            print(msj)
        else:
            msj = f"El resto es {resto} y el cociente es {cociente}"
            return msj
    elif dividendo < divisor:
        msj = "el dividendo es menor al divisor, intente otra vez"
        return msj
    else:
        msj = f"No se puede realizar esta operación, intente otra vez"
        return msj

def prueba():
    print(division_lenta("Escriba un número", "Ingrese su divisor"))

if __name__ == "__main__":
    prueba()