import discord
from discord.ext import commands
import os
from model import get_class

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

#görseller için klasörü oluşturuyoruz.
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR,exist_ok=True)#klasör yoksa oluştur
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
    if ctx.message.attachments: #eğer bağlamdaki mesajda ekler varsa
        for attachment in ctx.message.attachments:
            file_name = attachment.filename 
            file_path = os.path.join(IMAGE_DIR,file_name) #images klasörünün altına yerleşicek şekilde dosya yolu belirliyoruz.
            await attachment.save(file_path) 
            await ctx.send(f"{file_name}görseliniz başarılı şekilde kaydolmuştur.")
            try:
                class_name ,skor =  get_class(image=file_path )
                await ctx.send(f"görselinizin sınıfı: {class_name}, tahmin skoru: {skor}")
                if class_name =="dog":
                    await ctx.send(f"köpekler çok tatlıdır.")
                elif class_name =="at":
                    await ctx.send("atlar güzel hayvanlardır.")
                elif class_name =="kedi":
                    await ctx.send("kediler tatlıdır.")
                elif class_name == "baykuş":
                    await ctx.send("baykuşlar çok güzel.")
                elif class_name == "koyun":
                    await ctx.send("koyunlar çok güzel.")
                else:
                    await ctx.send("ördekler çok  güzel hayvanlardır.")
            except Exception as e:
                await ctx.send(f"şuanda işlemi yapamıyoruz hata bu:{e}")    
    else:
        await ctx.send("görsel göndermeyi unuttunuz,lütfen gönderin!")


bot.run()