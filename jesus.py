import discord
from discord.ext import commands
import random
client = discord.Client()
bot = commands.Bot(command_prefix='!')

def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      pos = buf.index(newline)
      yield buf[:pos]
      buf = buf[pos + len(newline):]
    chunk = f.read(4096)
    if not chunk:
      yield buf
      break
    buf += chunk

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def bothelp(ctx):
    embed = discord.Embed(name="help")
    embed.set_author(name="Jesus Bot commands:")
    embed.add_field(name="To generate random verse:", value="!verse", inline=False)
    # embed.add_field(name="To generate random quote", value="!quote", inline=False)
    await bot.say(embed=embed)

@bot.command(name='verse', help='selects random verse')
async def verse(ctx):
    verses = {}
    with open('100+verses.txt', 'r') as myfile:
        for myline in myreadlines(myfile, '`'):
            # verses.append(myline)
            x = myline.split('\n')
            y = []
            for line in x:
              if line != "":
                y.append(line)
            verses.update({y[0]: y[1]})
    # with open('100+verses.txt', newline = '') as lines:                                                                                          
    #     verse_reader = csv.reader(lines, delimiter='`')
    #     for verse in verse_reader:
    #         verses.append(verse)

    choice = random.choice(list(verses))
    emb = discord.Embed(title=choice,description=verses[choice],color=discord.Colour.magenta())
    await ctx.send(embed=emb)

@bot.command(name='quote', help='random jesus quote')
async def quote(ctx):
  quotes = []
  with open('quotes.txt', 'r') as myfile:
    for myline in myreadlines(myfile, '\n'):
      quotes.append(myline)
  choice = random.choice(quotes)
  emb = discord.Embed(description=choice, color=discord.Colour.dark_gold())
  await ctx.send(embed=emb)

bot.run('token')