import os
from dotenv import load_dotenv

load_dotenv()
my_token = os.getenv('DREWPH_DCTOKEN')

from pymongo import MongoClient


import discord
from discord.ext import commands
from discord.ui import View, Button, Select, Modal, TextInput

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)

#Either a Modal for user to write info here
class FeedbackModal(Modal, title="Details Form"):
    handle = TextInput(required=True, label="Provide your X handle", placeholder="@handle")
    address = TextInput(required=True, label="Provide your wallet address", placeholder="0x...")
    async def on_submit(self, interaction:discord.Interaction):
        await interaction.response.send_message(f"Thanks **{self.handle.value}**!", ephemeral=True)

class ModalView(View):
    def __init__(self):
        super().__init__()
        self.add_item(
                Button(label="Author",
                       url="https://github.com/imjakeym8",
                       style=discord.ButtonStyle.link))

    @discord.ui.button(label="Open Form", style=discord.ButtonStyle.success)
    async def button_callback(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_modal(FeedbackModal())

class MyEmbed(discord.Embed):
    def __init__(self):
        super().__init__(
            title="Need Support?",
            description="Press start filling up the form by pressing the button below.",
            color=discord.Colour.yellow()
        )
        self.set_thumbnail(
            url="https://images-ext-1.discordapp.net/external/qByp4BBBiV2q976hMJ4JD4cHvWs9eawF-g46405UpCo/%3Fcid%3D790b761199d506d04f0cee87ec5e42e315c015e6415cc589%26rid%3Dgiphy.gif%26ct%3Dg/https/media2.giphy.com/media/PfhDVTbCOsBxOMzemc/giphy.gif"
        )

@bot.event
async def on_guild_channel_create(channel):
    my_category = 1234745442743488512 

    if channel.category_id == my_category:
        print(f"New channel has been created on on {channel.category}.")
    try:
        await channel.send(embed=MyEmbed(),view=ModalView())
    except Exception as e:
        print("Failed to send message:", e)

bot.run(my_token)
