import sys, discord, datetime, asyncio, json, string, time
from discord.ext import commands
from datetime import datetime, timezone, timedelta
from pytz import timezone

talentascension = json.load(open("attributes/Guide/talentascension.json", "r"))
weaponascension = json.load(open("attributes/Guide/weaponascension.json", "r"))

class DomainSchedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "hidden"
        self.bot.loop.create_task(self.update_domains())

    def getServerTime(self, region: str):
        tz = timezone('US/Eastern')
        return {
            "America": (datetime.now(tz) - timedelta(hours=5)),
            "Europe": (datetime.now(tz) - timedelta(hours=1)),
            "Asia": (datetime.now(tz) + timedelta(hours=8))
        }.get(str(region))

    async def update_domains(self):
        if "dev" in sys.argv:
            return

        talents_channel = self.bot.get_channel(957878186639761448)
        weapons_channel = self.bot.get_channel(972744704489840700)
        await talents_channel.purge()
        await weapons_channel.purge()
        talents = await talents_channel.send("Updating...")
        weapons = await weapons_channel.send("Updating...")
        while True:
            await self.talents(talents)
            await self.weapons(weapons)
            await asyncio.sleep(600)

    async def talents(self, msg: discord.Message):
        # Genshin 
        regions = ["America", "Europe", "Asia"]
        attachments, embeds = [], []
        for region in regions:
            today = str(self.getServerTime(region).strftime("%A"))
            embed = discord.Embed(
                title = f"Talent Domains Overview [{region}]",
                color= discord.Color.blurple(),
            )
            desc=""
            domains = talentascension['data']['domains']
            for domain in domains:
                for talent in talentascension['data']['domains'][domain]['talent']:
                    for day in talent['days']:
                        if today == day:
                            if today == "Sunday":
                                desc = "All domains are available. Farm for **any** character you want today!"
                            else:
                                desc+= f"\n**Domain:** {string.capwords(domain.replace('_',' '))}\n**Book:** {string.capwords(talent['name'])}\n**Farmable For:**\n"
                                for character in talent["char"]:
                                    desc+= f"`{string.capwords(character['name'])}` "
                                desc+= "\n"
            domain_img = f"attributes/Images/TalentDomains/{today}.png"
            embed.set_image(url = f"attachment://{today}.png")
            embed.add_field(name=f"{today}'s Schedule", value=desc, inline=True)
            embed.add_field(name="\u200b", value=f'\n**Server Reset:** <t:{int((datetime.now(timezone("US/Eastern")) + timedelta(seconds=((24 - (self.getServerTime(region)).hour - 1) * 60 * 60) + ((60 - (self.getServerTime(region)).minute - 1) * 60) + (60 - (self.getServerTime(region)).second))).timestamp())}:R>\n**Last Updated:** <t:{int(time.time())}:R>', inline=False)
            embeds.append(embed)
            attachments.append(discord.File(domain_img))
        await msg.edit(embeds=embeds, attachments=attachments, content = None)
    
    async def weapons(self, msg: discord.Message):
        regions = ["America", "Europe", "Asia"]
        attachments, embeds = [], []
        for region in regions:
            today = str(self.getServerTime(region).strftime("%A"))
            embed = discord.Embed(
                title = f"Weapon Domains Overview [{region}]",
                color= discord.Color.blurple(),
            )
            desc=""
            domains = weaponascension['data']['domains']
            for domain in domains:
                for material in weaponascension['data']['domains'][domain]['material']:
                    for day in material['days']:
                        if today == day: 
                            if today == "Sunday":
                                desc = "All domains are available. Farm for **any** weapon you want today!"
                            else:
                                desc+= f"\n**Domain:** {string.capwords(domain.replace('_',' '))}\n**Material:** {string.capwords(material['name'])}\n**Farmable For:**\n"
                                for weapon in material["wpn"]:
                                    desc+= f"`{weapon}` "
                                desc+= "\n"
            domain_img = f"attributes/Images/WeaponDomains/{today}.png"
            embed.set_image(url = f"attachment://{today}.png")
            embed.add_field(name=f"{today}'s Schedule", value=desc, inline=True)
            embed.add_field(name="\u200b", value=f'**Server Reset:** <t:{int((datetime.now(timezone("US/Eastern")) + timedelta(seconds=((24 - (self.getServerTime(region)).hour - 1) * 60 * 60) + ((60 - (self.getServerTime(region)).minute - 1) * 60) + (60 - (self.getServerTime(region)).second))).timestamp())}:R>\n**Last Updated:** <t:{int(time.time())}:R>', inline=False)
            embeds.append(embed)
            attachments.append(discord.File(domain_img))
        await msg.edit(embeds=embeds, attachments=attachments, content = None)


async def setup(bot):
    await bot.add_cog(DomainSchedule(bot))
