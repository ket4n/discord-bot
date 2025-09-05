import discord
import time
from datetime import datetime
from discord.ext import commands

class Base(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Time module! Used `import time` Needs to create a time variable and then a useable variable as so !
    @commands.command()
    async def time(self, ctx):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        await ctx.send(current_time)

    @commands.command()
    async def info(self, ctx):
        servers = str(len(self.client.guilds))
        verEmbed = discord.Embed(title="Info", color=0xF39C12)
        verEmbed.add_field(name="Bot Owner:",
                           value="<@!617665985150713858>", inline=False)
        verEmbed.add_field(name="Bot ID:",
                           value="784074217352200203", inline=False)
        verEmbed.add_field(name="Serving Servers:",
                           value=f"{servers}", inline=False)
        verEmbed.set_footer(text="Made By Nucleo")

        await ctx.send(embed=verEmbed)

    @commands.command(pass_context=True)
    async def av(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.message.author
            pfp = user.avatar_url
            mbed = discord.Embed(description="User Avatar", color=0x000000)
            mbed.set_author(name=f"{user.name}", icon_url=pfp)
            mbed.set_image(url=(pfp))
            await ctx.send(embed=mbed)
        else:
            pfp = user.avatar_url
            mbed = discord.Embed(title=f"{user.name}", description="User Avatar", color=0x000000)
            mbed.set_image(url=(pfp))
            await ctx.send(embed=mbed)


    @commands.command()
    async def suggest(self, ctx, *, suggestion=None):
        if suggestion == None:
            mbed = discord.Embed(description="Missing Argument!", color=0xE74C3C)
            await ctx.send(embed=mbed)
        else:
            author = ctx.message.author
            m1bed = discord.Embed(title="Suggestion", description=f"{suggestion}")
            m1bed.set_footer(text=f"Suggestion By {author}.")
            message = await ctx.send(embed=m1bed)

            emojis   = ['✅', '❌']

            for emoji in emojis:
                await message.add_reaction(emoji)

    @commands.command(aliases=["mc"])
    async def membercount(self, ctx):
        count = ctx.guild.member_count
        mbed = discord.Embed(title=f"Members: ", description=count, color=0xe74c3c)
        await ctx.send(embed=mbed)

    @commands.command(aliases=['gn'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def giftnitro(self, ctx, member : discord.User):
        try:
            embed = discord.Embed(title=f"You Have Been Gifted A Nitro From {ctx.message.author}", description="Gift Link: https://discord.gift/klmn43j34k3", color=0xe74c3c)
            await member.send(embed=embed)
            await member.send("https://cdn.discordapp.com/attachments/784344319221039123/790549432206622750/xedy9ugkqo621.png")
            await ctx.send(f"<a:Seop_nitro:790557438990090280> Successfully Gifted A Nitro To {member.mention}!")
        except:
            await ctx.send("**Mentioned User\'s DMs Are Off!**")

    @giftnitro.error
    async def giftnitro_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            gnembed = discord.Embed(description="Uh Oh! It seems that you are on a cooldown of 1 min to use this command again!",
                                      color=0xE74C3C)
            await ctx.send(embed=gnembed)

    @commands.command(aliases=["si"])
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner.mention)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        def_role = str(ctx.guild.default_role)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.add_field(name="Default Role", value=def_role, inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, target: discord.Member):
        if ctx.author.guild_permissions.administrator:
            x = ctx.guild.members
            if target in x:
                roles = [role for role in target.roles if role != ctx.guild.default_role]
                embed = discord.Embed(title="User information", colour=discord.Color.gold(),
                                      timestamp=datetime.utcnow())

                embed.set_author(name=target.name, icon_url=target.avatar_url)

                embed.set_thumbnail(url=target.avatar_url)

                fields = [("Name", str(target), False),
                          ("ID", target.id, False),
                          ("Status", str(target.status).title(), False),
                          (f"Roles ({len(roles)})", " ".join([role.mention for role in roles]), False),
                          ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                          ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(embed=embed)
            else:
                await ctx.send(f'You have to ping someone from this server')
        else:
            await ctx.send(f'Not enough permissions')






async def setup(client):
    await client.add_cog(Base(client))