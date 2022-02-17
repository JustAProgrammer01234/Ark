import os
import disnake
from disnake.ext import commands 

intents = disnake.Intents.default()
color = 11393254
guilds = []

if len(guilds) == 0:
    guilds = None 

ark = commands.Bot(
    description="A discord bot.",
    test_guilds=guilds,
    sync_commands = True,
    intents=intents 
)

@ark.event
async def on_connect():
    print("Bot is connected.")

@ark.event 
async def on_ready():
    print("Bot is ready.")

@ark.slash_command(description="Sends the bot's ping.")
async def ping(inter):
    embed = disnake.Embed(
        title="Pong!", 
        color=disnake.Colour(value=color)
    )
    embed.add_field(name="Latency:", value=f"`{ark.latency*1000:.2f}ms`")
    embed.set_thumbnail("https://c.tenor.com/LqNPvLVdzHoAAAAC/cat-ping.gif")
    await inter.response.send_message(embed=embed)

@ark.slash_command(description="Sends info about the bot.")
async def botinfo(inter):
    info = await ark.application_info()
    description = f"Owner: {info.owner}"
    embed = disnake.Embed(
        title="Some info about me:",
        description=description,
        color=disnake.Colour(value=color)
    )
    await inter.response.send_message(embed=embed)

ark.run(os.getenv("TOKEN"))