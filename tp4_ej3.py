################
# Gastón Emanuel Prat - @GastonPrat
# Ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    pass

def ingreso_grados(mensaje):
    ingreso = input(mensaje + " #")
    try:
        entero = float(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un NÚMERO!") from err
    return entero

def convertir_a_fahrrenheit(mensaje):
    try:
        in_celcius = ingreso_grados(mensaje)
        fahrrenheit = ((in_celcius * 1.8) + 32)
        msj = f"La Temperatura de {in_celcius}°C equivale a {fahrrenheit}°F"
    except ValueError as err:
        raise IngresoIncorrecto
    return msj
    
def convertir_a_centigrados(mensaje):
    try:
        in_fahrren = ingreso_grados(mensaje)
        centigrados = ((in_fahrren - 32) / 1.8)
        msj = f"La Temperatura de {in_fahrren}°C equivale a {centigrados}°F"
    except ValueError as err:
        raise IngresoIncorrecto
    return msj

def prueba():
    print(convertir_a_fahrrenheit("Ingrese una temperatura en °C"))
    
    print(convertir_a_centigrados("Ingrese una temperatura en °F"))
    

if __name__ == "__main__":
    prueba()
    
