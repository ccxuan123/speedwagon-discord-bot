import discord
import datetime
from discord.ext import commands

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def modtest(self, ctx):
        await ctx.send('Cog `mod` is working')

def setup(bot):
    bot.add_cog(mod(bot))
