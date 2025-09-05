import discord
from discord.ext import commands
from discord import Spotify
import random
import datetime
from datetime import datetime
import asyncio


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kill(self, ctx, innocent : discord.Member = None):
        if innocent == None:
            suicide = ['https://i.imgur.com/Y8a2UdS.gif',
                       'https://i.gifer.com/ANtJ.gif',
                       'https://imgur.com/Lw24A3n',
                       'https://media.tenor.com/images/a2fe7c4c0024e3ecd604c4cb01ae6cbf/tenor.gif'
                       'https://tenor.com/view/bird-jump-%E0%B8%99%E0%B8%81%E0%B9%82%E0%B8%94%E0%B8%94-%E0%B8%99%E0%B8%81-%E0%B9%82%E0%B8%94%Ehttps://tenor.com/view/bird-jump-%E0%B8%99%E0%B8%81%E0%B9%82%E0%B8%94%E0%B8%94-%E0%B8%99%E0%B8%81-%E0%B9%82%E0%B8%94%E0%B8%94-gif-13943434']
            killer = ctx.message.author
            embed = discord.Embed(description=f"**{killer.mention} Suicided!**")
            embed.set_image(url='{}'.format(random.choice(suicide)))
            await ctx.send(embed=embed)

        else:
            animation = ['https://i.pinimg.com/originals/9b/bc/10/9bbc10969b7558185c4c6cc915f1ff41.gif',
                         'https://media.giphy.com/media/3o6ZtjOzPmwYelxmla/giphy.gif',
                         'https://i.pinimg.com/originals/ef/49/93/ef4993b593954811a0c0a1c98af698a3.gif',
                         'https://i.pinimg.com/originals/3c/ed/ee/3cedee4f8118855c83ea05463498f326.gif',
                         'https://i.imgur.com/MGziZVa.gif',
                         'https://i.pinimg.com/originals/cc/87/65/cc87656cf72979fb8ee01c3eebc5cdff.gif',
                         'https://33.media.tumblr.com/ebc76b3228d7c93199035a5a448091de/tumblr_nekoxdVlve1titzlso1_500.gif',
                         'https://24.media.tumblr.com/tumblr_m6hij9iyIg1rwcc6bo1_400.gif',
                         'https://i.imgur.com/U6TAdE0.gif',
                         'https://i.gifer.com/ANu5.gif',
                         'https://media.tenor.com/images/09f8864588bbc1c4fa3b9bd351550569/tenor.gif',
                         'https://i.gifer.com/ANtb.gif',
                         'https://nerdschalk.com/wp-content/uploads/2020/10/tenor-16.gif']
            killer = ctx.message.author
            embed = discord.Embed(description=f"**{killer.mention} Killed {innocent.mention}**")
            embed.set_image(url='{}'.format(random.choice(animation)))
            await ctx.send(embed=embed)

    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        spot = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        if spot is None:
            emb = discord.Embed(description=f"User {user.name} is not listening to Spotify!", color=0xe74c3c)
            await ctx.send(embed=emb)
            return
        embed = discord.Embed(title=f"{user.name}'s Spotify", color=0xC902FF)
        embed.add_field(name="Song", value=spot.title, inline=False)
        embed.add_field(name="Artist", value=spot.artist, inline=False)
        embed.add_field(name="Album", value=spot.album, inline=False)
        embed.add_field(name="Track Link", value=f"[{spot.title}](https://open.spotify.com/track/{spot.track_id})", inline=False)
        embed.set_thumbnail(url=spot.album_cover_url)
        await ctx.send(embed=embed)

    @commands.command(case_insensitive=True, aliases=["remind", "remindme", "remind_me"])
    async def reminder(self, ctx, time, *, reminder):
        print(time)
        print(reminder)
        user = ctx.message.author
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
        embed.set_footer(
            text="Discord Server: discord.gg/otop",
            icon_url=f"{self.client.user.avatar_url}")
        seconds = 0
        if reminder is None:
            embed.add_field(name='Warning',
                            value='Please specify what do you want me to remind you about.')  # Error message
        if time.lower().endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"
        if time.lower().endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hours"
        elif time.lower().endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minutes"
        elif time.lower().endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} seconds"
        if seconds == 0:
            embed.add_field(name='Warning',
                            value='Please specify a proper duration, send `reminder_help` for more information.')
        elif seconds < 300:
            embed.add_field(name='Warning',
                            value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
        elif seconds > 7776000:
            embed.add_field(name='Warning',
                            value='You have specified a too long duration!\nMaximum duration is 90 days.')
        else:
            await ctx.send(f"Alright, I will remind you about {reminder} in {counter}.")
            await asyncio.sleep(seconds)
            await ctx.send(f"Hi, you asked me to remind you about `{reminder}` {counter} ago. {user.mention}")
            return
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Fun(client))
