import discord
from discord.ext import commands
import json
import pandas as pd

intents = discord.Intents.default()
intents.members = True
Client = discord.Client()
client = commands.Bot(command_prefix = ["!"], intents=intents)
# Add your bot Token to a JSON file and add the path below
ft = open('../token.JSON')
token = json.load(ft)
bot_token = token

async def on_ready(self):
    guild = client.get_guild()
    print ("I'm Online")
    for member in guild.members:
        print (guild.members)


@client.command()
async def memberlist(ctx):
    x = ctx.guild.members
    names = []
    ids = []
    for member in x:
        ids.append(member.id)
        names.append(member.name)
    df = pd.DataFrame({
		'Names':names,
        'IDs':ids
		})
    df.to_excel('./[PATH HERE]/report.xlsx')
    file = discord.File('./[PATH HERE]/report.xlsx')
    await ctx.message.author.send(str(ctx.message.author.mention) + ": here is the report!")
    await ctx.message.author.send(file=file)


client.run(bot_token)