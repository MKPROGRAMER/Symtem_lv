import os
import discord
from discord.ext import commands
import keep_alive

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix="*")

client.load_extension("commands") # Note, we don't need the .py file extension

my_secret = os.environ['SECRET']
keep_alive.keep_alive()
client.run("SECRET")

