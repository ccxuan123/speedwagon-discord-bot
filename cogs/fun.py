import discord
from discord.ext import commands
import asyncio
import random
from discord.ext.commands.core import command 
import requests

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        """need to fix the refresh button or delete it"""
        embed = discord.Embed()
        
        embed.set_image(url=self.get_cat())
        
        message = await ctx.send(embed=embed)
        await message.add_reaction('🔃')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '🔃'
        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        if str(reaction.emoji) == '🔃':
            new_image_url = self.get_cat()
            embed_refresh = discord.Embed()
            embed_refresh.set_image(url=new_image_url)
            await message.edit(embed=embed_refresh)

    

def setup(bot):
    bot.add_cog(FunCommands(bot))