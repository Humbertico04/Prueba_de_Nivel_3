import random
import math

class Nodo:
    def __init__(self, valor_original, valor_redondeado):
        self.valor_original = valor_original
        self.valor_redondeado = valor_redondeado
        self.siguiente = None

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if ini <= numero <= fin:
                return numero
            else:
                print(f"Por favor, ingrese un número entre {ini} y {fin}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    redondeo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    primer_nodo = None
    nodo_anterior = None

    for _ in range(numeros):
        num = random.uniform(0, 100)
        
        if redondeo == 1:
            redondeado = math.ceil(num)
        elif redondeo == 2:
            redondeado = math.floor(num)
        else:
            redondeado = round(num)

        nuevo_nodo = Nodo(num, redondeado)
        if primer_nodo is None:
            primer_nodo = nuevo_nodo
        else:
            nodo_anterior.siguiente = nuevo_nodo
        nodo_anterior = nuevo_nodo

    return primer_nodo

def imprimir_lista_numeros(nodo):
    while nodo is not None:
        print(f"Número original: {nodo.valor_original}, Número redondeado: {nodo.valor_redondeado}")
        nodo = nodo.siguiente
        
def imprimir_lista_numeros_redondeados(nodo):
    while nodo is not None:
        print(nodo.valor_redondeado, end=" -> ")
        nodo = nodo.siguiente
    print("Fin")

def main():
    lista_numeros = generador()
    print("\nNúmeros originales y redondeados:")
    imprimir_lista_numeros(lista_numeros)
    print("\nLista de números redondeados:")
    imprimir_lista_numeros_redondeados(lista_numeros)

if __name__ == "__main__":
    main()
