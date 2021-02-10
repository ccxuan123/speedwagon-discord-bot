import discord
import time
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_before_invoke(self, ctx):
        #As the scrapping takes time, we trigger a `typing` indicator whenever any command in invoked.
        await ctx.channel.trigger_typing()

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")
    
    @commands.command(aliases=['joinme', 'join', 'botinvite'])
    async def invite(self, ctx):
        """ Invite me to your server """
        await ctx.send(f"**{ctx.author.mention}**, use this URL to invite me\n<{discord.utils.oauth_url(self.bot.user.id)}>")

    @commands.command()
    async def reference(self, ctx):
        """Without them this bot would not exist!🙇"""
        # Reference: https://github.com/AlexFlipnote/discord_bot.py/blob/master/LICENSE
        embed = discord.Embed(
            title = "Reference:books:"
        )
        embed.description = \
            f"`Bot framework`   :   [discord_bot.py](https://github.com/AlexFlipnote/discord_bot.py) made by AlexFlipnote#0001\n" + \
            f"`nHentai cogs`    :   [Jiraya-bot](https://github.com/kiranajij/Jiraya-bot) made by kiranajij\n" + \
            f"`discord.py API`  :   [Documentation](https://discordpy.readthedocs.io/en/latest/index.html)\n" + \
            f"`Coding Shifu`    :   [Brian](https://www.instagram.com/d_brain_b/)\n" + \
            f"\nThe developer copy the code from them to create {ctx.bot.user.name}"
        
        await ctx.send(embed=embed)

    @commands.command()
    async def source(self, ctx):
        """Check out my source code"""
        await ctx.send (f"**{ctx.bot.user}** is powered by this source code:\nhttps://github.com/ccxuan123/speedwagon-discord-bot")


def setup(bot):
    bot.add_cog(Information(bot))