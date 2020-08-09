import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import random
import os
import time as UTC_Clock

Client=discord.Client()
client=commands.Bot(command_prefix="")

schoolList=['636613236006977537', '636620729739247626', '636613518547746826', '636613786039615508', '645663292932620298', 
            '636613625645367296', '636614053657182209', '636613983775883273', '636614382985543690', '636619867973222420', 
            '636614460253143050', '636621073378443264', '671756568349376512', '650491947089395732', '694013006551711796',
            '636620408346640401', '636620956345040916', '636620598226845696', '636620831589531649',  
            '670769209239797760',
            '636614782874681384', '689191748186275897', '702946421275361320', '714218854196445235', 
            '636624688520364066']
iconList=['<:selection:648231960556208138>', '<:anzio:648231934979211287>', '<:bc:648231960547688448>', 
          '<:bellwall:648231935394447379>', '<:bd:648231941128192001>', '<:bonple:648231951999959053>', 
          '<:chihatan:648231956009713674>', '<:count:648231941606342667>', '<:gregor:648231962183467008>', 
          '<:jatkosota:648231944902934534>', '<:koala_forest:648231952716922890>', '<:kuro:648231939630825483>', 
          '<:maginot:648231945125232690>', '<:maple:648231949512736793>', '<:neutrality:648517490099355648>',
          '<:ooarai:648231941992218624>', '<:pravda:648231939857448990>', '<:saunders:648231943934312488>', 
          '<:stg:648231944160673823>', '<:tatenashi:648231951467282432>',
          '<:viggen:648231943103578112>', '<:viking:648233133967147026>', '<:waffle:648231946845028365>', 
          '<:wkga:648233132977553409>', '<:yogurt:648231951781724171>']
#SWList=['653167395833249792', '653167938655748106', '653168305011425280', '653168628216102912', '653706748766715925', 
        #'653706973669490702']

@client.event
async def on_ready():
    print("Hello World!")

@client.event
async def on_member_update(before, after):
    if before.roles!=after.roles:
        fullList=[]
        text="Senshado School Member Count:```"
        for i in range(len(schoolList)):
            role = before.guild.get_role(int(schoolList[i]))
            icon = iconList[i]
            sum = len(role.members)
            text += role.name
            for j in range(len(role.name),34):
                text += " "
            if sum < 10:
                text += " "
            text += str(sum) + " members\n\n"
            if sum >= 30:
                fullList.append([role.name,icon])
        text += "```\n"
        for i in fullList:
            text += i[0] + " is full " + i[1] + "\n"
        #text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
        #yield from client.send_message(message.channel,text)
        
        
        msg = await client.get_channel(636669547667128337).fetch_message(659618792912977944)
        await msg.edit(content=text)
            
        #########################################

        #fullList=[]
        text=""
        #text="Strike Witches Squadron Member Count:```"
        #for i in range(len(SWList)):
            #role = before.guild.get_role(int(SWList[i]))
            #sum = len(role.members)
            #text += role.name
            #for j in range(len(role.name),34):
                #text += " "
            #if sum < 10:
                #text += " "
            #text += str(sum) + " members\n\n"
            #if sum >= 30:
                #fullList.append(role.name)
        #text += "```\n"
        #for i in fullList:
            #text += i + " is full\n"
        text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
        #yield from client.send_message(message.channel,text)
        
        
        msg = await client.get_channel(636669547667128337).fetch_message(659623723921440779)
        await msg.edit(content=text)

@client.event
async def on_member_remove(member):
    fullList=[]
    text="Senshado School Member Count:```"
    for i in range(len(schoolList)):
        role = before.guild.get_role(int(schoolList[i]))
        icon = iconList[i]
        sum = len(role.members)
        text += role.name
        for j in range(len(role.name),34):
            text += " "
        if sum < 10:
            text += " "
        text += str(sum) + " members\n\n"
        if sum >= 30:
            fullList.append([role.name,icon])
    text += "```\n"
    for i in fullList:
        text += i[0] + " is full " + i[1] + "\n"
    #text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
    #yield from client.send_message(message.channel,text)
        
        
    msg = await client.get_channel(636669547667128337).fetch_message(659618792912977944)
    await msg.edit(content=text)
            
    #########################################

    #fullList=[]
    text=""
    #text="Strike Witches Squadron Member Count:```"
    #for i in range(len(SWList)):
        #role = before.guild.get_role(int(SWList[i]))
        #sum = len(role.members)
        #text += role.name
        #for j in range(len(role.name),34):
            #text += " "
        #if sum < 10:
            #text += " "
        #text += str(sum) + " members\n\n"
        #if sum >= 30:
            #fullList.append(role.name)
    #text += "```\n"
    #for i in fullList:
        #text += i + " is full\n"
    text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
    #yield from client.send_message(message.channel,text)
        
        
    msg = await client.get_channel(636669547667128337).fetch_message(659623723921440779)
    await msg.edit(content=text)


@client.event
async def on_message(message):
                    
    if message.channel.id==636653692841623612:
        if message.content.startswith("-botstatus"):
            print("yes")
            await message.channel.send("I'm working well here!")
        if message.content.startswith("-iconcheck"):
            for i in range(len(schoolList)):
                role = message.guild.get_role(int(schoolList[i]))
                icon = iconList[i]
                await message.channel.send(role.name + " " + icon)
        if message.content.startswith("-currenttime"):
            await message.channel.send(UTC_Clock.asctime(UTC_Clock.gmtime()))
        if message.content.startswith("thisIsAnUpdate"):
            fullList=[]
            text="Senshado School Member Count:```"
            for i in range(len(schoolList)):
                role = message.guild.get_role(int(schoolList[i]))
                icon = iconList[i]
                sum = len(role.members)
                text += role.name
                for j in range(len(role.name),34):
                    text += " "
                if sum < 10:
                    text += " "
                text += str(sum) + " members\n\n"
                if sum >= 30:
                    fullList.append([role.name,icon])
            text += "```\n"
            for i in fullList:
                text += i[0] + " is full " + i[1] + "\n"
            #text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
            #await client.get_channel(636669547667128337).send(text)
            
            
            msg = await client.get_channel(636669547667128337).fetch_message(659618792912977944)
            await msg.edit(content=text)
            #yield from client.delete_message(message)
            
            ##################################################
            
            #fullList=[]
            text=""
            #text="Strike Witches Squadron Member Count:```"
            #for i in range(len(SWList)):
                #role = message.guild.get_role(int(SWList[i]))
                #sum = len(role.members)
                #text += role.name
                #for j in range(len(role.name),34):
                    #text += " "
                #if sum < 10:
                    #text += " "
                #text += str(sum) + " members\n\n"
                #if sum >= 30:
                    #fullList.append(role.name)
            #text += "```\n"
            #for i in fullList:
                #text += i + " is full\n"
            text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
            #await client.get_channel(636669547667128337).send(text)
            
            
            msg = await client.get_channel(636669547667128337).fetch_message(659623723921440779)
            await msg.edit(content=text)
            await message.delete()
            

access_token= os.environ["ACCESS_TOKEN"]
client.run(access_token)
