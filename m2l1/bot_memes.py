import discord
from discord.ext import commands
import random, os

description = '''An example.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=':', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def meme11(ctx):
    img_name = random.choice(os.listdir('./M2L1/images'))
    with open(f'./M2L1/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("MTI4OTYyODIzNzE1NjMxOTMzMg.Gp49Ce.L0laXx_CZjKJMlOt3KxnhL2DO6HnmUyKV36Ud8")
