################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero, IngresoIncorrecto

def suma_lenta(numero, otro_numero):
        resultado = numero + otro_numero
        lista = []
        if numero < otro_numero:
            contador = numero
            while contador <= resultado:
                lista.append(contador)
                contador = contador +1
        else:
            contador = otro_numero
            while contador <= resultado:
                lista.append(contador)
                contador = contador +1
        return lista



def prueba():
    numero = ingreso_entero("Ingrese un Número Entero")
    otro_numero = ingreso_entero("Ingrese otro Número Entero")
    lista = suma_lenta(numero, otro_numero)
    print(lista)
    
if __name__ == "__main__":
    prueba()
    
