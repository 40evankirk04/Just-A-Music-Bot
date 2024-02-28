import json
import os

from src.bot import Bot

def main():
    
    bot_token = os.environ.get('BOT_TOKEN')

    with open("jamb\\configs\\lavalink_server.json", "r", encoding="utf-8") as server_cfg:

        lavalink_server = json.load(server_cfg)

    bot = Bot(

        lavalink_server.get('host'), 
        lavalink_server.get('port'),
        lavalink_server.get('password')
    )
    
    cogs_list = ['music_player', 'client']
    
    for cog in cogs_list:
        bot.load_extension(f'src.cogs.{cog}')

    bot.run(bot_token)

if __name__ == "__main__":
    main()