################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 6
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def minimo(lista):
    lista_min = []
    agregados = 0
    while agregados != 4:
        lista_min.append(ingreso_entero(lista))
        agregados = agregados + 1
    else:
        return min(lista_min)
    
def maximo(lista):
    lista_max = []
    agregados = 0
    while agregados != 4:
        lista_max.append(ingreso_entero(lista))
        agregados = agregados + 1
    else:
        return max(lista_max)

def prueba():
    print("Se imprimirá el número más chico de los 4 ingresados")
    print(minimo("ingresar número a la lista"))
    print("Se imprimirá el número más grande de los 4 ingresados")
    print(maximo("ingresar número a la lista"))
    

if __name__ == "__main__":
    prueba()