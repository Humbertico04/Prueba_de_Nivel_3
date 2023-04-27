class nodoCola(object):
    """Clase nodo cola"""
    
    info, sig = None, None

class Cola(object):
    """Clase cola"""

    def __init__(self):
        """Crea una cola vacia"""
        self.frente, self.final = None, None
        self.tamanio = 0

    def arribo(cola, dato):
        """Arriba el dato al final de la cola"""
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamanio += 1

    def atencion(cola):
        """Atiende el elemento en el frente de la cola y lo devuelve"""
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
        cola.tamanio -= 1
        return dato
    
    def cola_vacia(cola):
        """Devuelve true si la cola esta vacia"""
        return cola.frente is None
    
    def en_frente(cola):
        """Devuelve el valor almacenado en el frente de la cola"""
        return cola.frente.info
    
    def tamanio(cola):
        """Devuelve el numero de elementos en la cola"""
        return cola.tamanio
    
    def mover_al_final(cola):
        """Mueve el elemento del frente de la cola al final"""
        dato = Cola.atencion(cola)
        Cola.arribo(cola, dato)
        return dato

    def barrido(cola):
        """Muestra el contenido de una cola sin perder datos"""
        i = 0
        while (i < cola.tamanio):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1

class nodoArbol(object):
    """Clase nodo árbol"""

    def __init__(self, info):
        """Crea un nodo con la información cargada"""
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0

    def eliminar_nodo(raiz, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra"""
        x = None
        if (raiz is not None):
            if(clave < raiz.info):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        raiz = nodoArbol.balancear(raiz)
        nodoArbol.actualizaraltura(raiz)
        return raiz, x
    
    def insertar_nodo(raiz, dato):
        """Inserta un dato al árbol"""
        if(raiz is None):
            raiz = nodoArbol(dato)
        elif(dato < raiz.info):
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        raiz = nodoArbol.balancear(raiz)
        nodoArbol.actualizaraltura(raiz)
        return raiz

    def arbolvacio(raiz):
        """Devuelve true si el árbol esta vacío"""
        return raiz is None

    def remplazar(raiz):
        """Determina el nodo que remplazará al que se elimina"""
        aux = None
        if (raiz.der is None):
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux
    
    def por_nivel(raiz):
        """Realiaza el barrido postorden del árbol"""
        pendientes = Cola()
        Cola.arribo(pendientes, raiz)
        while(not Cola.cola_vacia(pendientes)):
            nodo = Cola.atencion(pendientes)
            print(nodo.info)
            if(nodo.izq is not None):
                Cola.arribo(pendientes, nodo.izq)
            if(nodo.der is not None):
                Cola.arribo(pendientes, nodo.der)

    def buscar(raiz, clave):
        """Devuelve la dirección del elemento buscado"""
        pos = None
        if(raiz is not None):
            if(raiz.info == clave):
                pos = raiz
            elif clave < raiz.info:
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
    
    def inorden(raiz):
        """Realiza el barrido inorden del árbol"""
        if(raiz is not None):
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def preorden(raiz):
        """Realiza el barrido preorden del árbol"""
        if(raiz is not None):
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def postorden(raiz):
        """Realiza el barrido postorden del árbol"""
        if(raiz is not None):
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)

    def altura(raiz):
        """Devuelve la altura de un nodo"""
        if(raiz is None):
            return -1
        else:
            return raiz.altura
        
    def actualizaraltura(raiz):
        """Actualiza la altura de un nodo"""
        if(raiz is not None):
            alt_izq = nodoArbol.altura(raiz.izq)
            alt_der = nodoArbol.altura(raiz.der)
            raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1

    def rotar_simple(raiz, control):
        """Realiza una rotación simple de nodos a la derecha o a la izquierda"""
        if control:
            aux = raiz.izq
            raiz.izq = aux.der
            aux.der = raiz
        else:
            aux = raiz.der
            raiz.der = aux.izq
            aux.izq = raiz
        nodoArbol.actualizaraltura(raiz)
        nodoArbol.actualizaraltura(aux)
        raiz = aux
        return raiz
    
    def rotar_doble(raiz, control):
        """Realiza una rotación doble de nodos a la derecha o la izquierda"""
        if control:
            raiz.izq = nodoArbol.rotar_simple(raiz.izq, False)
            raiz = nodoArbol.rotar_simple(raiz, True)
        else:
            raiz.der = nodoArbol.rotar_simple(raiz.der, True)
            raiz = nodoArbol.rotar_simple(raiz, False)
        return raiz
    
    def balancear(raiz):
        """Determina que rotación hay que hacer para balancear el arbol"""
        if(raiz is not None):
            if(nodoArbol.altura(raiz.izq)-nodoArbol.altura(raiz.der) == 2):
                if(nodoArbol.altura(raiz.izq.izq) >= nodoArbol.altura(raiz.izq.der)):
                    raiz = nodoArbol.rotar_simple(raiz, True)
                else:
                    raiz = nodoArbol.rotar_doble(raiz, True)
            elif(nodoArbol.altura(raiz.der)-nodoArbol.altura(raiz.izq) == 2):
                if(nodoArbol.altura(raiz.der.der) >= nodoArbol.altura(raiz.der.izq)):
                    raiz = nodoArbol.rotar_simple(raiz, False)
                else:
                    raiz = nodoArbol.rotar_doble(raiz, False)
        return raiz

    def imprimir_arbol(raiz, nivel=0):
        """Imprime por pantalla el arbol"""
        if raiz is not None:
            nodoArbol.imprimir_arbol(raiz.der, nivel + 1)
            print('    ' * nivel + str(raiz.info))
            nodoArbol.imprimir_arbol(raiz.izq, nivel + 1)

    def contar_ocurrencias(raiz, valor):
        if raiz is None:
            return 0
        
        conteo_izquierdo = nodoArbol.contar_ocurrencias(raiz.izq, valor)
        conteo_derecho = nodoArbol.contar_ocurrencias(raiz.der, valor)
        
        if raiz.info == valor:
            return 1 + conteo_izquierdo + conteo_derecho
        else:
            return conteo_izquierdo + conteo_derecho

import random

def cargar_numeros_aleatorios(cantidad):
    arbol = nodoArbol(random.randint(1, 1000))
    for _ in range(cantidad-1):
        arbol = arbol.insertar_nodo(random.randint(1, 1000))
    return arbol

def contar_pares_impares(nodo):
    if nodo is None:
        return 0, 0
    
    pares, impares = contar_pares_impares(nodo.izq)
    pares_r, impares_r = contar_pares_impares(nodo.der)
    
    pares += pares_r
    impares += impares_r
    
    if nodo.info % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    return pares, impares

if __name__ == "__main__":
    # Insertar números en el árbol
    arbol = cargar_numeros_aleatorios(1000)

    # Barridos
    print("Barrido preorden:")
    arbol.preorden()
    print("\nBarrido inorden:")
    arbol.inorden()
    print("\nBarrido postorden:")
    arbol.postorden()
    print("\nBarrido por nivel:")
    arbol.por_nivel()

    # Buscar un número en el árbol
    busqueda = random.randint(1, 1000)
    print(f"\n¿Está el número {busqueda} en el árbol?:", "Sí" if arbol.buscar(busqueda) else "No")

    # Eliminar tres valores del árbol
    eliminar = [10, 20, 30]
    for num in eliminar:
        arbol.eliminar_nodo(num)

    # Alturas de subárboles izquierdo y derecho
    print(f"\nAltura del subárbol izquierdo: {arbol.izq.altura}")
    print(f"Altura del subárbol derecho: {arbol.der.altura}")

    # Cantidad de ocurrencias de un elemento en el árbol
    elemento = random.randint(1, 1000)
    print(f"\nCantidad de ocurrencias de {elemento}: {arbol.contar_ocurrencias(elemento)}")

    # Contar números pares e impares en el árbol
    pares, impares = contar_pares_impares(arbol)
    print(f"\nNúmeros pares en el árbol: {pares}")
    print(f"Números impares en el árbol: {impares}")
