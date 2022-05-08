import discord, sys
from discord.ext import commands

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "hidden"
        self.guild = self.bot.get_guild(961360869172842556)
        self._cd = commands.CooldownMapping.from_cooldown(1, 30.0, commands.BucketType.member)

    def get_ratelimit(self, message: discord.Message):
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return bucket.update_rate_limit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if "dev" in sys.argv:
            return

async def setup(bot):
    await bot.add_cog(OnMessage(bot))
