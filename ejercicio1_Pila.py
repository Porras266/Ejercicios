class Pila:
    def __init__(self):
        #Constructor: Inicializa una lista vacia para almacenar los elementos
        self.elementos = []
    
    def estas_vacia(self):
        #Verificamos si la pila esta vacia 
        return len(self.elementos) == 0
    
    def apilar(self,valor):
        #Agrega un elemento a la parte superior de la pila
        self.elementos.append(valor)
    
    def desapilar(self):
        #Remueve y devuelve el elemento de la parte superior de la pila
        
        #verifica que la pila NO este vacia antes de intentar acceder al tope 
        if not self.estas_vacia():
            return self.elementos.pop()
        else:
            #Lanzamos IndexError cuando intentas acceder a un indice que no existe  
            raise IndexError("La pila esta vacia")
        
    def longitud_pila(self):
        #Devuelve el numero de elementos en la pila
        return len(self.elementos)
    
    def ver_tope(self):
        #Devuelve el elemento en la parte superior de la pila sin removerlo
        
        if not self.estas_vacia():
            #En Python, los indices negativos acceden a los elementos desde el final 
                                #-1 "Ultimo elemento"
            return self.elementos[-1]
        else:
        #Lanzamos IndexError cuando intentas acceder a un indice que no existe   
            raise IndexError("La pila esta vacia")        