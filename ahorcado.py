import random
import string
import discord
from ahorcado_palabras import palabras

client=discord.Client()
#Funcion para seleccionar una palabra al azar de ahorcado_palabras
@client.event
async def palabra_valida(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

#FUNCION PRINCIPAL DE AHORCADO
@client.event
async def ahorcado(palabra):
    #Declaracion de variables
    palabra_letras = set(palabra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()
    vidas = 6

    #Bucle de juego. No termina hasta quedar sin mas vidas
    while vidas > 0 and len(palabra_letras) > 0:
        await client.channel.send("Tienes", vidas, "vidas")
        await client.channel.send("Has usado estas letras:", " ".join(letras_usadas))

        palabra_lista = [letra if letra in letras_usadas else "-" for letra in palabra]
        await client.channel.send("Palabra actual:", " ".join(palabra_lista))

        letra_usuario = input("Adivina un letra: ").upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in palabra_letras:
                palabra_letras.remove(letra_usuario)
            else:
                vidas = vidas - 1
                await client.channel.send("La letra", letra_usuario, "no está en la palabra")
        elif letra_usuario in letras_usadas:
            await client.channel.send("Ya has probado con la letra", letra_usuario, ".")
        else:
            await client.channel.send("Carácter inválido.")

        await client.channel.send("------------------------------")
    if vidas == 0:
        await client.channel.send("¡Perdiste! La palabra era", palabra)
    else:
        await client.channel.send("¡Correcto! La palabra es", palabra)

#Funcion del jugador que ingresa una palabra para adivinar
@client.event
async def ahorcado_jugador(mensaje):
    await mensaje.channel.send("El jugador 2 ingresa una palabra y jugador 1 debe adivinar")
    palabra=input().upper()

    ahorcado(palabra)

#Funcion del bot que elegira una palabra al azar
@client.event
async def ahorcado_bot():
    palabra = await palabra_valida(palabras)

    await ahorcado(palabra)

###ARRANQUE DEL PROGRAMA
@client.event
async def ahorcado_launch(mensaje):
  if mensaje.author == client.user:
        return

  await mensaje.channel.send("¡Ahorcado!")
  await mensaje.channel.send("¿Desea jugar contra el bot o prefiere hacerlo contra otro jugador?")
  await mensaje.channel.send("1. Bot")
  await mensaje.channel.send("2. Otro jugador")

  #Usuario elige si jugar contra bot u otro jugador
  if mensaje.content.startswith("!ahorcado"):
        await ahorcado_bot()
  elif mensaje.content.startswith("!2"):
        await ahorcado_jugador()