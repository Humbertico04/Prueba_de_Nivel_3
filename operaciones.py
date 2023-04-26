def suma(a, b):
    try:
        resultado = a + b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    return resultado

def resta(a, b):
    try:
        resultado = a - b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    return resultado

def producto(a, b):
    try:
        resultado = a * b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    return resultado

def division(a, b):
    try:
        resultado = a / b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        return None
    return resultado
