import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("상태메시지")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")


client.run("ODI0MjQ3OTAyNzU4NjMzNTM1.YFsmrQ.PpfOdhe4c7_B1sF61FMM30SoPi0")