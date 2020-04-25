import random
import os

import discord
from dotenv import load_dotenv


client = discord.Client()

load_dotenv()

prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="discord.py"))
    print(f'[{client.user}] has connected to Discord!')
    print(f'[{client.user}] Data Loading 5%')
    print(f'[{client.user}] Data Loading 20%')
    print(f'[{client.user}] Data Loading 40%')
    print(f'[{client.user}] Data Loading 55%')
    print(f'[{client.user}] Data Loading 75%')
    print(f'[{client.user}] Data Loading 85%')
    print(f'[{client.user}] Data Loading 100%')
    print(f'[{client.user}] Data suceffueled Loading')


@client.event
async def on_member_join(member):
    await member.create_dm()
    nubmer = random.randint(1, 100)
    if(nubmer == 5):
        member.dm_channel.send(
            f'Hi {member.name}, welcome to **Thumbie.py** Discord server! I hope you will like it here and you will learn to work in python if you don\'t know yet :D \nYou won the VIP rank on our Discord')

    else:
        member.dm_channel.send(
            f'Hi {member.name}, welcome to **Thumbie.py** Discord server! I hope you will like it here and you will learn to work in python if you don\'t know yet :D \nYou didn\'t win the VIP rank on our discord :( You\'re unlucky')


@client.event
async def on_message(message, *args):
    if(message.content == f"{prefix}help"):
        embed = discord.Embed(title="Help menu", color=discord.Colour(0xff3f))
        embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104", icon_url="https://lh3.googleusercontent.com/proxy/LhzZmn1eQNTDYVZsuhOUikt-bxsm9uOXOEMPICRU1eJIogAi6AjyIZRNPV7RZnAPD-f6WjQF0bLGWet_NqyAUXUpOmt5_bz5vZwUHZVvA_vl1s0scMOx28nmdkdJrcU8tzb3ODATg42aDrd317iH_A")
        embed.add_field(name=f"**Commands**", value=f"**{prefix}loteria** It gives you a chance to win the lottery\n**{prefix}git** Sends you the Pymbie source code\n**{prefix}py **help with Python")
        await message.channel.send(embed=embed)

    if(message.content == f"{prefix}git"):
        embed = discord.Embed(title="My Source code", color=discord.Colour(0xff3f), description=f"**[Click me](https://github.com/Vladimir-Urik/Learning-Python)**")
        embed.set_footer(text="© GitHub 2020", icon_url="https://www.pngitem.com/pimgs/m/128-1280162_github-logo-png-cat-transparent-png.png")
        await message.channel.send(embed=embed)


    if(message.content == (f'{prefix}py')):
        embed = discord.Embed(title="Python", color=discord.Colour(0xff3f), description=f"**Use:** ```+py <args>```")
        embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104", icon_url="https://lh3.googleusercontent.com/proxy/LhzZmn1eQNTDYVZsuhOUikt-bxsm9uOXOEMPICRU1eJIogAi6AjyIZRNPV7RZnAPD-f6WjQF0bLGWet_NqyAUXUpOmt5_bz5vZwUHZVvA_vl1s0scMOx28nmdkdJrcU8tzb3ODATg42aDrd317iH_A")
        await message.channel.send(embed=embed)

    if(message.content == (f"{prefix}py discord.py")):
        embed = discord.Embed(title="Python Discord.js", color=discord.Colour(0xff3f),
                              description=f"**Use:** ```+py discord.py <install|command>```")
        embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104",
                         icon_url="https://lh3.googleusercontent.com/proxy/LhzZmn1eQNTDYVZsuhOUikt-bxsm9uOXOEMPICRU1eJIogAi6AjyIZRNPV7RZnAPD-f6WjQF0bLGWet_NqyAUXUpOmt5_bz5vZwUHZVvA_vl1s0scMOx28nmdkdJrcU8tzb3ODATg42aDrd317iH_A")
        await message.channel.send(embed=embed)

    if(message.content == (f"{prefix}py discord.py install")):
        embed = discord.Embed(title="Python Discord.js install", color=discord.Colour(0xff3f))
        embed.add_field(name=f"Steps:", value=f"**1.step Create a new project in PyCharm**\n**2.step Install depencies with commands in Terminal:**\n```py -3 -m pip install -U discord.py```\n```py -3 -m pip install -U python-dotenv```\n**3.step Create python file bot.py**\n**4.step A place this code to bot.py**\n```py\nimport discord\nimport os\nfrom dotenv import load_dotenv\n \nclient = discord.Client()\nload_dotenv()\n \nprefix = \"prefix for your bot\"\n```\nnext page: `+py discord.py install 2`", inline=False)

        embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104",
                         icon_url="https://lh3.googleusercontent.com/proxy/LhzZmn1eQNTDYVZsuhOUikt-bxsm9uOXOEMPICRU1eJIogAi6AjyIZRNPV7RZnAPD-f6WjQF0bLGWet_NqyAUXUpOmt5_bz5vZwUHZVvA_vl1s0scMOx28nmdkdJrcU8tzb3ODATg42aDrd317iH_A")
        await message.channel.send(embed=embed)

    if(message.content == (f"{prefix}py discord.py install 1")):
        embed = discord.Embed(title="Python Discord.js install", color=discord.Colour(0xff3f))
        embed.add_field(name=f"Steps:", value=f"**1.step Create a new project in PyCharm**\n**2.step Install depencies with commands in Terminal:**\n```py -3 -m pip install -U discord.py```\n```py -3 -m pip install -U python-dotenv```\n**3.step Create python file bot.py**\n**4.step A place this code to bot.py**\n```py\nimport discord\nimport os\nfrom dotenv import load_dotenv\n \nclient = discord.Client()\nload_dotenv()\n \nprefix = \"prefix for your bot\"\n```\nnext page: `+py discord.py install 2`", inline=False)

        embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104",
                         icon_url="https://lh3.googleusercontent.com/proxy/LhzZmn1eQNTDYVZsuhOUikt-bxsm9uOXOEMPICRU1eJIogAi6AjyIZRNPV7RZnAPD-f6WjQF0bLGWet_NqyAUXUpOmt5_bz5vZwUHZVvA_vl1s0scMOx28nmdkdJrcU8tzb3ODATg42aDrd317iH_A")
        await message.channel.send(embed=embed)

    if(message.content.startswith(f'{prefix}loteria')):
        if(len(args) == 0):
            int = random.randint(1, 20);
            if(int == 4):
                ciselko = random.randint(1, 10000);
                embed = discord.Embed(title="You Win!!!", color=discord.Colour(0xff3f), description="Congratulations on winning")
                embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104", icon_url="https://lh3.googleusercontent.com/proxy/LhzZmn1eQNTDYVZsuhOUikt-bxsm9uOXOEMPICRU1eJIogAi6AjyIZRNPV7RZnAPD-f6WjQF0bLGWet_NqyAUXUpOmt5_bz5vZwUHZVvA_vl1s0scMOx28nmdkdJrcU8tzb3ODATg42aDrd317iH_A")
                embed.set_image(url="https://media.discordapp.net/attachments/660104128193888257/703518429990223932/you-lose-clipart-6.png?width=656&height=641")
                embed.add_field(name=f"You win a", value=f"{ciselko} :dollar: ")
                await message.channel.send(embed=embed)
            else:
                ciselko = random.randint(1, 10000);
                embed = discord.Embed(title="Oh, you're unlucky!", color=discord.Colour(0xff0003))
                embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104", icon_url="https://lh3.googleusercontent.com/proxy/LhzZmn1eQNTDYVZsuhOUikt-bxsm9uOXOEMPICRU1eJIogAi6AjyIZRNPV7RZnAPD-f6WjQF0bLGWet_NqyAUXUpOmt5_bz5vZwUHZVvA_vl1s0scMOx28nmdkdJrcU8tzb3ODATg42aDrd317iH_A")
                embed.set_image(url="https://media.discordapp.net/attachments/660104128193888257/703517390293434388/you-lose-clipart-6.png?width=656&height=641")
                embed.add_field(name="Your number:", value=f"{int}")
                embed.add_field(name=f"You just ran out of sight:", value=f"{ciselko} :dollar: ")
                embed.add_field(name="Winning number:", value="4")
                await message.channel.send(embed=embed)
        else:
            await message.channel.send("Wole tebe hrabe? 😲")

client.run(token)