import discord
import random
from discord import file
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=';', intents=intents)


@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['welcome']))
    await channel.send(f'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['welcome']))
    await channel.send(f'{member} leave!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')


@bot.command()
async def 派大星(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)


@bot.command()
async def shake(ctx):
    random_gif = random.choice(jdata['shake'])
    gif = discord.File(random_gif)
    await ctx.send(file=gif)


@bot.command()
async def av(ctx):
    await ctx.send('https://jable.tv')

bot.run(jdata['TOKEN'])
