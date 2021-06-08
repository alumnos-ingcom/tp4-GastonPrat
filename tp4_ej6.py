################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 6
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto
from random import randint

def minimo(valores):
    lista = []
    if valores == 1:
        lista.append(randint(1, 100))
        valor_minimo = lista[0]
        lista = tuple(lista)
        return valor_minimo, lista, valores
    elif valores < 1:
        raise IngresoIncorrecto("La lista debe contener"
                                " un valor o mas")
    for i in range(valores):
        lista.append(randint(1, 100))
    pila = lista
    lista = tuple(lista)
    for n in range(valores-1):
        uno = pila[-1]
        dos = pila[-2]
        if uno < dos:
            valor_minimo = uno
            pila.pop(-2)
        else:
            valor_minimo = dos
            pila.pop(-1)
    return valor_minimo, lista, valores
        
    
def maximo(lista, valores):
    if valores == 1:
        valor_maximo = lista[0]
        return valor_maximo
    pila = list(lista)
    for n in range(valores-1):
        uno = pila[-1]
        dos = pila[-2]
        if uno > dos:
            valor_maximo = uno
            pila.pop(-2)
        else:
            valor_maximo = dos
            pila.pop(-1)
    return valor_maximo
    

def prueba():
    print("Se imprimirá el número más chico de la lista")
    valores = ingreso_entero("¿cuantos valores tendra la lista aleatoria?")
    valor_minimo, lista, valores = minimo(valores)
    print(lista)
    print(f"El valor minimo de las lista es {valor_minimo}")
    
    print("Se imprimirá el número más grande de la lista")
    valor_maximo = maximo(lista, valores)
    print(f"El valor minimo de las lista es {valor_maximo}")

if __name__ == "__main__":
    prueba()
