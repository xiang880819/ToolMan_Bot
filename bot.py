import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=';')


@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('ODY2NTgxOTIyMzg1MzYyOTQ2.YPUpTg.zQbFdGJDvn_IFB4nw2V_BYxs9WA')
