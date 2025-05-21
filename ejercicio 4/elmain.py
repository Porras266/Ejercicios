""" Ejercicio #4: Implementación de una cola de prioridad. Diseñe una cola de prioridad
    donde los elementos se desencolan según su prioridad. Cada elemento tendrá un nombre y 
    una prioridad (un número entero, donde un número menor indica
    mayor prioridad).

Mi ejemplo: En una pasteleria hay prioridad para realizar los pedidos, ejemplo
los pasteles se hacen primero que los capcake (ya que dilatan mas en su realizacion), 
dependiendo de la necesidad o tiempo de pedido de la pasteleria (1 es la prioridad mas alta y 5 la mas baja ) 

Grupo: Andres Porras, Nicole Ramos, Allysson Palma"""
#Importamos la biblioteca Os 
import os

from modulos import ColaPrioridad

cola = ColaPrioridad()

# Bucle para mostrar el menú hasta que el usuario decida salir
while True:
    print(" Bienvenido al sistema de pedidos de la Pastelería Niki")
    print("1. Ingresar nuevo pedido")
    print("2. Eliminar pedido con mayor prioridad")
    print("3. Mostrar productos en cola")
    print("4. Salir")
    
    opcion = input("\nElija una opción porfavor  (1-4): ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        try:
            prioridad = int(input("Ingrese la prioridad (1 = más alta, 5 = más baja): "))
             # Validar que la prioridad esté en el rango permitido
            if prioridad < 1 or prioridad > 5:
                print("La prioridad debe estar entre 1 y 5 :)")
                input("presione una tecla para continuar")
                os.system('cls')

            else:
                cola.insertar(producto, prioridad)
                print(f" Producto '{producto}' agregado con prioridad {prioridad}.")
        except ValueError:
            # Si el usuario no escribe un número válido
            print("Prioridad inválida. Debe ser un número entero entre 1 y 5.")
        input("presione una tecla para continuar")
        os.system('cls')

    # Opcion para elimianr 
    elif opcion == "2":
        producto = cola.desencolar()
        if producto:
            print(f"Producto '{producto}' eliminado de la cola")
        input("presione una tecla para continuar")    
        os.system('cls')

    # Opcion para mostrar
    elif opcion == "3":
        cola.mostrar()
        input("presione una tecla para continuar")
        os.system('cls')

    # Mostrar 
    elif opcion == "4":
        print("¡Gracias por usar el sistema de la Pastelería Niki! Hasta luego :)")
        break
    # Opción inválida (no está entre 1 y 4)
    else:
        print("Opción no válida. Intente nuevamente.")
