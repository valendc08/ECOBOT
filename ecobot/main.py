import discord
import random
from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("chau")
    elif message.content.sarswith('$password'):
        await message.channel.send(gen_pass(10))

    else:
        await message.channel.send(message.content)

client.run("MTE1MDA3NTczMzE0MjY3NTUzOA.GbYW_5.IkC9uheJIGLm87k3Q6c9wBw5UjZNd69-hWq678")