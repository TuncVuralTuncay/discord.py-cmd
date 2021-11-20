from playsound import playsound
import discord
from discord.ext import commands
import random
import datetime
ds = datetime.datetime.now()

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot("/",intents=intents)




@Bot.event
async def on_message(message):
  print(f"""
{ds.day}/{ds.month}/{ds.year}  {ds.hour}:{ds.minute}
[{message.author}]: {message.content}""")


@Bot.event
async def on_ready():
  print(f"""
  Kullanıcı adı {Bot.user.name}
  Token : {Bot.user.id}""")
  await Bot.change_presence(activity=discord.Game(name='Tuncvr code ',type=random.randint(1,3)))
Bot.run("ODc3NjM1OTE0OTA4NzI5MzY0.YR1gIw.2sWhgXOtFPD4g5Ta8imOCLeT1PY")
