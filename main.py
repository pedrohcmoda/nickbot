# This example requires the 'message_content' privileged intents

import asyncio
import os
import discord
from discord.ext import commands



bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_member_join(member):
    await member.create_dm()
    print("Hello, {member.id}")
    await member.dm_channel.send(f'Olá {member.name}, bem vindo ao server, manda teu nick ai kk!')
    try:
        nickname = await bot.wait_for('message', check=lambda message: message.author == member and message.channel == member.dm_channel, timeout=60)
    except asyncio.TimeoutError:
        await member.dm_channel.send(f'Você não respondeu a tempo. Tente novamente mais tarde.')
    else:
        await member.edit(nick=nickname.content)
        
bot.event(on_member_join)

bot.run(os.environ["DISCORD_TOKEN"])
