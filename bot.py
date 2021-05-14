import discord
import cwral

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("상태메시지")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!과제"):
        await message.channel.send("\'!로그인 id pw\'를 입력")
    if message.content.startswith("!로그인"):
        input = list(message.content.split())
        try:
            await message.channel.send("과제 정보를 가져오는 중.........")
            a,b = cwral.getMyAssignment(input[1],input[2])
            for i in b: 
                await message.channel.send(i+' : '+b[i])
        except:
            await message.channel.send("잘못된 정보를 입력하거나 알 수 없는 오류가 발생함!")


client.run('여기에 토큰 넣기')
