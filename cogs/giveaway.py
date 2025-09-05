import discord
import datetime
import time
import asyncio
from asyncio import sleep
import random

from discord.ext import commands
from discord import Embed, TextChannel


class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    def convert(self, time):
        pos = ["s", "m", "h", "d"]
        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}
        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reroll(self, ctx, id_ : int):
        try:
            new_msg = await ctx.fetch_message(id_)
        except:
            await ctx.send(f'ID was incorrect!')
            return

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        await ctx.send(f'Congrats! New Winner Is {winner.mention}.')

    @commands.command()
    @commands.guild_only()
    async def gstart(self, ctx, duration, *, prize):
        time = self.convert(duration)
        if time == -1:
            await ctx.send(f'Answer Time With A Proper Unit (s, m, h, d)')
            return
        elif time == -2:
            await ctx.send(f'Time Must Be A Integer!')
            return
        giveawayembed = discord.Embed(
            title="🎉 New Giveaway! 🎉",
            description=f"**Prize:** {prize}\n"
                        f"**Hosted By:** {ctx.author.mention}\n",
            colour=discord.Color.green()
        )

        msg = await ctx.send(embed=giveawayembed)

        reactions = await msg.add_reaction("🎉")

        while time >= 0:

            if time <= 60:
                giveawayembed.remove_field(index=0)
                giveawayembed.insert_field_at(index=1, name='Ends:', value=f'{time} second(s) from now')
                await msg.edit(embed=giveawayembed)
                time -= 10
                await asyncio.sleep(10)
            elif 60 <= time < 3600:
                giveawayembed.remove_field(index=0)
                giveawayembed.insert_field_at(index=1, name='Ends:', value=f'{time/60} minute(s) from now')
                await msg.edit(embed=giveawayembed)
                time -= 6
                await asyncio.sleep(6)
            elif 3600 <= time < 86400:
                giveawayembed.remove_field(index=0)
                giveawayembed.insert_field_at(index=1, name='Ends:', value=f'{time/3600} hour(s) from now')
                await msg.edit(embed=giveawayembed)
                time -= 360
                await asyncio.sleep(360)
            elif time >= 86400:
                giveawayembed.remove_field(index=0)
                giveawayembed.insert_field_at(index=1, name='Ends:', value=f'{time/86400} day(s) from now')
                await msg.edit(embed=giveawayembed)
                time -= 8640
                await asyncio.sleep(8640)
        if time <= 0:
            giveawayembed.remove_field(index=0)
            giveawayembed.insert_field_at(index=1, name='Ends:', value=f'Ended at {datetime.datetime.now().strftime("%B %d, %I:%M %p")}') # noqa
            await msg.edit(embed=giveawayembed)

        await asyncio.sleep(time)

        new_msg = await ctx.fetch_message(msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        endembed = discord.Embed(
            title="Giveaway ended!",
            description=f"Prize: {prize}\nWinner: {winner.mention}")

        await msg.edit(embed=endembed)
        await ctx.send(f"🎉 Giveaway Winner: {winner.mention} | Prize: {prize}")



async def setup(client):
    await client.add_cog(Giveaway(client))