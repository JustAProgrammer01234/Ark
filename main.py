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
    intents=intents,
    activity=disnake.Game("Type /"),
    status=disnake.Status.dnd 
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
    bot_user = ark.user
    embed = disnake.Embed(
        title="Some info about me:",
        color=disnake.Colour(value=color)
    )
    embed.add_field(name="Owner:", value=info.owner)
    embed.add_field(name="Bot ID:", value=bot_user.id)
    embed.add_field(name="Created at:", value=disnake.utils.format_dt(bot_user.created_at, style="F"))
    embed.add_field(name="Servers I'm in:", value=len(ark.guilds))
    embed.add_field(name="Current number of commands:", value=len(ark.slash_commands))
    embed.set_thumbnail(ark.user.avatar)

    await inter.response.send_message(embed=embed)

ark.run(os.getenv("TOKEN"))