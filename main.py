import keep_alive
import discord
from discord.ext import commands
import song
import os

cogs = [song]
client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

keep_alive.keep_alive()
my_secret = os.environ['discord_token']
client.run(my_secret)