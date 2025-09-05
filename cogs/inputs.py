import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import asyncio
import time
import json

class Inputs(commands.Cog):

    def __init__(self, client):
        self.client = client




async def setup(client):
    await client.add_cog(Inputs(client))