import discord 
import os
import random 
import praw
import hostbot
from hostbot import keep_alive
from itertools import cycle
from discord.ext import commands, tasks

#used prefix
client = commands.Bot(command_prefix=".")

#cycle bot statuses
status = cycle(['Coded By: Luffyguy', '.help', " with Luffyguy"])

#remove default help command
client.remove_command('help')

#tells us when bot is active
@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready")

#loop bot statuses
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#says hi
@client.command()
async def hello(ctx):
    await ctx.send("Hi")

#just laughs
@client.command()
async def laugh(ctx):
    await ctx.send("Ha Ha Ha.....")    

#responds randomly
@client.command()
async def lol(ctx): 
    responces = [
        "Was it that funny?",
        "Noob Alert!",
        "Watch your tone dude!",
        "You are that dumb Lmao",
        "No comments",
        "You are such a kid dude",
    ]
    await ctx.send(random.choice(responces))

#square of a number
@client.command()
async def square(ctx,number):
    squared_number = int(number) ** 2
    await ctx.send("The square of " + str(number) + " is " + str(squared_number))
 
#cube of a number 
@client.command()
async def cube(ctx,number1):
    cubed_number = int(number1) ** 3
    await ctx.send("The cube of " + str(number1) + " is " + str(cubed_number))

#adds 2 numbers
@client.command()
async def add(ctx,number1,number2):
    summed_number = int(number1) + int(number2)
    await ctx.send("The sum of " + str(number1) + " and " + str(number2) + " is " + str(summed_number))

#subtracts 2 numbers
@client.command()
async def diff(ctx,number1,number2):
    subtracted_number = int(number1) - int(number2)
    await ctx.send("The differnce of " + str(number1) + " and " + str(number2) + " is " + str(subtracted_number))

#to clear chat
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):#algorithm channel id          #project channel id
    if ctx.channel.id != 778499893249310730 and ctx.channel.id !=778225956971347988: 
        await ctx.channel.purge(limit=amount+1)   

#botcommands(embed)
@client.command()
async def botcommands(ctx):
    embed = discord.Embed(
        title = 'Commands',
        description = 'Prefix : .',
        
        colour = discord.Colour.red()
    )

    embed.set_footer(text='by Luffyguy')
    embed.set_image(url='https://media.giphy.com/media/8aSSX6v0OwcDsHYnZ7/giphy.gif')
    embed.set_thumbnail(url='https://media.giphy.com/media/oaqHoQWu1Bk9FB5wsv/giphy.gif')
    embed.set_author(name= "Luffy Bot",
    icon_url='https://imgur.com/f1nKCsD.png')
    embed.add_field(name= '- Add : ', value= '.add <number1> <number2>', inline=False)
    embed.add_field(name= '- Differnce : ', value= '.diff <number1> <number2>', inline=True)
    embed.add_field(name= '- Clear : ', value= '.clear [amount=1]>', inline=False)
    embed.add_field(name= '- Square : ', value= '.square <number1>', inline=True)
    embed.add_field(name= '- Cube : ', value= '.cube <number1>', inline=False)
    embed.add_field(name= '- Laugh : ', value= '.laugh', inline=True)
    embed.add_field(name= '- Hello : ', value= '.hello', inline=False)
    embed.add_field(name= '- Lol : ', value= '.lol', inline=True)


    await ctx.send(embed=embed)

#new help(embed  dm)
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.green()
    )
    
    
    embed.set_footer(text='by Luffyguy')
    embed.set_image(url='https://media.giphy.com/media/8aSSX6v0OwcDsHYnZ7/giphy.gif')
    embed.set_thumbnail(url='https://media.giphy.com/media/oaqHoQWu1Bk9FB5wsv/giphy.gif')
    embed.set_author(name= "Help",
    icon_url='https://imgur.com/f1nKCsD.png')
    embed.add_field(name= '- Add : ', value= '.add <number1> <number2>', inline=False)
    embed.add_field(name= '- Differnce : ', value= '.diff <number1> <number2>', inline=True)
    embed.add_field(name= '- Clear : ', value= '.clear [amount=1]>', inline=False)
    embed.add_field(name= '- Square : ', value= '.square <number1>', inline=True)
    embed.add_field(name= '- Cube : ', value= '.cube <number1>', inline=False)
    embed.add_field(name= '- Laugh : ', value= '.laugh', inline=True)
    embed.add_field(name= '- Hello : ', value= '.hello', inline=False)
    embed.add_field(name= '- Lol : ', value= '.lol', inline=True)
    
    await ctx.message.author.send(embed=embed)

#server info
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

#reddit memes

reddit = praw.Reddit(client_id = "rp16UQQI7E6Qkw",client_secret = "m78JwvMdyphmvEyhueITWMy-az_B3Q",username = "your username",password = "your password",user_agent = "Luffybot")

@client.command(pass_context=True)
async def meme(ctx,subred = 'memes'):

    subreddit = reddit.subreddit(subred)
    all_subs =[]
    
    top = subreddit.top(limit = 50)
    for submission in top:
        all_subs.append(submission)

    random_sub =random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name, color=discord.Colour.green())
    em.set_image(url = url)
    
    channel = client.get_channel(778661570980741160)
    await channel.send(embed = em)

keep_alive()

#put your token here
client.run("Your token")
