import discord
from discord.ext import commands
import os
import datetime

client = discord.Client()
client = commands.Bot(command_prefix = '$')

#logging for bot
@client.event
async def on_connect():
    print(f'Bot {client.user} is connected to discord')

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

@client.event
async def on_resumed():
    print(f'Bot {client.user} is resumed to session')

@client.event
async def on_disconnect():
    print(f'Bot {client.user} is disconnected')

#test command
@client.command(aliases = ['t', 'hello'])
async def test(ctx):
    await ctx.send('Are you testing me?')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        #name = file[:-3]
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]} cog has been imported')

client.run(os.environ['DISCORD_TOKEN'])
 