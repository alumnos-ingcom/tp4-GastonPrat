################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 7
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def division_lenta(dividendo, divisor):
    if divisor > 0:
        cociente = 0
        resto = dividendo
        resultados = []
        while divisor <= resto:
            resto = resto - divisor
            cociente = cociente +1
            msj = f"Resto={resto} / Cociente={cociente}"
            resultados.append(msj)
        else:
            msj = f"Resto={resto} / Cociente={cociente}"
            resultados.append(msj)
#     elif dividendo < divisor:
#         msj = "el dividendo es menor al divisor, intente otra vez"
#         return msj
    else:
        raise IngresoIncorrecto("El divisor no puede ser cero")
    return resultados

def prueba():
    dividendo = ingreso_entero("Ingrese un número entero")
    divisor = ingreso_entero("ingresa un número entero que sera su divisor")
    resultados = division_lenta(dividendo, divisor)
    for item in(resultados):
        print(item)   
    

if __name__ == "__main__":
    prueba()