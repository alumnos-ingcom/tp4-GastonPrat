################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def ordenar_mayor_a_menor(uno, dos, tres):
    mayor_menor = []
    uno = mayor_menor.append(ingreso_entero(uno))
    dos = mayor_menor.append(ingreso_entero(dos))
    tres = mayor_menor.append(ingreso_entero(tres))
    mayor_menor.sort(key=None, reverse=True)
    return tuple(mayor_menor)

def ordenar_menor_a_mayor(uno, dos, tres):
    menor_mayor = []
    uno = menor_mayor.append(ingreso_entero(uno))
    dos = menor_mayor.append(ingreso_entero(dos))
    tres = menor_mayor.append(ingreso_entero(tres))
    menor_mayor.sort(key=None, reverse=False)
    return tuple(menor_mayor)

def prueba():
    print("El siguiente programa imprimirá los numero de Mayor a Menor")
    print(ordenar_mayor_a_menor("Ingresa un Número", "Ingresa un otro "
                                "Número", "Ingresa un el ultimo Número"))
    print("El siguiente programa imprimirá los numero de Menor a Mayor")
    print(ordenar_menor_a_mayor("Ingresa un Número", "Ingresa un otro "
                                "Número", "Ingresa un el ultimo Número"))

if __name__ == "__main__":
    prueba()
