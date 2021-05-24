################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def ordenar_mayor_a_menor(uno, dos, tres):
    mayor_menor = []
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
                mayor_menor.append(uno)
        else:
            mayor_menor.append(tres)
            mayor_menor.append(dos)
            mayor_menor.append(uno)
    return tuple(mayor_menor)

def ordenar_menor_a_mayor(uno, dos, tres):
    menor_mayor = []
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
                menor_mayor.append(uno)
        else:
            menor_mayor.append(tres)
            menor_mayor.append(dos)
            menor_mayor.append(uno)
    return tuple(menor_mayor)
def prueba():
    print("El siguiente programa imprimirá los numero de Mayor a Menor")
    uno = ingreso_entero("Ingrese un Número Entero")
    dos = ingreso_entero("Ingrese otro Número Entero")
    tres = ingreso_entero("Ingrese el último Número Entero")
    mayor_menor = ordenar_mayor_a_menor(uno, dos, tres)
    print(mayor_menor)
    
    print("El siguiente programa imprimirá los numero de Menor a Mayor")
    uno = ingreso_entero("Ingrese un Número Entero")
    dos = ingreso_entero("Ingrese otro Número Entero")
    tres = ingreso_entero("Ingrese el último Número Entero")
    menor_mayor = ordenar_menor_a_mayor(uno, dos, tres)
    print(menor_mayor)
    

if __name__ == "__main__":
    prueba()
