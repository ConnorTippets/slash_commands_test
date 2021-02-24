from discord_slash import SlashCommand, SlashContext
from discord.ext import commands
from properties import token
import discord
import discord_slash
import time

client = commands.Bot(command_prefix='sc!', intents = discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print("Ready!")

@slash.slash(name = "ping", description='test command')
async def ping(ctx: SlashContext):
    s = time.perf_counter()
    msg = await ctx.send('l')
    t = time.perf_counter()
    e = (t - s)*1000
    await msg.edit(embed = discord.Embed(title = "Pong", description=f'Responded in {round(e, 6)}ms'), content='')

client.run(token)
