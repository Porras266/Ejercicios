#Creacion de la clase Pila
class Pila:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los elementos de la pila
        self.items = []
    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        return len(self.items) == 0
    
    # Método para agregar un elemento a la cima de la pila
    def apilar(self, item):
        self.items.append(item)
        
    # Método para eliminar y devolver el elemento en la cima de la pila
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop() # pop() elimina y devuelve el último elemento de la lista
        return None # Si la pila está vacía, retorna None
    
    # Método para ver el elemento en la cima de la pila sin eliminarlo
    def cima(self):
        if not self.esta_vacia():
            # '-1' Accede al último elemento de la lista
            return self.items[-1]
        return None # Si la pila está vacía, retorna None
