import random
import string
import discord
from ahorcado_palabras import palabras

client=discord.Client()
#Funcion para seleccionar una palabra al azar de ahorcado_palabras

def palabra_valida(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

#FUNCION PRINCIPAL DE AHORCADO
def ahorcado(palabra,mensaje):
    #Declaracion de variables
    palabra_letras = set(palabra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()
    vidas = 6

    #Bucle de juego. No termina hasta quedar sin mas vidas
    while vidas > 0 and len(palabra_letras) > 0:
        await mensaje.channel.send("Tienes", vidas, "vidas")
        await mensaje.channel.send("Has usado estas letras:", " ".join(letras_usadas))

        palabra_lista = [letra if letra in letras_usadas else "-" for letra in palabra]
        await mensaje.channel.send("Palabra actual:", " ".join(palabra_lista))

        letra_usuario = input("Adivina un letra: ").upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in palabra_letras:
                palabra_letras.remove(letra_usuario)
            else:
                vidas = vidas - 1
                await mensaje.channel.send("La letra", letra_usuario, "no está en la palabra")
        elif letra_usuario in letras_usadas:
            await mensaje.channel.send("Ya has probado con la letra", letra_usuario, ".")
        else:
            await mensaje.channel.send("Carácter inválido.")

        await mensaje.channel.send("------------------------------")
    if vidas == 0:
        await mensaje.channel.send("¡Perdiste! La palabra era", palabra)
    else:
        await mensaje.channel.send("¡Correcto! La palabra es", palabra)

#Funcion del jugador que ingresa una palabra para adivinar
def ahorcado_jugador(mensaje):
    await mensaje.channel.send("El jugador 2 ingresa una palabra y jugador 1 debe adivinar")
    palabra=input().upper()

    ahorcado(palabra)

#Funcion del bot que elegira una palabra al azar
def ahorcado_bot():
    palabra = palabra_valida(palabras)

    ahorcado(palabra)


###ARRANQUE DEL PROGRAMA
async def ahorcado_launch(mensaje):
  if mensaje.author == client.user:
        return

  await mensaje.channel.send("¡Ahorcado!")
  await mensaje.channel.send("¿Desea jugar contra el bot o prefiere hacerlo contra otro jugador?")
  await mensaje.channel.send("1. Bot")
  await mensaje.channel.send("2. Otro jugador")

  #Usuario elige si jugar contra bot u otro jugador
  if mensaje.content.startswith("!1"):
        await ahorcado_bot()
  elif mensaje.content.startswith("!2"):
        await ahorcado_jugador()