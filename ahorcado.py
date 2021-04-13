import random
import string
from ahorcado_palabras import palabras

#Funcion para seleccionar una palabra al azar de ahorcado_palabras
def palabra_valida(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

#FUNCION PRINCIPAL DE AHORCADO
def ahorcado(palabra):
    #Declaracion de variables
    palabra_letras = set(palabra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()
    vidas = 6

    #Bucle de juego. No termina hasta quedar sin mas vidas
    while vidas > 0 and len(palabra_letras) > 0:
        print("Tienes", vidas, "vidas")
        print("Has usado estas letras:", " ".join(letras_usadas))

        palabra_lista = [letra if letra in letras_usadas else "-" for letra in palabra]
        print("Palabra actual:", " ".join(palabra_lista))

        letra_usuario = input("Adivina un letra: ").upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in palabra_letras:
                palabra_letras.remove(letra_usuario)
            else:
                vidas = vidas - 1
                print("La letra", letra_usuario, "no está en la palabra")
        elif letra_usuario in letras_usadas:
            print("Ya has probado con la letra", letra_usuario, ".")
        else:
            print("Carácter inválido.")

        print("------------------------------")
    if vidas == 0:
        print("¡Perdiste! La palabra era", palabra)
    else:
        print("¡Correcto! La palabra es", palabra)

#Funcion del jugador que ingresa una palabra para adivinar
def ahorcado_jugador():
    print("El jugador 2 ingresa una palabra y jugador 1 debe adivinar")
    palabra=input().upper()

    ahorcado(palabra)

#Funcion del bot que elegira una palabra al azar
def ahorcado_bot():
    palabra = palabra_valida(palabras)

    ahorcado(palabra)


###ARRANQUE DEL PROGRAMA
print("¡Ahorcado!")
print("¿Desea jugar contra el bot o prefiere hacerlo contra otro jugador?")
print("1. Bot")
print("2. Otro jugador")

#Usuario elige si jugar contra bot u otro jugador
eleccion = input()
if eleccion == "1":
    ahorcado_bot()
elif eleccion == "2":
    ahorcado_jugador()