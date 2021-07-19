import discord
from discord import channel
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=';', intents=intents)


@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(866593287749632030)
    await channel.send(f'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(866593287749632030)
    await channel.send(f'{member} leave!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('ODY2NTgxOTIyMzg1MzYyOTQ2.YPUpTg.Ue-qgCQ7QiMrjTTzH6FYqM65_DI')
