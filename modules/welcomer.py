import discord, asyncio, os, json
from ordinal import ordinal
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw, ImageFont
from io import BytesIO

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "hidden"
        self.guild = int(json.load(open('config.json', 'r'))['settings']['guild'])
        self.welcome_channel = int(json.load(open('config.json', 'r'))['settings']['welcome-channel'])

    # Round profile picture
    def circle(pfp,size = (215,215)): 
        pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
        
        bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(pfp.size, Image.ANTIALIAS)
        mask = ImageChops.darker(mask, pfp.split()[-1])
        pfp.putalpha(mask)
        return pfp

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(self.guild)
        channel = guild.get_channel(self.welcome_channel)
        # await member.add_roles(guild.get_role(ID_OF_ROLE)) # You can add a default role to new joiners if you'd like here
        
        filename = f"results_{member.id}.png" # <- The name of the file that will be saved and deleted after (Should be PNG)

        background = Image.open("welcome.png") # <- Background Image (Should be PNG)
        # asset = member.avatar.with_size(1024) if member.avatar else "../genshinWizard/attributes/Avatars/default.png" # This loads the Member Avatar
        if member.avatar:
            asset = member.avatar.with_size(1024)
        else:
            asset = self.bot.user.avatar.with_size(1024)

        data = BytesIO(await asset.read())

        pfp = Image.open(data).convert("RGBA")
        pfp = Welcomer.circle(pfp)
        pfp = pfp.resize((226,226)) # Resizes the Profilepicture so it fits perfectly in the circle

        draw = ImageDraw.Draw(background)
        welcomeFont = ImageFont.truetype("../Welcomer-Bot/attributes/Fonts/Gotham-Black.otf",100)
        memberFont = ImageFont.truetype("../Welcomer-Bot/attributes/Fonts/Gotham-Black.otf",42)
        welcome_text = "WELCOME!"
        member_text = f"You are the {ordinal(len(guild.members))} user"  # <- Text under the Profilepicture with the Membercount

        W, H = (1024,500) # Canvas Dimensions

        w, h = draw.textsize(welcome_text, font=welcomeFont)
        draw.text(( (W-w)/2, 275 ),welcome_text,font=welcomeFont)

        w, h = draw.textsize(member_text, font=memberFont)
        draw.text(( (W-w)/2, 380 ),member_text,font=memberFont)

        background.paste(pfp, ( int((W-226)/2), 50), pfp) # Pastes the Profilepicture on the Background Image
        background.save(filename) # Saves the finished Image in the folder with the filename

        await channel.send(file = discord.File(filename),content ="Welcome to the discord server " + member.mention + "!") # <- The welcome Message Content put above the Image. "member.mention" @mentions the user
        await asyncio.sleep(5) # 5 Seconds of waiting time
        try:
            os.remove(filename) # <- Change your path to where the Bot is located. Tries to delete the file again so your folder won't be full of Images. If it's already deleted nothing will happen
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(Welcomer(bot))