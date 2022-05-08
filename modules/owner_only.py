import os
from discord.ext import commands

class eval(commands.Cog):
    def __init__(self, bot):
        self.name = "hidden"
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, cmd):
        if ctx.author.id not in self.bot.owner_list:
            return await ctx.reply("You are not authorized to use this command!")
            
        found = False
        for path, subdirs, files in os.walk("modules"):
            for name in files:
                if name.endswith(".py") and name[:-3] == cmd:
                    name = os.path.join(name)[:-3]
                    path = (os.path.join(path).replace("/", ".")).replace("\\", ".")
                    filepath = path + "." + name
                    try:
                        await self.bot.reload_extension(filepath)
                        await ctx.send("Reloaded: `" + filepath + "`")
                        found = True
                    except:
                        await self.bot.load_extension(filepath)
                        await ctx.send("Loaded: `" + filepath + "`")
                        found = True
                else:
                    continue

        if not found:
            await ctx.send("Extension `" + cmd + "` was not found!")

async def setup(bot):
    await bot.add_cog(eval(bot))