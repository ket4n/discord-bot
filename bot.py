import discord
import os
import time
import datetime
from datetime import datetime
from datetime import timedelta
from discord.ext import commands
import json
import asyncio



intents = discord.Intents.all()

with open("prefixes.json") as f:
    prefixes = json.load(f)
default_prefix = "."

def get_prefix(client, message):
    prefix = default_prefix
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(client, message)

client = commands.Bot(
    command_prefix= get_prefix, case_insensitive=True,
    intents=intents
    )


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'`Prefix changed to:` {prefix}')


client.remove_command('help')

@client.event
async def on_ready():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(current_time)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Old Town Members Talk"))

@client.event
async def on_message(message):
    bot_mention = '<@!838356754218876968>'
    if bot_mention in message.content:
        with open("prefixes.json", "r") as f:
            data = json.loads(f.read())
            guildID = str(message.guild.id)
            prefix = data[guildID]
            channel = message.channel
            msg = f'Prefix: `{prefix}`'
            await channel.send(msg)

    await client.process_commands(message)

    

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency * 1000)) + ' ms')

@client.command()
async def alarm(ctx, time):
    now = datetime.now()
    mtimeA = time
    mtimeB = mtimeA.split(":")
    hr = int(mtimeB[0])
    min = int(mtimeB[1])
    secsleft = int((timedelta(hours=24) - (now - now.replace(hour=hr, minute=min, second=0, microsecond=0))).total_seconds() % (24 * 3600))
    await ctx.send(f"OK\nAlarm set to {time}")
    def check(message):
        return message.author == ctx.author and message.content.lower() == "cancel alarm"
    try:
        await client.wait_for("message", check=check, timeout=secsleft)
        await ctx.send("Alarm cancelled")
    except:
        await ctx.send(f"{ctx.author.mention} alarm finished")




@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

async def load_extension():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
    async with client:
        await load_extension()
        await client.start('')

asyncio.run(main())
# client.run('')

