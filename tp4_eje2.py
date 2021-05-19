from tp4_ej1 import ingreso_entero, IngresoIncorrecto
################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def suma_lenta(numero, otro_numero):
        numero = ingreso_entero(numero)
        otro_numero = ingreso_entero(otro_numero)
        resultado = numero + otro_numero
        if numero < otro_numero:
            contador = numero
            while contador < resultado:
                print(f"{contador}")
                contador = contador +1
        else:
            contador = otro_numero
            while contador < resultado:
                print(f"{contador}")
                contador = contador +1
        return resultado



def prueba():
    print(suma_lenta("ingrese un numero entero", "ingrese otro numero a sumar"))

if __name__ == "__main__":
    prueba()
    
