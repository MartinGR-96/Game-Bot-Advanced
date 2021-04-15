import discord
import os
import random
import tateti_game
import ahorcado

client = discord.Client()

greet_bot = ["hey", "sup", "hi", "hello"]

@client.event
async def on_ready():
    print("We logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ahorcado"):
        await ahorcado.ahorcado_launch(message)

    if message.content.startswith("!tateti"):
        await tateti_game.tateti_launch(message)

    if any(word in message.content for word in greet_bot):
        await message.channel.send(random.choice(greet_bot))


client.run(os.getenv("TOKEN"))
