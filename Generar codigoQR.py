import discord
from discord.ext import commands
import qrcode
import random
import io
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def nombre(ctx,*, habbo):
    web = f"https://habbo.es/home/{habbo}"

    qr = qrcode.QRCode(version=1,box_size=10,border=5)

    qr.add_data(web)
    qr.make(fit=True)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = r,g,b

    img = qr.make_image(back_color=(255, 255, 255), fill_color=rgb)

    with io.BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='codigoQR.png'))
        img.save("codigoQR.png")#Esto lo puedes eliminar si gustas
    
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications