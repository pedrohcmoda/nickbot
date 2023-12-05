# This example requires the 'message_content' privileged intents

import discord
import os
import asyncio

client = discord.Bot(intents=discord.Intents.all())


@client.event
async def on_member_join(member):
    await member.create_dm()
    print("Hello, {member.id}")
    await member.dm_channel.send(f'Olá {member.name}, bem vindo ao server, manda teu nick ai kk!')
    try:
        nickname = await client.wait_for('message', check=lambda message: message.author == member and message.channel == member.dm_channel, timeout=60)
    except asyncio.TimeoutError:
        await member.dm_channel.send(f'Você não respondeu a tempo. Tente novamente mais tarde.')
    else:
        await member.edit(nick=nickname.content)
        
client.event(on_member_join)


client.run(os.environ["DISCORD_TOKEN"])
