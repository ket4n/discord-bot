import discord
from discord.ext import commands
from discord import Member, Role
import asyncio

class Rolesystem(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, name, color:discord.Colour=0xffffff):
        guild = ctx.guild
        await guild.create_role(name=name, color=color)
        mbed = discord.Embed(description=f"Successfully Create Role {name}.", color=color)
        await ctx.send(embed=mbed)

    @createrole.error
    async def createrole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            roleembed = discord.Embed(description="Uh Oh! It seems that you do not have permission to do that!", color=0xE74C3C)
            await ctx.send(embed=roleembed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, section, member: discord.Member, role: Role):
        if section == 'add':
            await member.add_roles(role)
            await ctx.send('**Succesfully Added Role To User**' + member.mention + '**!**')

        if section == 'remove':
            await member.remove_roles(role)
            await ctx.send('**Succesfully Removed Role From User**' + member.mention + '**!**')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def newrole(self, ctx, name, color:discord.Colour=0xffffff):
            guild = ctx.guild
            await guild.create_role(name=name, color=color)
            mbed = discord.Embed(description=f"Successfully Created Role {name}.", color=color)
            await ctx.send(embed=mbed)


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def delrole(self, ctx, role_name):
            role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
            await role_object.delete()
            m1bed = discord.Embed(description=f"Successfully Deleted Role {role_object}.", color=0xffffff)
            await ctx.send(embed=m1bed)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def roles(self, ctx):
        guild = ctx.guild
        roles = [role for role in guild.roles if role != ctx.guild.default_role]
        embed = discord.Embed(title="Server Roles", description=f"\n".join([role.mention for role in roles]))
        await ctx.send(embed=embed)

    @commands.command()
    async def inrole(self, ctx, role : discord.Role):
        people = "\n".join(map(str, role.members))
        embed = discord.Embed(title=f"Users With {role.name}",
                              description=people)
        await ctx.send(embed=embed)






async def setup(client):
    await client.add_cog(Rolesystem(client))