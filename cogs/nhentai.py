import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands.cog import Cog

import logging
from hentai import Hentai, Format, Utils
import datetime

import sys
sys.path.append('..')
from utils.custom_embeds import ErrorEmbed

logging.basicConfig(level=logging.INFO, format="[%(levelname)s]\t%(message)s")

class NHentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_before_invoke(self, ctx: Context):
        """
        As the scrapping takes time, we trigger a `typing` indicator whenever
        any command in invoked.
        """
        await ctx.channel.trigger_typing()

    async def cog_command_error(self, ctx, error):
        logging.error(f'{type(error).__name__}:{error}')    #Log the error in the console
        
        if isinstance(error, commands.CheckFailure):
            await ctx.send(embed=ErrorEmbed("Channel is not NSFW"))
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(
                embed=ErrorEmbed(str(error)[str(error).find('[')+1::])
            )
        else:
            await ctx.send(embed=ErrorEmbed(str(error)))
    
    def cog_check(self, ctx: Context) -> bool:
        """
        Check if the channel is NSFW. The entire cog requires the channel to be NSFW
        """

        return ctx.channel.is_nsfw()


    @commands.command()
    async def nh_get(self, ctx, id):
        """<id>   Search the manga from Nhentai with id"""
        try:
            hnt = Hentai(id)

        except Exception:
            await ctx.send(embed=ErrorEmbed("Doujin doesn't exist! Try another one."))
            #raise ValueError("Doujin doesn't exist! Try another one.")
            
        else:
            embed = self.make_embed(hnt)
            await ctx.send(embed=embed)
    
    @commands.command(aliases = ['horny', 'lonely'])
    async def nh_random(self, ctx):
        """Randomly search manga from NHentai"""
        hnt = Utils.get_random_hentai()
        embed = self.make_embed(hnt)
        await ctx.send(embed=embed)
            
    
    @staticmethod
    def hentai_url(hnt: Hentai):
        return f"https://nhentai.net/g/{hnt.id}"

    @staticmethod
    def make_embed(hnt: Hentai):
        def convert(tag: list) -> str:
            lst = list(map(lambda x: x.name, tag))
            return ", ".join(lst)

        embed = discord.Embed(
            colour = discord.Colour.random(),
            title = hnt.title(Format.Pretty),
            url = f"https://nhentai.net/g/{hnt.id}"
        )

        embed.set_thumbnail(
            url=hnt.thumbnail
        )
        embed.set_image(url=hnt.cover)

        description = \
            f"`id`      :    {hnt.id}\n" + \
            f"`pages`   :    {hnt.num_pages}\n" + \
            f"`tags`    :    {convert(hnt.tag)}\n"

        if hnt.artist: description += f"`artist`   :   {convert(hnt.artist)}"

        embed.description = description
        embed.set_footer(text="Speedwagon Foundation got ur back")
        embed.timestamp = datetime.datetime.utcnow()
        return embed

def setup(bot):
    bot.add_cog(NHentai(bot))
