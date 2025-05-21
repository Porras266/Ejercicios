"""
 Ejercicio #3: Simulación de una lista de reproducción de música. Implemente
una lista de reproducción de música utilizando una lista enlazada. El programa debe
permitir agregar canciones, eliminar canciones, reproducir la siguiente canción,
reproducir la canción anterior y mostrar la lista de reproducción actual
"""
import Modulo3 as playlist

def main():
    lista = playlist.ListaReproduccion()

    while True:
        print("\n--- Spotify  ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente ")
        print("4. Reproducir anterior ")
        print("5. Repetir canción ")
        print("6. Reproducir canción específica ")
        print("7. Ver canción actual ")
        print("8. Mostrar lista completa ")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la canción: ")
            lista.agregar_cancion(nombre)
        elif opcion == "2":
            nombre = input("Nombre de la canción a eliminar: ")
            lista.eliminar_cancion(nombre)
        elif opcion == "3":
            lista.siguiente_cancion()
        elif opcion == "4":
            lista.anterior_cancion()
        elif opcion == "5":
            lista.repetir_actual()
        elif opcion == "6":
            nombre = input("Nombre de la canción a reproducir: ")
            lista.reproducir_cancion(nombre)
        elif opcion == "7":
            lista.reproducir_actual()
        elif opcion == "8":
            lista.mostrar_lista()
        elif opcion == "9":
            print("Cerrando Spotify ")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
