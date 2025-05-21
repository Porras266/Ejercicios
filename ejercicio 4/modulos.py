""" Ejercicio #4: Implementación de una cola de prioridad. Diseñe una cola de prioridad
    donde los elementos se desencolan según su prioridad. Cada elemento tendrá un nombre y 
    una prioridad (un número entero, donde un número menor indica
    mayor prioridad).

Mi ejemplo: En una pasteleria hay prioridad para realizar los pedidos, ejemplo
los pasteles se hacen primero que los capcake (ya que dilatan mas en su realizacion), 
dependiendo de la necesidad o tiempo de pedido de la pasteleria (1 es la prioridad mas alta y 5 la mas baja ) 

Grupo: Andres Porras, Nicole Ramos, Allysson Palma"""



# Clase Nodo
class Nodo:
    def __init__(self, producto, prioridad):
        self.producto = producto
        self.prioridad = prioridad  # Prioridad (1 es la más alta)
        self.siguiente = None

#la cola de prioridad con lista enlazada
class ColaPrioridad:
    def __init__(self):
        self.frente = None  # Nodo al inicio de la cola (mayor prioridad obvi)


    def insertar(self, producto, prioridad):
        nuevo = Nodo(producto, prioridad)
        
        # Insertar al inicio si la cola está vacía o la prioridad es mayor
        if self.frente is None or prioridad < self.frente.prioridad:
            nuevo.siguiente = self.frente  # Insertar al inicio de la cola
            self.frente = nuevo
        else:
            actual = self.frente
            # Buscar la posición correcta según la prioridad
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
                  # Insertar el nodo en su lugar
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo


    # para eliminarsh pero en el ejercicio decia desencolar por eso pongo desencolar(se que es lo mismo)
    def desencolar(self):
        if self.frente is None:
            print("La cola de pedidos está vacía")
            return None
        else:
            producto = self.frente.producto        # Tomar el producto del frente
            self.frente = self.frente.siguiente    # Mover el frente al siguiente producto
            return producto                        # Retornar el nombre del producto eliminado

    # para mostrar la colita 
    def mostrar(self):
        actual = self.frente  # Comenzamos desde el frente
        if actual is None:
            print("La cola de pedidos está vacía")
        else:
            print("Productos en cola por prioridad (1 mas alta):")
            while actual:
                 # Mostrar nombre y prioridad del producto actual
                print(f"- {actual.producto} (Prioridad: {actual.prioridad})")
                actual = actual.siguiente

