################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def ingreso_float(mensaje):
    ingreso = input(mensaje + " #")
    try:
        real = float(ingreso)
    except ValueError as err:
        print("Eso no era un Número, intenta nuevamente")
        return prueba()
    return real

def convertir_a_fahrrenheit(in_celcius):
    try:
        fahrrenheit = ((in_celcius * 1.8) + 32)
        msj = f"La Temperatura de {in_celcius}°C equivale a {fahrrenheit}°F"
    except ValueError as err:
        raise IngresoIncorrecto
    return msj
    
def convertir_a_centigrados(in_fahrren):
    try:
        centigrados = ((in_fahrren - 32) / 1.8)
        msj = f"La Temperatura de {in_fahrren}°C equivale a {centigrados}°F"
    except ValueError as err:
        raise IngresoIncorrecto
    return msj

def prueba():
    print("Esto pasara de °C --->°F")
    in_celcius = ingreso_float("Ingrese temperatura en grados Celcius")
    msj = convertir_a_fahrrenheit(in_celcius)
    print(msj)
    
    print("Esto pasara de °F --->°C")
    in_fahrren = ingreso_float("Ingrese temperatura en grados fahrrenheit")
    msj = convertir_a_centigrados(in_fahrren)
    print(msj)
    

if __name__ == "__main__":
    prueba()
    
