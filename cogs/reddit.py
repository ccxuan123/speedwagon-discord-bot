import discord
from discord.ext import commands

import os
import asyncpraw
import random

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


def setup(bot):
    bot.add_cog(Reddit(bot))