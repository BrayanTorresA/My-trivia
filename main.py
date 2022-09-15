import time  # Importamos la librería time
import random  # Importamos la librería random

lista_puntajes = []
lista_preguntas = [
    '1) ¿Qué significa "Valar Morghulis"?',
    "2) Cómo se llama el lobo huargo de Jon Snow",
    "3) ¿Quién orquesto la boda roja?",
    "4) ¿Cúal es la raza de lobos de los Stark?",
    "5) ¿Cómo se llaman los dragones de Daenerys?",
    "6) ¿Qué palabra utiliza Daenerys para que los dragones arrojen fuego?",
    "7) ¿En qué capitulo muere el rey Joffrey?",
    '8) ¿Quién dijo la iconica frase:"Cuando juegas al juego de tronos, o ganas o mueres"?',
    "9) ¿Cómo se llama a entrar en la mente de los animales?",
    "10) ¿Que personajes aparecen en todos los capítulos de la primera temporada?"
]
lista_alternativas = [
    [
        "a) Todos los hombres deben vivir", "b) Todos los hombres deben morir",
        "c) Todos los hombres deben servir",
        "d) Todos los hombres deben cumplir"
    ], ["a) Ghost", "b) Summer", "c) Grey worm", "d) Grey wind"],
    [
        "a) Daario Naharis", "b) Cersei Lannister", "c) Walder Frey",
        "d) Tyrion Lannister"
    ], ["a) Hurjo", "b) Hurgo", "c) Huargo", "d) Hungaro"],
    [
        "a) Rhaegal, Viserion y Drogon", "b) Rhaegal, Viserion y Drogo",
        "c) Rhaegal, Velirion y Drago", "d) Rhaegal, Visol y Drogon"
    ], ["a) Domeris", "b) Dracorys", "c) Dracarys", "d) Domecris"],
    [
        "a) Pink wedding", "b) Red wedding", "c) Yellow wedding",
        "d) Purple wedding"
    ],
    [
        "a) Cersei Lannister",
        "b) Margaery Tyrell",
        "c) Arya Stark",
        "d) Melisandre",
    ], ["a) Warm", "b) Warg", "c) Warp", "d) Ward"],
    [
        "a) Tyrion y Cersei", "b) Tyrion y Joffrey", "c) Cersei y Joffrey",
        "d) Sansa y Tyrion"
    ]
]

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[39m"

puntaje = 0

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("Bienvenido a mi trivia sobre Game of Thrones")
print("Pondremos a prueba tus conocimientos sobre la serie")
nombre = input("Ingresa tu nombre: ")
print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)
print(nombre + " tienes ", puntaje, "puntos")

while iniciar_trivia == True:  #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje1 = 0

    print("\nIntento número:", intentos)
    time.sleep(1)
    print("Comenzamos...")
    for numero_carga in range(5, 0, -1):
        print(numero_carga)
        time.sleep(1.5)
    time.sleep(1)  # para ayudarnos a imaginar que vamos jugando
    print("Cargando pregunta...")
    time.sleep(2)
    # Pregunta 1
    print(lista_preguntas[0])
    for alternativa in lista_alternativas[0]:
        print(alternativa)
    respuesta_1 = input("\nTu respuesta: ")

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_1 == "b":
        puntaje1 += 10
        lista_puntajes.append(puntaje1)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje1 -= 10
        lista_puntajes.append(puntaje1)
        print(RED + "Incorrecto", nombre, "!" + RESET)

    print(nombre, "ganaste", puntaje1, "puntos")

    puntaje2 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    time.sleep(2)
    # Pregunta 2
    print(lista_preguntas[1])
    for alternativa in lista_alternativas[1]:
        print(alternativa)
    respuesta_2 = input("\nTu respuesta: ")

    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_2 == "a":
        puntaje2 += 10
        lista_puntajes.append(puntaje2)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje2 -= 20
        lista_puntajes.append(puntaje2)
        print(RED + "Incorrecto", nombre, "!" + RESET)

    print(nombre, "ganaste", puntaje2, "puntos")

    puntaje3 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    print(
        RED +
        "Advertencia esta pregunta te quita una cantidad aleatoria de puntos si fallas"
        + RESET)
    time.sleep(2)
    # Pregunta 3
    print(lista_preguntas[2])
    for alternativa in lista_alternativas[2]:
        print(alternativa)

    respuesta_3 = input("\nTu respuesta: ")

    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_3 == "c":
        puntaje3 += 10
        lista_puntajes.append(puntaje3)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje3 -= random.randint(10, 50)
        lista_puntajes.append(puntaje3)
        print(RED + "Incorrecto", nombre, "!" + RESET)

    print(nombre, "ganaste", puntaje3, "puntos")

    puntaje4 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    print("Vas muy bien,sigue adelante")
    time.sleep(2)
    # Pregunta 4
    print(lista_preguntas[3])
    for alternativa in lista_alternativas[3]:
        print(alternativa)

    respuesta_4 = input("\nTu respuesta: ")

    while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_4 == "c":
        puntaje4 += 10
        lista_puntajes.append(puntaje4)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje4 -= 10
        lista_puntajes.append(puntaje4)
        print(RED + "Incorrecto", nombre, "!" + RESET)
    print(nombre, "ganaste", puntaje4, "puntos")

    puntaje5 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    print(
        GREEN +
        "Ya vamos por la mitad, esta pregunta te otorga una cantidad de puntaje aleatoria si aciertas"
        + RESET)
    time.sleep(2)
    # Pregunta 5
    print(lista_preguntas[4])
    for alternativa in lista_alternativas[4]:
        print(alternativa)

    respuesta_5 = input("\nTu respuesta: ")

    while respuesta_5 not in ("a", "b", "c", "d"):
        respuesta_5 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_5 == "a":
        puntaje5 += random.randint(10, 50)
        lista_puntajes.append(puntaje5)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje5 -= 10
        lista_puntajes.append(puntaje5)
        print(RED + "Incorrecto", nombre, "!" + RESET)
    print(nombre, "ganaste", puntaje5, "puntos")

    puntaje6 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    print(RED +
          "Desde ahora las respuestas incorrectas te restaran 20 puntos" +
          RESET)
    time.sleep(2)
    # Pregunta 6
    print(lista_preguntas[5])
    for alternativa in lista_alternativas[5]:
        print(alternativa)
    respuesta_6 = input("\nTu respuesta: ")

    while respuesta_6 not in ("a", "b", "c", "d"):
        respuesta_6 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_6 == "c":
        puntaje6 += 10
        lista_puntajes.append(puntaje6)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje6 -= 20
        lista_puntajes.append(puntaje6)
        print(RED + "Incorrecto", nombre, "!" + RESET)
    print(nombre, "ganaste", puntaje6, "puntos")

    puntaje7 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    time.sleep(2)
    # Pregunta 7
    print(lista_preguntas[6])
    for alternativa in lista_alternativas[6]:
        print(alternativa)

    respuesta_7 = input("\nTu respuesta: ")

    while respuesta_7 not in ("a", "b", "c", "d"):
        respuesta_7 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_7 == "d":
        puntaje7 += 10
        lista_puntajes.append(puntaje7)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje7 -= 20
        lista_puntajes.append(puntaje7)
        print(RED + "Incorrecto", nombre, "!" + RESET)
    print(nombre, "ganaste", puntaje7, "puntos")

    puntaje8 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    time.sleep(2)
    # Pregunta 8
    print(lista_preguntas[7])
    for alternativa in lista_alternativas[7]:
        print(alternativa)

    respuesta_8 = input("\nTu respuesta: ")

    while respuesta_8 not in ("a", "b", "c", "d"):
        respuesta_8 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_8 == "a":
        puntaje8 += 10
        lista_puntajes.append(puntaje8)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje8 -= 20
        lista_puntajes.append(puntaje8)
        print(RED + "Incorrecto", nombre, "!" + RESET)
    print(nombre, "ganaste", puntaje8, "puntos")

    puntaje9 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    time.sleep(2)
    # Pregunta 9
    print(lista_preguntas[8])
    for alternativa in lista_alternativas[8]:
        print(alternativa)
    respuesta_9 = input("\nTu respuesta: ")

    while respuesta_9 not in ("a", "b", "c", "d"):
        respuesta_9 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_9 == "b":
        puntaje9 += 10
        lista_puntajes.append(puntaje9)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje9 -= 20
        lista_puntajes.append(puntaje9)
        print(RED + "Incorrecto", nombre, "!" + RESET)
    print(nombre, "ganaste", puntaje9, "puntos")

    puntaje10 = 0
    time.sleep(1)
    print("Cargando pregunta...")
    print(GREEN + "Felicidades has llegado a la pregunta final, suerte" +
          RESET)
    time.sleep(2)
    print(GREEN +
          "si contestas bien obtendras un puntaje aleatorio entre 50 y 100" +
          RESET)
    time.sleep(2)
    print(RED + "De lo contrario se te restará ese mismo puntaje" + RESET)
    time.sleep(2)
    # Pregunta 10
    print(lista_preguntas[9])
    for alternativa in lista_alternativas[9]:
        print(alternativa)
    respuesta_10 = input("\nTu respuesta: ")

    while respuesta_10 not in ("a", "b", "c", "d"):
        respuesta_10 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_10 == "c":
        puntaje10 += random.randint(50, 100)
        lista_puntajes.append(puntaje10)
        print(GREEN + "Muy bien", nombre, "!" + RESET)
    else:
        puntaje10 -= random.randint(50, 100)
        lista_puntajes.append(puntaje10)
        print(RED + "Incorrecto", nombre, "!" + RESET)
    print(nombre, "ganaste", puntaje10, "puntos")

    print(GREEN + "Excelente, has obtenido", sum(lista_puntajes),
          "puntos" + RESET)

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    if repetir_trivia != "si":  # != significa "distinto"
        print("\nEspero " + nombre +
              " que lo hayas pasado bien, hasta pronto!")
        iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
