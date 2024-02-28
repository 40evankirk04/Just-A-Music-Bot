import discord
import wavelink

class Bot(discord.Bot):

    def __init__(self, host: str, port: int, password: str, intents: discord.Intents = discord.Intents.default()):

        self.host = host
        self.port = port
        self.password = password

        super().__init__(intents=intents)

    @discord.Cog.listener()
    async def on_ready(self):
        
        await self.connect_node()

    async def connect_node(self):

        """Connect to our Lavalink nodes."""

        await self.wait_until_ready()

        node: wavelink.Node = wavelink.Node(

            uri=f"http://{self.host}:{self.port}", 
            password=f"{self.password}"
        )
        
        await wavelink.Pool.connect(nodes=[node], client=self)