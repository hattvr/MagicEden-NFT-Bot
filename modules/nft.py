import discord, asyncio, sys, json
from discord.ext import commands

ME_URL = "https://api-mainnet.magiceden.dev/v2/collections/{}"
MARKETPLACE = json.load(open('config.json', 'r'))['nfts']
channel_id = json.load(open('config.json', 'r'))['settings']['log-channel']
guild_id = json.load(open('config.json', 'r'))['settings']['guild']


class NFT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "hidden"
        self.bot.loop.create_task(self.update_status())

    async def update_status(self):
        if "dev" in sys.argv:
            return
        prev_fp = [0.0] * len(MARKETPLACE)
        
        while True:
            prev_fp = await self.stats(prev_fp)
            # Loop timer, default is set to 600
            await asyncio.sleep( int(json.load(open('config.json', 'r'))['settings']['refreshrate']) ) 

    async def stats(self, prev_fp):
        new_fp = [0.0] * len(MARKETPLACE)
        for i in range(len(MARKETPLACE)):
            response = await (await self.bot.session.get(ME_URL.format(MARKETPLACE[i].lower()))).json()
            fp = float(response["floorPrice"]) / 1000000000
            new_fp[i] = fp
            if (fp > prev_fp[i]):
                embedColor = discord.Color.brand_green()
            elif (fp < prev_fp[i]):
                embedColor = discord.Color.brand_red()
            else:
                embedColor = discord.Color.light_grey()

            embed = discord.Embed(
                title = response["name"],
                description=f"**Floor Price**: {fp} SOL\n**List count**: {response['listedCount']}\n **[MagicEden](https://magiceden.io/marketplace/{response['name'].lower()})**",
                color = embedColor
            )
            embed.set_thumbnail(url=response["image"])

            channel = self.bot.get_guild(int(guild_id)).get_channel(int(channel_id))
            await channel.send(embed=embed)
        return new_fp


async def setup(bot):
    await bot.add_cog(NFT(bot))
