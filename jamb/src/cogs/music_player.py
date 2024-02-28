import wavelink
import discord

from .. bot import Bot

class MusicPlayer(discord.Cog):
    
    def __init__(self, bot: Bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:

        print(f"Node '{payload.node.identifier}' is ready.")

def setup(bot: Bot):
    bot.add_cog(MusicPlayer(bot))