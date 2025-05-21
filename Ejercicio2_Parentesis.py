"""Ejercicio #2: Verificación de paréntesis balanceados. Escriba un programa que
determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados.
Use una pila para realizar el seguimiento de los paréntesis abiertos """

#Se entienden como balanceados cuando tenemos un parentesis que abre y cierra

from Ejercicio2_Modulo import Pila

#Como buena practica utilizamos la funcion para verificar si esta balanceado
def verificar_balanceo(cadena):
    #Creamos nuestra instancia de la clase pila
    pila = Pila()
    # Definimos un diccionario para relacionar cada paréntesis de cierre con su apertura correspondiente
    pares = {')': '(', '}': '{', ']': '['}

    # Recorremos cada carácter en la cadena de texto
    for caracter in cadena:
        # Si encontramos un paréntesis de apertura, lo agregamos a la pila
        if caracter in "({[":
            pila.apilar(caracter)
        # Si encontramos un paréntesis de cierre
        elif caracter in ")}]":
            # Verificamos si la pila está vacía o si el último paréntesis abierto no coincide
            if pila.esta_vacia() or pila.desapilar() != pares[caracter]:
                # Si alguna de esas condiciones se cumple, los paréntesis no están balanceados
                return False
    # Al finalizar, si la pila está vacía, los paréntesis están balanceados
    return pila.esta_vacia()


# Ejemplo de uso:
if __name__ == "__main__":
    cadena = input("Ingrese una cadena: ")
    
    #llamada a la funcion para verificar si esta balanceado 
    if verificar_balanceo(cadena):
        print("Los paréntesis están balanceados.")
    else:
        print("Los paréntesis NO están balanceados.")
