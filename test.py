import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.command()
async def log(ctx):
    mychannel = ctx.channel
    print(f"Command used in: {mychannel.id}, Name:{mychannel.name}, Category:{mychannel.category}")
    await ctx.send("Hello world!")

@bot.event
async def on_guild_channel_create(channel):
    my_category = 1234745442743488512

    if channel.category_id == my_category:
        print("New channel has been created.")
        print(f"Channel ID: {channel.id}, Name:{channel.name}, Category:{channel.category}")

    #Either a Modal for user to write info here

    #Log info on MongoDB    

bot.run('')
