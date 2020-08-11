import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import random
import re
import os
import time as UTC_Clock

Client=discord.Client()
client=commands.Bot(command_prefix="")

schoolList=['648538406556663850', '648536799093850114', '648535340574834710', '648539120033071104',
            '648537502059069452', '648535963097628672', '648538389385314304', '651130538047832072',
            '726113825241301053', '648538759742357523', '648537267765379083', '652141003670683649',
            '652159619304652821', '648535031232593950', '648539710653988884', '652141533230792705',
            '704753655332732990', '648536574652317736', '648537398271279107', '648535562587996161',
            '648535702216114176', '725961752000462878', '648538907239251990', '656525536432095264',
            '651723637228961793', '717895107335946271', '648539290988707860', '687634886978306058']
iconList=['<:Selection:648955411755565056>', '<:Anzio:648953971154747408>', '<:BC_Freedom:639854220274696193>',
          '<:Bellwall:648955590164480006>', '<:Blue_Division:648956039474970679>', '<:Bonple:648969722276085801>',
          '<:Chi_Ha:648955105588150272>', '<:CountHS:651130791576993794>', '<:Gilbert:726832154968850504>',
          '<:Gregor:648969383850541076>', '<:Jatkosota:639854905833816083>', '<:NewKebab:720090882707292160>',
          '<:KoalaHS:683327268218863654>', '<:KMM:639852209063985170>', '<:Maginot:648969406252318741>',
          '<:Maple:656523210812162090>', '<:Neutrality:727969236638498947>', '<:Ooarai:639851203269885953>',
          '<:Pravda:639851595512676352>', '<:Saunders:639852388466819107>', '<:STGGC:639850530981543966>',
          '<:Tategoto:741866608976330763>', '<:Tatenashi:683326430062313502>', '<:Viggen:656523291653308416>',
          '<:Viking:656524130727886858>', '<:Waffle:719592170109272067>', '<:NewWestK:720072480399556619>',
          '<:Yogurt:689588507168997400>', '<:OldWestK:694543043201859694>']

@client.event
async def on_ready():
    print("Hello World!")

@client.event
async def on_message(message):

    executed = False
                    
    if message.channel.id==663883554098249776:
        if message.content.startswith("&botstatus"):
            print("yes")
            await message.channel.send("I'm working well here!")
        if message.content.startswith("&iconcheck"):
            for i in range(len(schoolList)):
                role = message.guild.get_role(int(schoolList[i]))
                icon = iconList[i]
                await message.channel.send(role.name + " " + icon)
        if message.content.startswith("&currenttime"):
            await message.channel.send(UTC_Clock.asctime(UTC_Clock.gmtime()))
        if message.content.startswith("&test"):
            print(message.content)
            await message.add_reaction("✅")

    if message.channel.id==671039362602893331:
        if message.content.startswith("&member"):
            executed = True
            try:
                result = re.search("<(.*)>",message.content)
                result = '<'+result.group(1)+'>'
                school = iconList.index(result)
                if school == 28:
                    school = 26
                role = message.guild.get_role(int(schoolList[school]))
                await message.add_reaction("✅")
                await message.author.send("Members of "+role.name+":")
                for i in role.members:
                    text = i.name + " #" + i.discriminator
                    if i.nick != None:
                        text += " (" + i.nick+")"
                    await message.author.send(text)
                await message.author.send("A total of "+str(len(role.members))+" members")
            except:
                await message.channel.send("""Sorry, I couldn't understand that command.
Use &help for a full list of commands""")

    if message.content.startswith("&help"):
        executed = True
        await message.add_reaction("✅")
        await message.author.send("""Thank you for using Sensha-Dō Federation Bot

The current available commands are:

&member [Icon] - can only be used in #commanders-hall channel. Use the icon of a school to recieve a full list of its members.""")

    if ("522154037257175041" in message.content) and not(executed):
        await message.channel.send("Don't ping me Reeeee!\nUse \"&help\" for a full list of commands")            

access_token= os.environ["ACCESS_TOKEN"]
client.run(access_token)
