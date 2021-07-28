import discord
from discord import embeds
from discord.ext import commands
import discord_components
import os
import dotenv
from dotenv import load_dotenv

#Main part
prefix = '?'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

#token stuff
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Start Message
@bot.event 
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="Rhimzy#4452"))
    print("Logged in!")

#Ping command
@bot.command(aliases=['p'])
async def ping(ctx):
    await ctx.send(f'Ping {round(bot.latency * 1000)}ms')

#Test command
@bot.command(aliases=['t'])
async def test(ctx):
    await ctx.send('Yes i am working!')

#Clear command
@bot.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

#Help group
@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use ?help <command> for detailed information!",color = 0x00ffb7)
    em.add_field(name = "Basic", value = "Ping,Test,Help")
    em.add_field(name = "fun", value = "Kick,Ban,Warn")

    await ctx.send(embed = em)

@help.command()
async def ping(ctx):
    em = discord.Embed(title = "Ping", description = "Shows the Bot latency.", color = 0x00ffb7)
    em.add_field(name = "**Usage**", value = "?ping or ?p")
    await ctx.send(embed = em)

@help.command()
async def test(ctx):
    em = discord.Embed(title = "Test", description = "Just a useless command to check whether the bot is working or not.", color = 0x00ffb7)
    em.add_field(name = "**Usage**", value = "?test or ?t")
    await ctx.send(embed = em)




























bot.run(TOKEN)
