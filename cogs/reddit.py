import discord
from discord.ext import commands

import os
import asyncpraw
import random

#need to fix the method of import custom_embeds
import sys
sys.path.append('..')
from utils.custom_embeds import ErrorEmbed

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(
            client_id = os.environ['REDDIT_APP_ID'],
            client_secret = os.environ['REDDIT_APP_SECRET'],
            user_agent = f"speedwagon-discord-bot:{os.environ['REDDIT_APP_ID']}:1.0",
            check_for_async = False
        )
        
    @commands.command()
    async def meme(self, ctx):
        """Meme from r/meme"""
        async with ctx.channel.typing():
            
            subreddit = await self.reddit.subreddit("meme")
            submission_list = [submission async for submission in subreddit.hot(limit=20) if not submission.stickied]
            selector = random.randint(0, len(submission_list) - 1)
            post = submission_list[selector]
            #embed = discord.Embed()
            #embed.set_image(url = post.url)
            #embed.set_footer(text = 'from r/meme')
            #await ctx.send(embed=embed)
            await ctx.send(post.url)

    @commands.command()
    async def jojomeme(self, ctx):
        "JoJo meme from r/ShitPostCrusaders"
        async with ctx.channel.typing():
            
            subreddit = await self.reddit.subreddit("ShitPostCrusaders")
            submission_list = [submission async for submission in subreddit.hot(limit=30) if not submission.stickied]
            selector = random.randint(0, len(submission_list) - 1)
            post = submission_list[selector]
            await ctx.send(post.url)

    @commands.command()
    async def thigh(self, ctx):
        "Lewd thigh pic from r/thighdeology"
        async with ctx.channel.typing():
            subreddit = await self.reddit.subreddit("thighdeology")
            submission_list = [submission async for submission in subreddit.rising(limit=30) if not submission.stickied]
            selector = random.randint(0, len(submission_list) - 1)
            post = submission_list[selector]
            embed = discord.Embed(
                colour = 0x46bac7,
                title = post.title,
                url = f"https://www.reddit.com{post.permalink}",
            )
            embed.set_image(url = post.url)
            embed.set_footer(text = "It's cold out, warm yourself between some thighs.")
            if(post.over_18 and not ctx.channel.is_nsfw()):
                await ctx.send(embed=ErrorEmbed("Channel is not NSFW"))
            else:
                await ctx.send(embed=embed)
            

def setup(bot):
    bot.add_cog(Reddit(bot))