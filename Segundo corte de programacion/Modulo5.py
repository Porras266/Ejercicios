"""
Módulo para manejar lista enlazada con búsqueda, agregar, eliminar, guardar y cargar.
"""
#Defenimos nuestra clase nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
#defenimos nusetra clase de listra enlazada 
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
# Definimos el nodo cabeza y un construcotr para agregrs los vaalores 
    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo
# construcotr para eliminar los valores
    def eliminar(self, valor):
        temp = self.cabeza
        anterior = None
        while temp:
            if temp.valor == valor:
                if anterior:
                    anterior.siguiente = temp.siguiente
                else:
                    self.cabeza = temp.siguiente
                return True  # Eliminado con éxito
            anterior = temp
            temp = temp.siguiente
        return False  # No encontrado
#construcotr para buscar los valores
    def buscar(self, valor_buscado):
        temp = self.cabeza
        posicion = 1
        while temp:
            if temp.valor == valor_buscado:
                return posicion
            temp = temp.siguiente
            posicion += 1
        return -1

# Definimos el construcotr para mostrar los valores
    def mostrar(self):
        temp = self.cabeza
        if not temp:
            print("La lista está vacía.")
            return
        print("Lista enlazada:")
        pos = 1
        while temp:
            print(f"{pos}. {temp.valor}")
            temp = temp.siguiente
            pos += 1
