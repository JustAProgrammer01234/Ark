import os
import disnake
from disnake.ext import commands 

guilds = []

if len(guilds) == 0:
    guilds = None 

ark = commands.Bot(
    description="A discord bot.",
    test_guilds=guilds
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
        color=disnake.Colour(value=11393254)
    )
    embed.add_field(name="Latency:", value=f"`{ark.latency*1000:.2f}ms`")
    embed.set_thumbnail("https://c.tenor.com/LqNPvLVdzHoAAAAC/cat-ping.gif")
    await inter.response.send_message(embed=embed)

@ark.slash_command(description="Adds two numbers.")
async def add(inter, addend1: int, addend2: int):
    await inter.response.send_message(addend1 + addend2)

ark.run(os.getenv("TOKEN"))