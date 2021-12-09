import discord
import requests
from discord.ext import commands, tasks

# Setup the bot
intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='$', intents=intents, case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    f = open("past.log", "w")
    print(f"╔═══════════════════════════════════════════════════")
    print(f"╠Bot is ready")
    print(f"╠IP Watcher")
    print(f"╠By BoredManCodes")
    print(f"╠Discord API Version: {discord.__version__}")
    print(f"╚═══════════════════════════════════════════════════")
    url = "https://ip4.seeip.org"
    page = requests.get(url)
    embed = discord.Embed(
        title=f"The IP address has changed!",
        description=f"The current IP address is {page.text}:25565",
        colour=discord.Colour.blue()
    )

    await bot.get_channel(CHANNEL ID).send(embed=embed)  # put your channel ID here


@tasks.loop(minutes=15)  # every 15 minutes check if the IP changed
async def check():
    url = "https://ip4.seeip.org"
    page = requests.get(url)
    with open("past.log", "r") as f:
        data = f.read()
    if not data == page.text:  # if the old IP does not equal the current one
        with open("past.log", "w") as f:
            f.write(page.text)
        embed = discord.Embed(
            title=f"The IP address has changed!",
            description=f"The current IP address is {page.text}:25565",
            colour=discord.Colour.blue()
        )

        await bot.get_channel(786017749523628082).send(embed=embed)

check.start()

bot.run("TOKEN")
