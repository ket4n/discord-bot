import discord
from discord.ext import commands
import json

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, section=None):
        if section == None:
            with open("prefixes.json", "r") as f:
                data = json.loads(f.read())
                guildID = str(ctx.guild.id)
                prefix = data[guildID]
                mbed = discord.Embed(title="Command Section", color=0xE74C3C)
                mbed.add_field(name="Basic Commands", value=f"`{prefix}help basic`", inline=False)
                mbed.add_field(name="Moderation Commands", value=f"`{prefix}help mod`", inline=False)
                mbed.add_field(name="Role Commands", value=f"`{prefix}help role`", inline=False)
                mbed.add_field(name="Extra Commands", value=f"`{prefix}help extras`", inline=False)
                mbed.set_footer(text=f"Bot Prefix `{prefix}`")
                await ctx.send(embed=mbed)

        if section == 'basic':
            with open("prefixes.json", "r") as f:
                data = json.loads(f.read())
                guildID = str(ctx.guild.id)
                prefix = data[guildID]
                m1bed = discord.Embed(title="Basic Commands", color=0xE74C3C)
                m1bed.add_field(name="Time Command", value=f"`{prefix}time`", inline=False)
                m1bed.add_field(name="Bot Info Command", value=f"`{prefix}info`", inline=False)
                m1bed.add_field(name="Avatar Command", value=f"`{prefix}av`, `{prefix}av @user/userID`", inline=False)
                m1bed.add_field(name="Server Description Command", value=f"`{prefix}description`", inline=False)
                m1bed.add_field(name="Server Info Command", value=f"`{prefix}serverinfo`", inline=False)
                m1bed.add_field(name="User Info Command [Admin] ", value=f"`{prefix}userinfo`", inline=False)
                m1bed.set_footer(text=f"Bot Prefix `{prefix}`")
                await ctx.send(embed=m1bed)

        if section == 'mod':
            with open("prefixes.json", "r") as f:
                data = json.loads(f.read())
                guildID = str(ctx.guild.id)
                prefix = data[guildID]
                m2bed = discord.Embed(title="Moderation Commands", color=0xe74c3c)
                m2bed.add_field(name="Warn Command", value=f"`{prefix}warn @user [reason]`", inline=False)
                m2bed.add_field(name="Mute Command", value=f"`{prefix}mute @user [reason]`", inline=False)
                m2bed.add_field(name="Unmute Command", value=f"`{prefix}unmute @user`", inline=False)
                m2bed.add_field(name="Kick Command", value=f"`{prefix}kick @user [reason]`", inline=False)
                m2bed.add_field(name="Ban Command", value=f"`{prefix}ban @user [reason]`", inline=False)
                m2bed.add_field(name="Unban Command", value=f"`{prefix}unban [userID]`", inline=False)
                m2bed.add_field(name="Clear Messages Command", value=f"`{prefix}clear [no. of messages]`", inline=False)
                m2bed.set_footer(text=f"Bot Prefix `{prefix}`")
                await ctx.send(embed=m2bed)

        if section == 'role':
            with open("prefixes.json", "r") as f:
                data = json.loads(f.read())
                guildID = str(ctx.guild.id)
                prefix = data[guildID]
                m3bed = discord.Embed(title="Role Commands", color=0xe74c3c)
                m3bed.add_field(name="Add Role Command", value=f"`{prefix}role add @user [roleName/roleID]`", inline=False)
                m3bed.add_field(name="Remove Role Command", value=f"`{prefix}role remove @user [roleName/roleID]`", inline=False)
                m3bed.add_field(name="Create Role Command ", value=f"`{prefix}newrole [roleName] [HexColor]`", inline=False)
                m3bed.add_field(name="Delete Role Command ", value=f"`{prefix}delrole [roleName/roleID]`", inline=False)
                m3bed.add_field(name="Users In Given Role Command ", value=f"`{prefix}inrole [rolename/roleID]`", inline=False)
                m3bed.add_field(name="Server Roles Command  [Admin]", value=f"`{prefix}roles`", inline=False)
                m3bed.set_footer(text=f"Bot Prefix `{prefix}`")
                await ctx.send(embed=m3bed)

        if section == 'extras':
            with open("prefixes.json", "r") as f:
                data = json.loads(f.read())
                guildID = str(ctx.guild.id)
                prefix = data[guildID]
                m4bed = discord.Embed(title="Extra Commands", color=0xe74c3c)
                m4bed.add_field(name="Suggestion Command", value=f"`{prefix}suggest [suggestion]`", inline=False)
                m4bed.add_field(name="Open Ticket Command", value=f"`{prefix}ticket`", inline=False)
                m4bed.add_field(name="Close Ticket Command [Admin]", value=f"`{prefix}close`", inline=False)
                m4bed.add_field(name="Giveaway Start Command [Admin]", value=f"`{prefix}gstart [duration (s, m , h, d)] [prize]`", inline=False)
                m4bed.add_field(name="Giveaway Reroll Command [Admin]", value=f"`{prefix}reroll [giveawayMsgID]`", inline=False)
                m4bed.add_field(name="Spotify Song Status Command", value=f"`{prefix}spotify [userMention/userID]`", inline=False)
                m4bed.add_field(name="Reminder Command [5 Min - 90 Days]", value=f"`{prefix}remind [duration] [reminder]`", inline=False)
                m4bed.add_field(name="Kill Command [Fun]", value=f"`{prefix}kill [userMention/userID]`", inline=False)
                m4bed.set_footer(text=f"Bot Prefix `{prefix}`")
                await ctx.send(embed=m4bed)


async def setup(client):
    await client.add_cog(Help(client))
