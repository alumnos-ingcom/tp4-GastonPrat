################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def ordenar_mayor_a_menor(uno, dos, tres):
    mayor_menor = []
    uno = ingreso_entero(uno)
    dos = ingreso_entero(dos)
    tres = ingreso_entero(tres)
    if uno >= dos:
        if uno >= tres:
            mayor_menor.append(uno)
            if dos >= tres:
                mayor_menor.append(dos)
                mayor_menor.append(tres)
            else:
                mayor_menor.append(tres)
                mayor_menor.append(dos)
        else:
            mayor_menor.append(tres)
            mayor_menor.append(uno)
            mayor_menor.append(dos)
    else:
        if dos >= tres:
            mayor_menor.append(dos)
            if uno >= tres:
                mayor_menor.append(uno)
                mayor_menor.append(tres)
        else:
            mayor_menor.append(tres)
            mayor_menor.append(dos)
            mayor_menor.append(uno)
    return tuple(mayor_menor)

def ordenar_menor_a_mayor(uno, dos, tres):
    menor_mayor = []
    uno = ingreso_entero(uno)
    dos = ingreso_entero(dos)
    tres = ingreso_entero(tres)
    if uno <= dos:
        if uno <= tres:
            menor_mayor.append(uno)
            if dos <= tres:
                menor_mayor.append(dos)
                menor_mayor.append(tres)
            else:
                menor_mayor.append(tres)
                menor_mayor.append(dos)
        else:
            menor_mayor.append(tres)
            menor_mayor.append(uno)
            menor_mayor.append(dos)
    else:
        if dos <= tres:
            menor_mayor.append(dos)
            if uno <= tres:
                menor_mayor.append(uno)
                menor_mayor.append(tres)
        else:
            menor_mayor.append(tres)
            menor_mayor.append(dos)
            menor_mayor.append(uno)
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
