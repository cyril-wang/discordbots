import discord
import os
bot = discord.Client()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "joe" in message.content.lower():
        await message.channel.send('JOE MAMA!')

bot.run('OTk5MTgyMDg5NTcwMjQyNjIx.GucYuy.rkBU84up9YbeAZPDRdRtbdt8d5VRg4lGhxDZg8')




