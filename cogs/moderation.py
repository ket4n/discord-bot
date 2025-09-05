import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from discord import user



class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member:discord.Member, *, reason=None):
        if reason == None:
            mbed = discord.Embed(description="Please Provide A Reason!", color=0xE74C3C)
            await ctx.send(embed=mbed)
        else:
            channel_id = 785494238229299250
            channel = self.client.get_channel(channel_id)
            mod = ctx.message.author
            await ctx.send(f"**You Are Being Warned For {reason} {member.mention}!**")
            await channel.send(f"{mod} Has Warned {member} For {reason}!")

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            warnembed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!", color=0xE74C3C)
            await ctx.send(embed=warnembed)

    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            kickembed = discord.Embed(description="Please Provide A Reason!", color=0xe74c3c)
            await ctx.send(embed=kickembed)

        else:
            await member.kick()
            await ctx.send('Member ' + member.mention + ' Has Been Kicked!')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            kickembed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!", color=0xE74C3C)
            await ctx.send(embed=kickembed)

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member=None, *, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.send('Lmfao! You Can Not Ban Yourself!')
            return
        if reason == None:
            reason = 'For Being A Jerk!'
        message = f'You Have Been Banned From {ctx.guild.name} {reason}!'
        await member.send(message)
        await member.ban(reason=reason)
        await ctx.send('Member ' + member.mention + f' Has Been Banned. **Reason**: {reason}  !')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            banembed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!", color=0xE74C3C)
            await ctx.send(embed=banembed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self , ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {len(deleted)} messages")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            clearembed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!", color=0xE74C3C)
            await ctx.send(embed=clearembed)

    @commands.command(name='unban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned User Successfully!")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            unbanembed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!", color=0xE74C3C)
            await ctx.send(embed=unbanembed)

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member:discord.Member=None, reason=None):
        if member == None:
            mbed = discord.Embed(description="Please Mention A User!")
            await ctx.send(embed=mbed)

        else:
            user = ctx.message.author
            role = get(member.guild.roles, name="Muted")
            await member.add_roles(role)
            await ctx.send(f"Successfully Muted User {member.mention} for {reason}!")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            muteembed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!",
                                       color=0xE74C3C)
            await ctx.send(embed=muteembed)

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member = None):
        if member == None:
            mbed = discord.Embed(description="Please Mention A User!")
            await ctx.send(embed=mbed)

        else:
            user = ctx.message.author
            role = get(member.guild.roles, name="Muted")
            await member.remove_roles(role)
            await ctx.send(f"Successfully Unmuted User {member.mention}!")


    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!",
                                       color=0xE74C3C)
            await ctx.send(embed=   embed)


async def setup(client):
    await client.add_cog(Moderation(client))

