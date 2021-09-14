import discord
import random
from kkep_alive import keepAlive
import requests
import json
import praw
import youtube_dl
from discord.ext import commands
import asyncio
import urllib.parse, urllib.request, re
from threading import Thread , Timer
from datetime import datetime
import asyncio
#biblio to install PyNaCl : Command : pip install PyNaCl

players = {}
reddit = praw.Reddit(client_id="KTWWAd45SNhgaA",client_secret="d09wNkztWALKaE055PFL8aI73j1NVg",username="Reference_Background",password="clashamin",user_agent="whatever")

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


warniwarniparol = "هي هي هيدي ور ني ورني ورني دي ورني ، ورني"

#client = discord.Client()
client = commands.Bot(command_prefix = '$$ ')
help = ["$$ 3ak3ak","$$ say my name","$$ chinhi","$$ hello","$$ ti warni warni","$$ tell me a joke","$$ 33070","$$calc","$$ meme","$$ cursedimages","$$ wow","$$ 9adarBot","$$ emergency meeting","$$ 5ra","$$ i'm sad","$$ l glace","$$ play Rock Paper Scissors with me"]
@client.event
async def on_ready():
  print("i'm here suckers")


@client.event
async def on_message(message):
  if message.author == client.user :
    return 
  await client.process_commands(message)
  usern = message.author.name
  if message.content.startswith("$$ 3ak3ak"):
    randomakak = ["wlahi 9ol tw l we7ed yched yemsa7 bik l 9e3a 😡 🤬","omlos ya 555555ra"]
    await message.channel.send(randomakak[random.randint(0,1)])
  elif message.content.startswith("$$ say my name"):
    usern = message.author.name
    if usern == "amin" :
      await message.channel.send("7adher, Si Amin")
    else :
      await message.channel.send("blehi bara e5tani 9alo say my name 9alo balot")
  elif message.content.startswith("$$ chinhi"):
      await message.channel.send("chinhi li chinhi?!?")
  elif message.content.startswith("$$ who is the the boss here ?") and message.author.name == "amin":
      await message.channel.send(message.author.name)
  elif message.content.startswith("$$ ti warni warni"):
      await message.channel.send(warniwarniparol)
  elif message.content.startswith("$$calc"):
      eq = message.content[6:len(message.content)]
      await message.channel.send(str(eq) +" = " + str(eval(eq)))
  elif message.content.startswith("$$ 9adarBot"):
      await message.channel.send("Si 9adarBot men fadhlek")
  elif message.content.startswith("$$ help"):
      await message.channel.send("chof ya si " +message.author.name+" manich kif l botet l o5rin la help la wedhni" )
      await message.channel.send("yala nfadlko ahom el available commands :")
      for t in help:
        await message.channel.send( " / " + t )
  elif message.content.startswith("$$ 5ra"):
    await message.channel.send("3la mandhrek ya 5imej ")
  elif message.content.startswith("$$ i'm sad"):
    await message.channel.send("mot you don't matter 😀")
  elif message.content.startswith("$$ i'm"):
    eq = message.content[6:len(message.content)]
    await message.channel.send("hi" + eq + " i'm 9adarBot Ha Ha Ha ")
  elif message.content.startswith("$$ l glace"):
    await message.channel.send("l GLLLLAAAASSSSS w L Birrrrra  🍺 🍻 🥂")
  elif message.content.startswith("$$ emergency meeting"):
    await message.channel.send("hey @everyone "+ message.author.name +" is in danger , or he/she is just beeing an asshole ")
  elif message.content.startswith("$$ 33070"):
    await message.channel.send("👇🍒 👉👀")
  elif message.content.startswith("$$ play Rock Paper Scissors with me"):
    await message.channel.send("ok i'll beat you ofc 😏 choose : $$ Rock | $$ Paper | $$ Scissors")
  elif message.content.startswith("$$ Rock"):
    await message.channel.send("Paper HaHa EZ 😂😂😂")
  elif message.content.startswith("$$ Paper"):
    await message.channel.send("Scissors HaHa EZ 😂😂😂")
  elif message.content.startswith("$$ Scissors"):
    await message.channel.send("Rock HaHa EZ 😂😂😂")
  elif message.content.startswith("$$ play Rock Paper Scissors with me"):
    await message.channel.send("ok i'll beat you ofc 😏")
  elif  "love you" in message.content.lower() and message.content.startswith("$$"):
    await message.channel.send("i'm married sorry here is my wife 👩‍🦰 she is a pretty bot")
    await message.channel.send("goodbye babe take care ...💃")
    await message.channel.send("pssst ... you still here , she is gone , whats your name again ?")
  elif message.content.startswith("$$ tell me a joke"):
    await message.channel.send("here is a random joke")
    await randomJoke(message)
  
  elif message.content.startswith("$$ hello"):
    await message.channel.send("Hello, it's me I was wondering if after all these years you'd like to meet To go over everything They say that time's supposed to heal ya But I ain't done much healing")
  elif message.content.startswith("$$ meme")or message.content.startswith("$$ setupS7or")  or message.content.startswith("$$ stop") or message.content.startswith("$$ wow") or message.content.startswith("$$ play") or message.content.startswith("$$ cursedimages"):
    return
  elif message.content.startswith("$$ mute") : 
    message_content = message.content
    user_id = message_content.replace("$$ mute <@!", "")
    user_id = user_id.replace(">", "")
    member = await message.guild.fetch_member(user_id)
    await message.channel.send(member.name + " has been server muted")
    await member.edit(mute = True) 
  elif message.content.startswith("$$ unmute") : 
    message_content = message.content
    user_id = message_content.replace("$$ unmute <@!", "")
    user_id = user_id.replace(">", "")
    member = await message.guild.fetch_member(user_id)
    await message.channel.send(member.name + " has been server unmuted")
    await member.edit(mute = False)
  elif message.content.startswith("$$ deafen") : 
    message_content = message.content
    user_id = message_content.replace("$$ deafen <@!", "")
    user_id = user_id.replace(">", "")
    member = await message.guild.fetch_member(user_id)
    await message.channel.send(member.name + " has been server deafened")
    await member.edit(deafen = True) 
  elif message.content.startswith("$$ undeafen") : 
    message_content = message.content
    user_id = message_content.replace("$$ undeafen <@!", "")
    user_id = user_id.replace(">", "")
    member = await message.guild.fetch_member(user_id)
    await message.channel.send(member.name + " has been server undeafened")
    await member.edit(deafen = False) 
  elif message.content.startswith("$$ dm") : 
    message_content = message.content
    user_id = message_content.replace("$$ dm <@!", "")
    user_id = user_id.replace(">", "")
    member = await message.guild.fetch_member(user_id)
    await message.channel.send(member.name + " has been server deafened and muted")
    await member.edit(deafen = True) 
    await member.edit(mute = True) 
  elif message.content.startswith("$$ undm") : 
    message_content = message.content
    user_id = message_content.replace("$$ undm <@!", "")
    user_id = user_id.replace(">", "")
    member = await message.guild.fetch_member(user_id)
    await message.channel.send(member.name + " has been server undeafened and unmuted")
    await member.edit(deafen = False) 
    await member.edit(mute = False) 
  elif message.content.startswith("$$"):
    await message.channel.send("7ata botet ma yerte7och fi hal bled chno t7eb ... a3mel $$ help ken ma ta3refch")
  

@client.command()
async def meme(ctx):
  subbreddit = reddit.subreddit("HolUp")
  top = subbreddit.top(limit=50)
  all_subs = []
  for submition in top:
    all_subs.append(submition)
    
  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url

  em = discord.Embed(title=name)
  em.set_image(url=url)
  await ctx.send(embed = em)


@client.command()
async def wow(ctx):
  subbreddit = reddit.subreddit("nextfuckinglevel")
  top = subbreddit.top(limit=50)
  all_subs = []
  for submition in top:
    all_subs.append(submition)
    
  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url

  em = discord.Embed(title=name)
  em.set_image(url=url)
  await ctx.send(embed = em)

@client.command()
async def cursedimages(ctx):
  subbreddit = reddit.subreddit("cursedimages")
  top = subbreddit.top(limit=50)
  all_subs = []
  for submition in top:
    all_subs.append(submition)
    
  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url

  em = discord.Embed(title=name)
  em.set_image(url=url)
  await ctx.send(embed = em)

  
async def randomJoke(message):
  if random.randint(0,1)==1 :
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        'x-rapidapi-key': "e62b5c960cmshe37db75b3e3b4c9p10e7cajsn2f65750f4783",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    jsonData = json.loads(response.text)
    await message.channel.send(jsonData["body"][0]["setup"])
    await message.channel.send(jsonData["body"][0]["punchline"])
  else:
    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-key': "e62b5c960cmshe37db75b3e3b4c9p10e7cajsn2f65750f4783",
        'x-rapidapi-host': "joke3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    d = json.loads(response.text)
    await message.channel.send(d["content"])
  
@client.command()
async def play(ctx,url,channelFromShour = None):
  # url = titleToUrl(url)
  # await ctx.send(url)
  if ctx.voice_client is None:
        if ctx.author.voice:
            pass
        else:
            await ctx.send("You are not connected to a voice channel.")
            return
  
  channel = ctx.author.voice.channel
  try:
    await channel.connect()
  except:
    pass
  async with ctx.typing():
    player = await YTDLSource.from_url(url, loop=False)
    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

  await ctx.send('Now playing: {}'.format(player.title))


@client.command()
async def stop( ctx):
  await ctx.voice_client.disconnect()
  await ctx.send(" n8anilhom w ytardoni..  😑")

@client.command()
async def yahya(ctx):
  channel = discord.utils.get(ctx.guild.channels, name='💻___Coding Ⅰ ___💻')
  await channel.connect()
  url = 'https://www.youtube.com/watch?v=WwYOAhw12WM'
  async with ctx.typing():
    player = await YTDLSource.from_url(url, loop=False)
    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

@client.command()
async def test(ctx):
  print(ctx)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)





async def komoTsa7aro(ctx):
  now = datetime.now().strftime("%H%M")
  print(int(now)+100)
  try:
    Timer(5.0, komoTsa7aro(ctx)).start()
    channel = discord.utils.get(ctx.guild.channels, name='💻___Coding Ⅰ ___💻')
    if(int(now)+100 > 200 ):
      await play(ctx,'https://www.youtube.com/watch?v=xB8KucG0Clw',channel)
      #await ctx.send(" 9omo tsa7aro ")
  except:
    print("waiting for setup")

komoTsa7aro(None)

keepAlive()
client.run("ODEwODYwMjE1NzY3MjY5NDM2.YCpybA.HpfTO6wYAdITyBDhkOi-rQLWprk")
