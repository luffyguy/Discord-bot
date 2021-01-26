import discord 
import os
import random 
import praw
import hostbot
from hostbot import keep_alive
from itertools import cycle
from discord.ext import commands, tasks
from dotenv import load_dotenv
import requests
import math
import random
import pyjokes
import datetime
from imgurpython import ImgurClient
import configparser


load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
#used prefix
client = commands.Bot(command_prefix=".",intents=intents)

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
async def hi(ctx):
    await ctx.send("Hello")

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
async def bc(ctx):
    embed = discord.Embed(
        title = 'Commands',
        description = '```\nPrefix : .```',
        
        colour = discord.Colour.red()
    )
    embed.set_footer(text='by Luffyguy')
    embed.set_image(url='https://media.giphy.com/media/8aSSX6v0OwcDsHYnZ7/giphy.gif')
    embed.set_thumbnail(url='https://media.giphy.com/media/oaqHoQWu1Bk9FB5wsv/giphy.gif')
    embed.set_author(name= "Luffy Bot",
    icon_url='https://imgur.com/f1nKCsD.png')
    embed.add_field(name= '- Hi/Lol/Laugh : ', value= '```\n.hi/lol/laugh```', inline=False)
    embed.add_field(name= '- Add : ', value= '```\n.add <number1> <number2>```', inline=False)
    embed.add_field(name= '- Differnce : ', value= '```\n.diff <number1> <number2>```', inline=True)
    embed.add_field(name= '- Clear Chat : ', value= '```\n.clear [amount=1]>```', inline=False)
    embed.add_field(name= '- Square/Cube : ', value= '```\n.square/cube <number>```', inline=True)
    embed.add_field(name= '- Wallpapers : ', value= '```\n.wp <keyword>```', inline=True)
    embed.add_field(name= '- Meme : ', value= '```\n.meme <keyword>```', inline=False)
    embed.add_field(name= '- Gif : ', value= '```\n.gif <keyword>```', inline=True)
    embed.add_field(name= '- Server Info : ', value= '```\n.server```', inline=True)
    embed.add_field(name= '- Jokes : ', value= '```\n.joke```', inline=True)
    embed.add_field(name= '- Bot Commands: ', value= '```\n.bc```', inline=True)
    await ctx.send(embed=embed)

#new help(embed  dm)
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = 'Help',
        description = '```\nPrefix : .```',
        colour = discord.Colour.red()
    )
    embed.set_footer(text='by Luffyguy')
    embed.set_image(url='https://media.giphy.com/media/8aSSX6v0OwcDsHYnZ7/giphy.gif')
    embed.set_thumbnail(url='https://media.giphy.com/media/oaqHoQWu1Bk9FB5wsv/giphy.gif')
    embed.set_author(name= "Help Commands",
    icon_url='https://imgur.com/f1nKCsD.png')
    embed.add_field(name= '- Hi/Lol/Laugh : ', value= '```\n.hi/lol/laugh```', inline=False)
    embed.add_field(name= '- Add : ', value= '```\n.add <number1> <number2>```', inline=False)
    embed.add_field(name= '- Differnce : ', value= '```\n.diff <number1> <number2>```', inline=True)
    embed.add_field(name= '- Clear Chat : ', value= '```\n.clear [amount=1]>```', inline=False)
    embed.add_field(name= '- Square/Cube : ', value= '```\n.square/cube <number>```', inline=True)
    embed.add_field(name= '- Wallpapers : ', value= '```\n.wp <keyword>```', inline=True)
    embed.add_field(name= '- Meme : ', value= '```\n.meme <keyword>```', inline=False)
    embed.add_field(name= '- Gif : ', value= '```\n.gif <keyword>```', inline=True)
    embed.add_field(name= '- Server Info : ', value= '```\n.server```', inline=True)
    embed.add_field(name= '- Jokes : ', value= '```\n.joke```', inline=True)
    embed.add_field(name= '- Bot Commands: ', value= '```\n.bc```', inline=True)
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
        title = name + " Server Information",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)

#reddit memes

reddit = praw.Reddit(client_id = "_xC37StY7xVaAg",client_secret = os.getenv('R_CLIENTSECRET'),username = os.getenv('R_USERNAME'),password = os.getenv('R_PASSWORD'),user_agent = "Luffybot")

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
    
    #channel = client.get_channel(778661570980741160)
    #await channel.send(embed = em)
    await ctx.send(embed = em)

#jokes
@client.command()
async def joke(ctx):
    await ctx.send(pyjokes.get_joke()) 

#fetch wallpapers from wallhaven.cc
@client.command()
async def wp(ctx,keyword='anime'):
       
        response = requests.get('https://wallhaven.cc/api/v1/search?q='+keyword +'&purity=100&apikey='+os.getenv('WALL_API'))
        json1=response.json()
        print(json1)
        index=math.floor(random.random() * len(json1['data']))
        channel = client.get_channel(778649939764576338)
        try:
            await channel.send(json1['data'][index]["path"])
        except:
            response = requests.get('https://wallhaven.cc/api/v1/search?q=anime' +'&purity=100&apikey='+os.getenv('WALL_API'))
            json1=response.json()
            index=math.floor(random.random() * len(json1['data']))
            channel = client.get_channel(778649939764576338)
            await channel.send(json1['data'][index]["path"])
            #await ctx.send(json1['data'][index]["path"])
        finally:
            auth = ctx.author
            channel = client.get_channel(778649939764576338)
            await channel.send(f'here {auth.mention}')

#fetch nsfw wallpapers from wallhaven.cc
@client.command()
async def sx(ctx,keyword='nude'):  
 
        response = requests.get('https://wallhaven.cc/api/v1/search?q='+keyword +'&purity=111&apikey='+os.getenv('WALL_API'))
        json1=response.json()
        print(json1)
        index=math.floor(random.random() * len(json1['data']))
        channel = client.get_channel(803603760953294889)
        try:
            await channel.send(json1['data'][index]["path"])
        except:
            response = requests.get('https://wallhaven.cc/api/v1/search?q=nude' +'&purity=111&apikey='+os.getenv('WALL_API'))
            json1=response.json()
            index=math.floor(random.random() * len(json1['data']))
            channel = client.get_channel(803603760953294889)
            await channel.send(json1['data'][index]["path"])
            #await ctx.send(json1['data'][index]["path"])
        #finally:
            #auth = ctx.author
            #channel = client.get_channel(803603760953294889)
            #await channel.send(f'here {auth.mention}')

#fetch gif 
@client.command()
async def gif(ctx,keyword='code'):

        response = requests.get('https://api.tenor.com/v1/search?q='+keyword+'&key='+os.getenv('TENOR')+'&limit=8')
        json1=response.json()
        print(json1)
        index=math.floor(random.random() * len(json1['results']))
        try:
            await ctx.channel.send(json1['results'][index]["url"])
        except:
            response = requests.get('https://api.tenor.com/v1/search?q=code&key='+os.getenv('TENOR')+'&limit=8')
            json1=response.json()
            index=math.floor(random.random() * len(json1['results']))
            await ctx.channel.send(json1['results'][index]["url"])   

@client.command()
async def nsfw(ctx,subred = 'NSFW_Wallpapers'):

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
    
    channel = client.get_channel(803603760953294889)
    await channel.send(url)

#fetch images from imgur
@client.command()
async def img(ctx,keyword='anime'):
    config = configparser.ConfigParser()
    config.read('auth.ini')

    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)

    # Extracts the items (images) on the front page of imgur.
    items = client.gallery_search(f'{keyword}', advanced=None, sort='time', window='all', page=0)
    n=math.floor(random.random()*len(items))
    await ctx.channel.send(items[n].link+'.jpg')


#welcome message
@client.event
async def on_member_join(member):
    guild =client.get_guild(777598102882091018)
    channel = guild.get_channel(778645688929615902)

    embed = discord.Embed(
        title = "**Welcome**",
        description = (f'Welcome to the {guild.name } server , {member.mention}!:partying_face: \n You are the {len(list(member.guild.members))} member ! '),
        colour = discord.Colour.green(),
        timestamp=datetime.datetime.utcfromtimestamp(1611660157)

    )
    embed.set_footer(text='by Luffyguy')
    embed.set_image(url='https://media.giphy.com/media/8aSSX6v0OwcDsHYnZ7/giphy.gif')
    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name= "HellHole",
    icon_url=f'{member.guild.icon_url}')
    await channel.send(embed=embed)
    await member.send(embed=embed)
   


keep_alive()

client.run(TOKEN)
