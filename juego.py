import random

# Función para obtener la elección del jugador
def obtener_eleccion():
    opciones = ["piedra", "papel", "tijeras"]
    eleccion = ""
    while eleccion not in opciones:
        eleccion = input("Elige piedra, papel o tijeras: ").lower()
    return eleccion

# Función para determinar el ganador comparando ambas elecciones
def determinar_ganador(eleccion1, eleccion2):
    if eleccion1 == eleccion2:
        return "Empate"
    elif (eleccion1 == "piedra" and eleccion2 == "tijeras") or \
         (eleccion1 == "papel" and eleccion2 == "piedra") or \
         (eleccion1 == "tijeras" and eleccion2 == "papel"):
        return "Jugador 1 gana"
    else:
        return "Computadora gana"

# Modo de juego contra la computadora
def jugar_vs_computadora(historial):
    print("\n--- Jugar contra la Computadora ---")
    jugador = obtener_eleccion()
    computadora = random.choice(["piedra", "papel", "tijeras"])
    print(f"La computadora eligió: {computadora}")
    resultado = determinar_ganador(jugador, computadora)
    print(f"Resultado: {resultado}\n")
    historial.append(resultado)
    if len(historial) > 5:
        historial.pop(0)

# Modo de juego multijugador
def jugar_multijugador(historial):
    print("\n--- Modo Multijugador ---")
    print("Jugador 1")
    jugador1 = obtener_eleccion()
    print("\nJugador 2")
    jugador2 = obtener_eleccion()
    resultado = determinar_ganador(jugador1, jugador2)
    print(f"Resultado: {resultado}\n")
    historial.append(resultado)
    if len(historial) > 5:
        historial.pop(0)

# Mostrar las estadísticas de las últimas 5 partidas
def mostrar_estadisticas(historial):
    print("\n--- Últimas 5 partidas ---")
    if not historial:
        print("Aún no hay partidas registradas.")
    else:
        for i, resultado in enumerate(historial[::-1], 1):
            print(f"Partida {i}: {resultado}")
    print()

# Menú principal del juego
def menu():
    historial = []
    while True:
        print("\n=== Menú Principal ===")
        print("1. Jugar vs Computadora")
        print("2. Modo Multijugador")
        print("3. Ver Estadísticas")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar_vs_computadora(historial)
        elif opcion == "2":
            jugar_multijugador(historial)
        elif opcion == "3":
            mostrar_estadisticas(historial)
        elif opcion == "4":
            print("Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

# Ejecutar el menú si el script es ejecutado directamente
if __name__ == "__main__":
    menu()
