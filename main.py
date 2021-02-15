import discord
from discord.ext import commands
import os
import datetime

client = discord.Client()
client = commands.Bot(command_prefix = '$')
client.remove_command("help")

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

@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        title = "Help"
    )

    embed.add_field(name="$coinflip", value="Flip a coin", inline=False)
    embed.add_field(name="$dice <number of sides>", value="Roll a dice, default is 6 sides", inline=False)
    embed.add_field(name="$cat", value="Random picture of a meow", inline=False)
    embed.add_field(name="$dog", value="Random picture of a woof", inline=False)
    embed.add_field(name="$ping", value="Returns Pong!", inline=False)
    embed.add_field(name="$invite", value="Invite me to your server", inline=False)
    embed.add_field(name="$reference", value="The references when creating this bot", inline=False)
    embed.add_field(name="$source", value="Check out this source code", inline=False)
    embed.add_field(name="$ping", value="Returns Pong!", inline=False)
    embed.add_field(name="$nh_get <id>", value="Search nHentai manga with id", inline=False)
    embed.add_field(name="$nh_search <keyword>", value="Search nHentai manga with keyword", inline=False)
    embed.add_field(name="$nh_random", value="Random nHentai manga", inline=False)
    embed.add_field(name="$meme", value="Hot meme from r/meme", inline=False)
    embed.add_field(name="$jojomeme", value="JoJo meme from r/ShitPostCrusaders", inline=False)
    embed.add_field(name="$thigh", value="Lewd thigh pic from r/thighdeology", inline=False)

    await author.send(embed=embed)
    await ctx.send(":inbox_tray: The list of commands has been sent to your DMs.")

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        #name = file[:-3]
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]} cog has been imported')

client.run(os.environ['DISCORD_TOKEN'])
 