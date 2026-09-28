import requests
from   urllib.parse import quote
import discord
from discord.ext import commands
from  config import TOKEN


description = '''An example bot to showcase the discord.ext.commands extension
module. 
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def imagecreate(ctx,prompt):
    download_image(prompt)
    file = discord.File("generated_image.jpg")
    await ctx.send(file=file)


def download_image(prompt):
    encoded_prompt= quote(prompt)
    url = f"https://image.pollinations.ai/image/{encoded_prompt}"
    response = requests.get(url)
    with open('generated_image.jpg', 'wb') as file:
        file.write(response.content)
    print('Resim indirildi!')
    return "generated_image.jpg"

bot.run(TOKEN)