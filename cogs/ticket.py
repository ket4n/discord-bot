import discord
from discord.ext import commands
import time
import asyncio

class Ticket(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ticket(self, ctx):
        guild = ctx.guild
        member = ctx.message.author
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.message.author: discord.PermissionOverwrite(read_messages=True)
        }

        channel = await guild.create_text_channel(f'Ticket {member}', overwrites=overwrites)
        message = await ctx.send("`Ticket Created!`")
        await message.add_reaction('✉️')

    @commands.command()
    async def close(self, ctx):
        if ctx.author.guild_permissions.administrator:
            channel = ctx.message.channel
            await ctx.send("`Closing ticket in 3 seconds...`")
            await asyncio.sleep(3)
            await channel.delete()

        else:
            embed = discord.Embed(description="Uh Oh! Only Admins Can Close Tickets!",
                                     color=0xE74C3C)
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Ticket(client))