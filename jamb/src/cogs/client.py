import discord
from discord.ext import commands

from .. bot import Bot

class Client(commands.Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):

        print(f'Logged in {self.bot.user} | {self.bot.user.id}')

        await self.bot.change_presence(activity=discord.Game("вашем ритме"))

def setup(bot: Bot):
    bot.add_cog(Client(bot))