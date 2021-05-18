################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    pass

def ingreso_entero(mensaje):

    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    
    while cantidad_reintentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto:
            cantidad_reintentos = cantidad_reintentos - 1
            print(f"No ingresaste un numero entero, te quedan {cantidad_reintentos} intentos")
    raise IngresoIncorrecto("Te quedaste sin mas intentos")

def ingreso_entero_restringido(mensaje):
    rango = (int(input("ingrese un valor entre 0 y 10 #")))
    if (rango <= 10 and rango >= 0):
        print(f"El numero ingresado {rango} es correcto")
        return rango
    else:
        print("El nomero ingresado no pertenece al rango entre 0 y 10")
        return rango
    
    
def prueba():
    print(ingreso_entero_reintento("Ingrese un Numero Entero"))
    print(ingreso_entero_restringido("Ingrese un numero entero entre 0 y 10"))

if __name__ == "__main__":
    prueba()