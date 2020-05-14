import discord
from random import randint
echo = []
ignore = []
mute = False
echoNum = 0
remember = ""
file = open("code.txt", "r")
AtTag = {"@Liftyee": "Liftyee#6981", "@織田 信長": "ç¹”ç”° ä¿¡é•·#0927", "@amri123": "amri123#5069", "@Spamri123": "Spamri123#2899", "@D17381": "D17381#0757", "@Nawdy": "Nawdy#2021", "@Liftyee Not Bot": "Liftyee Not Bot#6729"}
board =[["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

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
    if not mute:
        if message.author == client.user:
            return

        stop = False
        for person in ignore:
            if str(person) == str(message.author):
                stop = True
                break

        if message.content[0] == "." and not stop:
            a = message.content.split()

            if message.content.startswith(".kill"):
                for x in range(0, int(a[1])):
                    await message.channel.send(a[2])

            elif message.content.startswith(".stop"):
                echo = []
                ignore = []

            elif message.content.startswith(".echo"):
                if a[1] == "add":
                    echo.append((AtTag[a[3]], int(a[2])))
                    print("added")
                elif a[1] == "remove":
                    echo.remove((AtTag[a[3]], int(a[2])))
elif message.content.startswith(".roll"):
                total = 0
                for x in range(0, int(a[1])):
                    total += randint(1, int(a[2]))
                await message.channel.send(str(total + a[3]))

            elif message.content.startswith(".mute"):
                mute = True

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
                content = file.read()
                await message.channel.send(str(content))

        for echos in echo:
            print(echos[0])
            if str(message.author) == str(echos[0]):
                for x in range(0, int(echos[1])):
                    await message.channel.send(message.content)

    elif message.content.startswith(".unmute"):
        mute = False


client.run('<insert token here>')
