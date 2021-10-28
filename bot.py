import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(903333111973163019)
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(903333170508869713)
    await channel.send(f"{member} leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} (ms)")



bot.run("OTAzMjc5Nzc0MjQ2NTEwNjUz.YXqq2A.QnLa9bFro0jh-NQVUYzVDc0VCT0")
