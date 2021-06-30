import datetime

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='-', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print("Duhh, The LAZY Bot is here")

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Chilz-Bot commands",
        description="All commands listed below",
        color=discord.Color.red(),
        author="Raghav"
    )
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1071582837030060032/kKV-I01n.jpg")
    embed.add_field(name="-help", value="Gives a list of all commands", inline="False")
    embed.add_field(name="-server", value="Information about the server", inline="False")
    embed.add_field(name="-hello", value="Says Hello", inline="False")
    embed.add_field(name="-clear", value="Deletes messages specifying the amount or after a particular date or both", inline="False")
    embed.add_field(name="-kick", value="Kicks the member from the server", inline="False")
    embed.add_field(name="-ban", value="Bans the member from the server", inline="False")
    embed.add_field(name="-unban", value="Unbans the member from the server", inline="False")

    await ctx.send(embed=embed)

@client.command()
async def hello(ctx, *args):
    await ctx.send("Hello there!!")

@client.command()
async def server(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    region = ctx.guild.region
    icon = ctx.guild.icon_url
    memberCount = ctx.guild.member_count
    owner = str(ctx.guild.owner)

    embed = discord.Embed(
        title=name+"'s Server Information",
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count",value=memberCount, inline="True")

    await ctx.send(embed=embed)

@client.command()
@commands.has_role(859748628969291776)
async def clear(ctx, amount, month=None, day=None, year=None):
    if(amount == '-'):
        amount=None
    else:
        amount = int(amount) + 1
    if(month==None or day==None or year==None):
        date=None
    else:
        date = datetime.datetime(int(year), int(month), int(day))

    await ctx.channel.purge(limit=amount, after=date)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permissions to use this command")

@client.command()
@commands.has_role(859748628969291776)
async def kick(ctx, member: discord.Member, *, reason):
    await member.kick(reason=reason)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permissions to use this command")

@client.command()
@commands.is_owner()
async def ban(ctx, member: discord.Member, *, reason):
    await member.ban(reason=reason)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Only the owner can use this command")

@client.command()
@commands.is_owner()S
async def unban(ctx, *, member):
    banned_members = await ctx.guild.bans()
    for person in banned_members:
        user = person.user
        if member == str(user):
            await ctx.guild.unban(user)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Only the owner can use this command")

client.run('TOKEN')