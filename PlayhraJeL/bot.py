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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="na mc.ProjectE.eu"))
    print(f'[{client.user}] has connected to Discord!')
    print(f'[{client.user}] Data Loading 5%')
    print(f'[{client.user}] Data Loading 20%')
    print(f'[{client.user}] Data Loading 40%')
    print(f'[{client.user}] Data Loading 55%')
    print(f'[{client.user}] Data Loading 75%')
    print(f'[{client.user}] Data Loading 85%')
    print(f'[{client.user}] Data Loading 100%')
    print(f'[{client.user}] Data suceffueled Loading')

    # @client.event
    # async def on_member_join(member):
    # await member.create_dm()
    # nubmer = random.randint(1, 100)
    # if(nubmer == 5):
    #    member.dm_channel.send(
    #        f'Hi {member.name}, welcome to **Thumbie.py** Discord server! I hope you will like it here and you will learn to work in python if you don\'t know yet :D \nYou won the VIP rank on our Discord')
    #
    #    else:
    #       member.dm_channel.send(
    #          f'Hi {member.name}, welcome to **Thumbie.py** Discord server! I hope you will like it here and you will learn ň

@client.event
async def on_message(message, *args):
    if(message.content == f"{prefix}help"):
        embed = discord.Embed(title="Pomoc", color=discord.Colour(0xb400ff))
        embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104",
                         icon_url="https://cdn.discordapp.com/avatars/535708984959827978/3abf6879d0561fe8580bc2eac5d5e76c.webp")
        embed.add_field(name=f"**Príkazy**",
                        value=f"**{prefix}loteria** Chceš zariskovať? V tom prípade je lotéria pre teba\n**{prefix}git** ukáže ty zdrojový kód tohto bota")
        await message.channel.send(embed=embed)

    if (message.content.startswith(f'{prefix}nabor')):
        embed = discord.Embed(title=f"Vyber si pozici", color=discord.Colour(0xff3f),
                              description="```,nabor <pozice>```\nKategórie: ```helper, builder```")
        embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104",
                         icon_url="https://cdn.discordapp.com/avatars/535708984959827978/3abf6879d0561fe8580bc2eac5d5e76c.webp")
        await message.channel.send(embed=embed)


    if (message.content.startswith(f'{prefix}loteria')):
        if (len(args) == 0):
            int = random.randint(1, 20);
            if (int == 4):
                ciselko = random.randint(1, 10000);
                embed = discord.Embed(title=f"({message.author})You Win!!!", color=discord.Colour(0xff3f),
                                      description="Congratulations on winning")
                embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104",
                                 icon_url="https://cdn.discordapp.com/avatars/535708984959827978/3abf6879d0561fe8580bc2eac5d5e76c.webp")
                embed.set_image(
                    url="https://media.discordapp.net/attachments/660104128193888257/703518429990223932/you-lose-clipart-6.png?width=656&height=641")
                embed.add_field(name=f"You win a", value=f"{ciselko} :dollar: ")
                await message.channel.send(embed=embed)
            else:
                ciselko = random.randint(1, 10000);
                embed = discord.Embed(title="Oh, you're unlucky!", color=discord.Colour(0xff0003))
                embed.set_footer(text="By 𝗚𝗚𝗚𝗘𝗗𝗥#6104",
                                 icon_url="https://cdn.discordapp.com/avatars/535708984959827978/3abf6879d0561fe8580bc2eac5d5e76c.webp")
                embed.set_image(
                    url="https://media.discordapp.net/attachments/660104128193888257/703517390293434388/you-lose-clipart-6.png?width=656&height=641")
                embed.add_field(name="Your number:", value=f"{int}")
                embed.add_field(name=f"You just ran out of sight:", value=f"{ciselko} :dollar: ")
                embed.add_field(name="Winning number:", value="4")
                await message.channel.send(embed=embed)
        else:
            await message.channel.send("Wole tebe hrabe? 😲")

client.run(token)