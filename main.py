# This example requires the 'message_content' privileged intents

import asyncio
import discord

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_member_join(member):
  await member.create_dm()
  print("Hello, {member.id}")
  await member.dm_channel.send(
      f'Olá {member.name}, bem vindo ao KOC, manda seu nick ingame ai')
  try:
    nickname = await bot.wait_for(
        'message',
        check=lambda message: message.author == member and message.channel ==
        member.dm_channel,
        timeout=60)
  except asyncio.TimeoutError:
    await member.dm_channel.send(
        f'Você não respondeu a tempo, assim que possivel altere manualmente seu apelido no servidor, seu apelido precisa ser seu nick ingame'
    )
  else:
    await member.edit(nick=nickname.content)


bot.event(on_member_join)

bot.run("MTE4MTU5NjU3MTM4MTU1MTEzNQ.G5yUgK.AhKNJyg6HxQZ0ZtAI8F54oEkSgiElMkVrFpQCU")
