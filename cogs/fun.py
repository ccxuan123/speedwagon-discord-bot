import discord
from discord.ext import commands
#import aiohttp
import random
from discord.ext.commands.core import command 
import requests

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #async def cog_before_invoke(self, ctx):
        #As the scrapping takes time, we trigger a `typing` indicator whenever any command in invoked.
        #await ctx.channel.trigger_typing()

    @commands.command(aliases = ['coin', 'flip'])
    async def coinflip(self, ctx):
        """Flip a coin"""
        sides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.mention}** flipped a coin and get **{random.choice(sides)}**!")

    @commands.command()
    async def dice(self, ctx, *, num=None):
        """Roll a dice"""
        if num == None:
            result = random.randint(1,6)
            dice_type = 'dice'
        else:
            result = random.randint(1,int(num))
            dice_type = 'd' + str(num)
        
        await ctx.send(f"**{ctx.author.mention}** rolled a {dice_type} and get {result}")

    @staticmethod
    def get_cat():
        url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(url).json()
        image_url = response[0]['url']
        return image_url

    @commands.command()
    async def cat(self, ctx):
        """Random cat image"""
        async with ctx.channel.typing():
            embed = discord.Embed()
            embed.set_image(url=self.get_cat())
            embed.set_footer(text="From https://api.thecatapi.com/")
            await ctx.send(embed=embed)

    #@commands.command()
    #async def dog(self, ctx):
    #   """Random dog image"""
    #   async with ctx.channel.typing():
    #        async with aiohttp.ClientSession() as cs:
    #            async with cs.get("https://random.dog/woof.json") as r:
    #                data = await r.json()
    ##                embed = discord.Embed()
     #               embed.set_image(url = data['url'])
    #                embed.set_footer(text = 'http://random.dog/')
    #                await ctx.send(embed=embed)


    @commands.command()
    async def refuse(self, ctx):
        """I refuse!!!"""
        embed = discord.Embed(title="I refuse!")
        embed.set_image(url='https://media.tenor.com/images/20c76a29e9da31861c56f416713b8462/tenor.gif')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunCommands(bot))