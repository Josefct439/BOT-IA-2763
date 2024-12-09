import discord
from discord.ext import commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url 
            await ctx.send(f"Archivo guardado en ./{file_name }")
            await attachment.save(f"./{file_name}") 

            try:
                class_name = get_class("keras_model.h5", "labels.txt", file_name)
                if class_name[0] == "Palomas":
                    await ctx.send("Esta es una paloma y ella puede comer lo siguiente: ......")
                
                elif class_name[0] == "Gorriones":
                    await ctx.send("Esta es un Gorrion y puede comer lo siguiente: ......")
            
            except:
                await ctx.send("Ha ocurrido un error, seguro que usaste una imagen???...")
    else:
        await ctx.send("Olvidaste subir una imagen :(") 



bot.run("TU TOKEN")