import discord
import os
import random

client = discord.Client()
 
greet_bot = ["hey", "sup", "hi", "hello"]


@client.event
async def on_ready():
    print("We logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content for word in greet_bot):
        await message.channel.send(random.choice(greet_bot))


client.run(os.getenv("TOKEN"))
