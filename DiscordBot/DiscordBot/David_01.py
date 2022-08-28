import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import urllib
from eth_server import *

# ===== Variables =====
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


# ===== bot connection ======
@client.event
async def on_ready():
    print("------------------------------------")
    print("[+] David Is Connected to the server")


# ==== member activity =======
@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_ID)
    await channel.send(f'Welcome to the group {member.mention}')


@client.event
async def on_member_remove(member):
    channel = client.get_channel(channel_ID)
    await channel.send(f'{member.mention} Has left the group')


# ===== slash commands ======
@client.slash_command(name="hei", description="Replies with hello", guild_ids=[server_ID])
async def hello_command(interaction: Interaction):
    await interaction.response.send_message('Hei')


# @client.slash_command(name="help", description="Show to search engine", guild_ids=[server_ID])
# async def help_command(interaction: Interaction, ):
# await interaction.response.send_message(urllib - "https://www.google.com/")


client.run(BOT_TOKEN)
