import discord
import asyncio

from config import *
from commands import commands

class Engine():

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
    
    async def run(self):
        has_prefix = self.message.content.startswith("!")
        if has_prefix:
            if is_maintenance and self.message.author.id not in MAINTENANCE_AUTHORIZE:
                pass
            else:
                self.message.content = self.message.content.lower()
                command_info = commands.get(self.message.content[1:].split()[0])
                command = command_info[0]
                must_reg = command_info[1]
                await command(self.message, self.bot).run()
