# Genshin Domain Schedule Bot
import discord, os, traceback, json
from colorama import Fore, init
from aiohttp import ClientSession
from discord.ext import commands

# Read config file and grab username/password
token = json.load(open('config.json', 'r'))['settings']['token']

# Declare intents
intents = discord.Intents.default()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="domain!", intents=intents)
        self.remove_command('help')
        self.session: ClientSession

    async def on_ready(self):
        print(f"[{Fore.GREEN}!{Fore.RESET}] Bot has started successfully!") # Set up production/development bot
        self.session = ClientSession(loop=self.loop)
        await self.load_modules()
        await self.change_presence(status=discord.Status.online, activity=discord.Game('github.com/hattvr'))

    async def load_modules(self):
        for path, subdirs, files in os.walk("modules"):
            for name in files:
                if name.endswith(".py"):
                    name = os.path.join(name)[:-3]
                    path = (os.path.join(path).replace("/", ".")).replace("\\", ".")
                    filepath = path + "." + name
                    try:
                        await self.load_extension(filepath)
                        print(f"{Fore.LIGHTGREEN_EX}Loaded:{Fore.RESET} " + filepath)
                    except:
                        print(f"{Fore.RED}Error:{Fore.RESET} {filepath}\n" + traceback.format_exc())
                else:
                    continue
                  
init()
Client().run(token)