# ejercicio de aritmetica, pasar el ejercicio de infijo a postfijo 
# Grupo Andres Porras, Allysson Palma y Nicole Ramos 
class Nodo:
    def __init__(self, dato):
        self.dato = dato              
        self.siguiente = None         

class Pila:
    def __init__(self):
        self.tope = None           

    def esta_vacia(self):
        return self.tope is None      # Verifica si la pila está vacía

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)            
        nuevo_nodo.siguiente = self.tope    # El nuevo nodo apunta al tope actual
        self.tope = nuevo_nodo              # El nuevo nodo ahora es el tope de la pila

    def desapilar(self):
        if self.esta_vacia():           
            return None
        valor = self.tope.dato              # Guarda el valor del nodo en el tope
        self.tope = self.tope.siguiente     # El tope ahora apunta al siguiente nodo
        return valor                        # Devuelve el valor que estaba en el tope

    def ver_tope(self):
        return None if self.esta_vacia() else self.tope.dato  # Devuelve el valor del tope sin quitarlo

# Función para obtener la prioridad de un operador
def prioridad(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0  # Por defecto, prioridad 0 (para paréntesis u otros caracteres)

# Convierte una expresión en notación infija a postfija
def convertir_infija_a_postfija(expresion):
    pila = Pila()        # Pila para almacenar operadores
    salida = ""          # Cadena de salida (expresión postfija)

    for simb in expresion:
        if simb.isalnum():  # Si es un operando (letra o número), se agrega a la salida
            salida += simb
        elif simb == '(':   # Si es paréntesis de apertura, se apila
            pila.apilar(simb)
        elif simb == ')':   # Si es paréntesis de cierre, desapilar hasta '('
            while not pila.esta_vacia() and pila.ver_tope() != '(':
                salida += pila.desapilar()
            pila.desapilar()  # Quita el paréntesis de apertura '('
        else:
            # Si es operador, desapilar operadores de mayor o igual prioridad
            while (not pila.esta_vacia() and
                   prioridad(simb) <= prioridad(pila.ver_tope())):
                salida += pila.desapilar()
            pila.apilar(simb)  # Apilar el operador actual

    # Al finalizar, desapilar todo lo que quede en la pila
    while not pila.esta_vacia():
        salida += pila.desapilar()

    return salida  # Devuelve la expresión en notación postfija

# Evalúa una expresión en notación postfija con valores numéricos
def evaluar_postfija(postfija, valores):
    pila = Pila()  # Pila para cálculos

    for simb in postfija:
        if simb.isalnum():
            pila.apilar(valores[simb])  # Se apilan los valores de los operandos
        else:
            op2 = pila.desapilar()      # Se desapilan dos operandos
            op1 = pila.desapilar()
            # Se realiza la operación correspondiente y se apila el resultado
            if simb == '+':
                pila.apilar(op1 + op2)
            elif simb == '-':
                pila.apilar(op1 - op2)
            elif simb == '*':
                pila.apilar(op1 * op2)
            elif simb == '/':
                pila.apilar(op1 / op2)
            elif simb == '^':
                pila.apilar(op1 ** op2)

    return pila.desapilar()  # Resultado final de la expresión postfija