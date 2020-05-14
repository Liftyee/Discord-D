#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  discord bot.py
#  
#  Copyright 2020 Victor <victor@victor-linux>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import discord
from random import randint
import time
echo = []
ignore = []
mute = False
stahp = False
echoNum = 0
urself = False
remember = ""
AtTag = {"<@!710197292677726239>": "Spamri123#2899"}
#enter here @ and user names of people in server

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global echo
    global echoNum
    global remember
    global mute
    global ignore
    global stahp
    global urself
    if not mute:
        if message.author == client.user and not urself:
            return

        stop = False
        for person in ignore:
            if str(person) == str(message.author):
                stop = True
                break

        try:
            if message.content[0] == "." and not stop:
                a = message.content.split()

                if message.content.startswith(".kill"):
                    for x in range(0, int(a[1])):
                        time.sleep(0.1)
                        if stahp:
                            return
                        await message.channel.send(message.content[6+len(a[1]):len(message.content)])

                if message.content.startswith(".continue"):
                    stahp = False

                elif message.content.startswith(".stop"):
                    echo = []
                    ignore = []
                    stahp = True

                elif message.content.startswith(".urself"):
                    if urself:
                        urself = False
                        await message.channel.send("Off")
                    else:
                        urself = True
                        await message.channel.send("On")

                elif message.content.startswith(".echo"):
                    if a[1] == "add":
                        echo.append((AtTag[a[3]], int(a[2])))
                        print("added")
                    elif a[1] == "remove":
                        echo.remove((AtTag[a[3]], int(a[2])))
                    elif a[1] == "bot":
                        echo.append((message.content[11+int(len(a[2])):len(message.content)], int(a[2])))

                elif message.content.startswith(".roll"):
                    total = 0
                    for x in range(0, int(a[1])):
                        total += randint(1, int(a[2]))
                    await message.channel.send(str(total + a[3]))

                elif message.content.startswith(".mute"):
                    mute = True
                    await message.channel.send("Muted")

                elif message.content.startswith(".ignore"):
                    if a[1] == "add":
                        ignore.append(AtTag[message.content[12:1000]])
                    elif a[1] == "remove":
                        ignore.remove(AtTag[message.content[15:1000]])

                elif message.content.startswith(".info"):
                    await message.channel.send(".kill (number) (word to repeat) \n \
    spams a message a number of times \n \
    .stop \n \
    clears ignores and echos \n \
    .roll (number) (number of sides) (modifier) \n \
    rolls a number of die and gives you the output plus a modifier \n \
    .mute \n \
    mutes the bot and doesn't answer any commands apart from .unmute \n \
    .unmute \n \
    unmutes the bot \n \
    .ignore (add or remove) (player @ tag) \n \
    makes the bot ignores someones commands \n \
    echo (add or remove) (number) (player @ tag) \n \
    will echo someone a number of times")

                elif message.content.startswith(".code"):
                    await message.channel.send("code can be accessed at \nhttps://github.com/Liftyee/Discord-D/blob/master/discord%20bot%20notoken.py")

        except IndexError:
            pass

        for echos in echo:
            print(echos[0])
            if str(message.author) == str(echos[0]):
                for x in range(0, int(echos[1])):
                    time.sleep(0.2)
                    if stahp:
                        return
                    await message.channel.send(message.content)

    elif message.content.startswith(".unmute"):
        mute = False
        await message.channel.send("unmuted")


client.run('<enter token here>')
