"""
Módulo para manejar una lista de reproducción estilo Spotify usando lista enlazada.
"""

# Clase para cada canción (nodo)
class NodoCancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None

# Clase para la lista de reproducción
class ListaReproduccion:
    def __init__(self):
        self.primera = None
        self.actual = None

    # Agregar canción al final
    def agregar_cancion(self, nombre):
        nueva = NodoCancion(nombre)
        if self.primera is None:
            self.primera = nueva
            self.actual = nueva
        else:
            temp = self.primera
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp

    # Eliminar canción por nombre
    def eliminar_cancion(self, nombre):
        temp = self.primera
        while temp:
            if temp.nombre == nombre:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primera = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                if temp == self.actual:
                    self.actual = temp.siguiente or temp.anterior or self.primera
                print(f"'{nombre}' fue eliminada.")
                return
            temp = temp.siguiente
        print(f"La canción '{nombre}' no fue encontrada.")

    # Mostrar canción actual
    def reproducir_actual(self):
        if self.actual:
            print(f"Reproduciendo ahora: {self.actual.nombre}")
        else:
            print("No hay canción seleccionada.")

    # Reproducir siguiente
    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            self.reproducir_actual()
        else:
            print("No hay siguiente canción.")

    # Reproducir anterior
    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            self.reproducir_actual()
        else:
            print("No hay canción anterior.")

    # Repetir actual
    def repetir_actual(self):
        if self.actual:
            print(f" Repitiendo: {self.actual.nombre}")
        else:
            print("No hay canción para repetir.")

    # Reproducir una canción específica
    def reproducir_cancion(self, nombre):
        temp = self.primera
        while temp:
            if temp.nombre == nombre:
                self.actual = temp
                self.reproducir_actual()
                return
            temp = temp.siguiente
        print(f"La canción '{nombre}' no fue encontrada.")

    # Mostrar toda la lista
    def mostrar_lista(self):
        temp = self.primera
        if not temp:
            print(" La lista de reproducción está vacía.")
            return
        print(" Lista de reproducción:")
        while temp:
            indicador = " (💽Reproduciendo ahora)" if temp == self.actual else ""
            print(f"- {temp.nombre} {indicador}")
            temp = temp.siguiente
