################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 6
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def minimo(uno, dos, tres, cuatro):
    lista_min = []
    lista_min.append(uno)
    lista_min.append(dos)
    lista_min.append(tres)
    lista_min.append(cuatro)
    return lista_min
    
    
def maximo(lista):
    lista_max = lista_min
    

def prueba():
    print("Se imprimirá el número más chico de los 4 ingresados")
    uno = ingreso_entero("Ingresa el primer número entero")
    dos = ingreso_entero("Ingresa otro número entero")
    tres = ingreso_entero("Ingresa otro número entero")
    cuatro = ingreso_entero("Ingresa el ultimo número entero")
    lista_min = minimo(uno, dos, tres, cuatro)
    print(f"el numero mas chico es: {min(lista_min)}")
    

    print("Se imprimirá el número más grande de los 4 ingresados")
    print(f"el numero mas grande es: {max(lista_min)}")
    

if __name__ == "__main__":
    prueba()