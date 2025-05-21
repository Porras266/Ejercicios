import Modulo5 as busqueda  # Importar el módulo con alias

def main():
    lista = busqueda.ListaEnlazada()

    while True:
        print("\n--- Menú Lista Enlazada ---")
        print("1. Mostrar lista")
        print("2. Agregar valor")
        print("3. Eliminar valor")
        print("4. Buscar valor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista.mostrar()
        elif opcion == "2":
            valor = input("Ingrese valor a agregar: ")
            lista.agregar(valor)
            print(f"'{valor}' agregado a la lista.")
        elif opcion == "3":
            valor = input("Ingrese valor a eliminar: ")
            eliminado = lista.eliminar(valor)
            if eliminado:
                print(f"'{valor}' eliminado de la lista.")
            else:
                print(f"'{valor}' no se encontró en la lista.")
        elif opcion == "4":
            valor = input("Ingrese valor a buscar: ")
            posicion = lista.buscar(valor)
            if posicion == -1:
                print(f"'{valor}' no está en la lista.")
            else:
                print(f"'{valor}' encontrado en la posición {posicion}.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
