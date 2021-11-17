import discord
from discord.ext import commands
import song

cogs = [song]
client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("OTEwNDM1MDMxMTQ5ODM4MzY3.YZSysg.91babJdlQfosHd_KIy812cxCkPk")