import random

def obtener_eleccion(jugador):
    opciones = ["piedra", "papel", "tijeras"]
    eleccion = ""
    while eleccion not in opciones:
        eleccion = input(f"{jugador}, elige piedra, papel o tijeras: ").lower()
    return eleccion

def determinar_ganador(eleccion1, eleccion2, jugador1, jugador2):
    if eleccion1 == eleccion2:
        return "Empate"
    elif (eleccion1 == "piedra" and eleccion2 == "tijeras") or \
         (eleccion1 == "papel" and eleccion2 == "piedra") or \
         (eleccion1 == "tijeras" and eleccion2 == "papel"):
        return f"{jugador1} gana"
    else:
        return f"{jugador2} gana"

def jugar_vs_computadora(historial):
    jugador = input("Ingresa tu nombre: ")
    eleccion_jugador = obtener_eleccion(jugador)
    eleccion_computadora = random.choice(["piedra", "papel", "tijeras"])
    print(f"La computadora eligió: {eleccion_computadora}")
    resultado = determinar_ganador(eleccion_jugador, eleccion_computadora, jugador, "Computadora")
    print(f"Resultado: {resultado}\n")
    historial.append(f"{jugador} vs Computadora: {resultado}")

def jugar_multijugador(historial):
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")
    eleccion1 = obtener_eleccion(jugador1)
    eleccion2 = obtener_eleccion(jugador2)
    resultado = determinar_ganador(eleccion1, eleccion2, jugador1, jugador2)
    print(f"Resultado: {resultado}\n")
    historial.append(f"{jugador1} vs {jugador2}: {resultado}")

def mostrar_estadisticas(historial):
    print("\n--- Últimas 5 partidas ---")
    if not historial:
        print("Aún no hay partidas registradas.")
    else:
        for i, resultado in enumerate(historial[-5:], 1):
            print(f"Partida {i}: {resultado}")
    print()

def mostrar_reglas():
    print("\n=== Reglas del Juego ===")
    print("1. Piedra vence a Tijeras")
    print("2. Tijeras vence a Papel")
    print("3. Papel vence a Piedra")
    print("4. Si ambos jugadores eligen lo mismo, es un empate.")
    print()

def menu():
    historial = []
    while True:
        print("\n=== Menú Principal ===")
        print("1. Jugar vs Computadora")
        print("2. Modo Multijugador")
        print("3. Ver Estadísticas")
        print("4. Ver Reglas")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar_vs_computadora(historial)
        elif opcion == "2":
            jugar_multijugador(historial)
        elif opcion == "3":
            mostrar_estadisticas(historial)
        elif opcion == "4":
            mostrar_reglas()
        elif opcion == "5":
            print("Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    menu()

