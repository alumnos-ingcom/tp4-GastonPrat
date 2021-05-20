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
        except IngresoIncorrecto as err:
            print(f"No ingresaste un numero entero, te quedan {cantidad_reintentos} intentos")
            cantidad_reintentos = cantidad_reintentos - 1
    raise IngresoIncorrecto("Te quedaste sin mas intentos")

def ingreso_entero_restringido(mensaje,minimo = 0, maximo = 10):
    mensaje2 = f"Ingresar un numero entre {minimo} y {maximo}"
    num = ingreso_entero(mensaje2)
    if (num >= minimo and num <= maximo):
        return num
        print(f"El numero ingresado {num} es correcto")
    else:
        raise IngresoIncorrecto("El nomero ingresado no pertenece al rango entre 0 y 10")
    
def prueba():
    print(ingreso_entero_reintento("Ingrese un Numero Entero"))
    print(ingreso_entero_restringido("Ingrese un numero entero entre 0 y 10"))

if __name__ == "__main__":
    prueba()
    
