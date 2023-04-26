import random
import math

class Nodo:
    def __init__(self, valor):
        self.valor = valor
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
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    primer_nodo = None
    nodo_anterior = None

    for _ in range(numeros):
        num = random.uniform(0, 100)
        
        if modo == 1:
            redondeado = math.ceil(num)
        elif modo == 2:
            redondeado = math.floor(num)
        else:
            redondeado = round(num)

        print(f"Número original: {num}, Número redondeado: {redondeado}")
        
        nuevo_nodo = Nodo(redondeado)
        if primer_nodo is None:
            primer_nodo = nuevo_nodo
        else:
            nodo_anterior.siguiente = nuevo_nodo
        nodo_anterior = nuevo_nodo

    return primer_nodo

def imprimir_lista_numeros(nodo):
    while nodo is not None:
        print(nodo.valor, end=" -> ")
        nodo = nodo.siguiente
    print("Fin")

if __name__ == "__main__":
    lista_numeros = generador()
    print("Lista de números redondeados:")
    imprimir_lista_numeros(lista_numeros)
