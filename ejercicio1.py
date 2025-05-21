#De el archivo ejercicio1_Pila importamos la clase pila
from ejercicio1_Pila import Pila
import time

def invertir_frase(frase):
     #1. Dividir la frase en palabras individuales
                #Recordemos Split funciona para dividir por espacios en blanco
     palabras = frase.split()
     
     #2.Creamos la instancia de la pila
     pila = Pila()
     
     #3. Apilar cada palabra
     for palabra in palabras:
        """Recordemos que en el modulo tenemos la funcion para apilar
         solo mandamos a llamar a esta funcion para realizar el append
         a cada una de las palabras ya desaparadas"""
        pila.apilar(palabra)
        
     #4. Inicializamos una lista para almacenar la frase invertida
     frase_invertida = []
     
     #5. Desapilar palanras hasta que la pila este vacia   
     #Mientras la pila no este vacia
     while not pila.estas_vacia():
         #'palabra' utilizamos la funcion de desapilar
         palabra = pila.desapilar()
         #Agregamos palabra a la lista invertida
         frase_invertida.append(palabra)
         
     #6. Unir las palabras invertidas en una cadena
          #tenemos la frase invertida  ' ' es el string que usamos como separador
          #.join metodo de string que une los elementos de una lista
     return ' '.join(frase_invertida)
 
if __name__ == "__main__":
    
    frase_original = "Hola mundo desde UAM"
    resultado = invertir_frase(frase_original)
    
    print(f"Frase original: {frase_original}")
    time.sleep(2)
    print("Imprimiendo Frase invertida....")
    time.sleep(2)
    print(f"Frase invertida: {resultado}")