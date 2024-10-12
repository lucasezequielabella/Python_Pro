import discord
from discord.ext import commands
import youtube_dl

# Configuración de la aplicación
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Configuración de youtube_dl
ytdl_format_options = {
    'format': 'bestaudio',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

@bot.event
async def on_ready():
    print(f'Bot conectado como: {bot.user}')

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'Conectado a {channel}')
    else:
        await ctx.send('¡Debes estar en un canal de voz!')

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send('Desconectado del canal de voz.')
    else:
        await ctx.send('No estoy en un canal de voz.')

@bot.command()
async def play(ctx, url):
    if not ctx.voice_client:
        await ctx.send('¡No estoy en un canal de voz!')
        return
    
    async with ctx.typing():
        info = ytdl.extract_info(url, download=False)
        url = info['formats'][0]['url']
        ctx.voice_client.stop()
        ctx.voice_client.play(discord.FFmpegPCMAudio(url, **ffmpeg_options))
    
    await ctx.send(f'Reproduciendo: {info["title"]}')

@bot.command()
async def stop(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send('Detenido.')
    else:
        await ctx.send('No estoy reproduciendo nada.')

# Reemplaza 'TU_TOKEN_AQUI' con tu token real
bot.run('MTI5MjE3NTAwNTQ0MTg1NTY4MQ.GknQVf.LOVOAXDFwxPaMoAzkxPk-9HImyHZFzBicxZ6R4')