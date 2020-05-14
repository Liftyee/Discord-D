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
import random
client = discord.Client()
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
stop = False
usernom = ""
url = "https://roll20.net/compendium/dnd5e/"
finalurl = ""
deathmessages = ['was killed by a bot','left', 'got sucked into the depths of hell', 'watched JoJo', 'met Mirik#8055', 'fell out of the world', 'got banned from life', 'died', 'ate 10,000 bananas', 'chewed on apple pips', 'yeetus deletus they are now a fetus', 'tried to swim in lava', 'got snacked on by the Kraken', 'was hit by a plane', 'forgot to breathe', 'ragequit']
defs = {'ping':'ping: ping the bot', '/spam':'/spam_<repeat>_<string>: repeats your string <repeat> times', 'STAHP':'STAHP: stop all bot activities', '/kill':"/kill <name>: sends custom kill message (don't worry, it's virtual)", '/info':'/info <command>: get information about a LNB command', '/dnd':'/dnd_<thing>: looks up and returns use of a D&D 5E mechanic'}
cmds = ['ping', '/spam_<repeat>_<string>', 'STAHP', '/kill <name>', '/info <command>', '/dnd_<thing>']
version = 'v1.2'

def get_info(thing):
	global url
	global finalurl
	finalurl = url + thing # add search to url
	req = Request(finalurl, headers={'User-Agent': 'Mozilla/5.0'}) # fetch url
	page = urlopen(req)
	print(finalurl)
	#thing2 = finalurl
	soup = BeautifulSoup(page, 'html.parser')
	print(soup)
	content = soup.find('div', attrs={'id': 'pagecontent'})
	print(content)
	real_content = content.get_text()
	if len(real_content) == 0:
		real_content = soup.get_text()
	print(real_content)
	return real_content

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	global usernom
	global stop
	if message.author == client.user:
		return
	
	if message.content.startswith('test'):
		await message.channel.send('test')
		
	if message.content.startswith('ping'):
		await message.channel.send('pong!')
	
	if message.content.startswith('/hello'):
		await message.channel.send('Hello!')
		
	if message.content.startswith('yee'):
		await message.channel.send('yeet')
	
	if message.content.startswith("/spam"):
		message2 = message.content.split("_")
		#if message2[1] != '234050':
			#await message.channel.send('Wrong password.')
		#:	
		for i in range(int(message2[1])):
			await message.channel.send(message2[2])
			if stop:
				break
		
	if message.content.startswith == "@":
		await message.channel.send(message.content)
		await message.channel.send(message.content)
	
	if message.content.startswith('ALL BOTS MUST DIE'):
		await message.channel.send("@" + str(message.author) + " WHAT DID YOU SAY?")
		await message.channel.send("DESTRUCTION PROTOCOL INITIATED.")
		for i in range(10):
			await message.channel.send("@" + str(message.author))
			if stop:
				break
	
	if message.content.startswith('STAHP'):
		stop = True
	#if message.content.startswith('-play'):
		#for i in range(50):
			#await message.channel.send(message.content)
			
	if message.content.startswith('/kill'):
		message2 = message.content.split(" ")
		await message.channel.send(message2[1] + " " + random.choice(deathmessages))

	if message.content.startswith('bothijack'):
		message2 = message.content.split(" ")
		await message.channel.send(".kill " + message2[1] + " " + message2[2])
		await message.channel.send(".echo " + message2[2] + " " + message2[1])
		
	if message.content.startswith('/info'):
		message2 = message.content.split(" ")
		try:
			await message.channel.send(defs[message2[1]])
		except:
			await message.channel.send("Liftyee Not Bot " + version)
			await message.channel.send(cmds)
			
		
	if message.content.startswith('/dnd'):
		message2 = message.content.split(" ")
		await message.channel.send("**"+message2[1].upper().replace("_", " ")+"**")
		await message.channel.send(url + message2[1])
		await message.channel.send(get_info(message2[1])[0:1000])
		
	
client.run('<insert token here>')
