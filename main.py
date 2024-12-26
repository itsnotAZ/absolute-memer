# absolute memer bot by itsnotAZ source code

# IMPORTANT: The file "config" needs to be in the same directory as this script.

# api's used:
# - jokeapi.dev
# - opentdb.com
# - memegen.link
# - Meme_Api
# - discord.py (obviously)

# i'm not affiliated with the people behind the above software products and i do not own the rights to any of them either
# for licenses check the /legal/licenses folder

# imports

import discord
from discord.ext import commands
from discord import app_commands
import requests
import html
import asyncio
import json
import os
import random

# open config

config = open(r"config", 'r')
config.seek(0)

# define client and intents

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

# general variables for the bot (pulled from config)
 
bot_name = config.readlines()[2] # name of the bot
bot_name = bot_name.replace(f"\n", "")
config.seek(0)
bot_shde = config.readlines()[3] # bot short description
bot_shde = bot_shde.replace(f"\n", "")
config.seek(0)
bot_vers = config.readlines()[4] # bot version
bot_vers = bot_vers.replace(f"\n", "")
config.seek(0)
promo = config.readlines()[5] # promo message
promo = promo.replace(f"\n", "")
config.seek(0) 
rpc = config.readlines()[6] # rpc message
rpc = rpc.replace(f"\n", "")
guildnum = len(client.guilds) # variable for number of guilds

# top.gg promo related code

def ad_chance(chance=0.1): # 10%
    return random.random() < chance

# on ready code

@client.event
async def on_ready():
    print(f"Bot is online as {client.user}")
    await client.change_presence(activity=discord.Game(name=rpc))
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    print(f"Bot is active in {guildnum} guilds")

# slash commands

@client.tree.command(name="hello", description="Make the bot greet!") # hello command
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"<:am:1309893290921033818> My name is {bot_name}, and I'm the best {bot_shde} :fire:")
    if ad_chance(chance=0.1):
        await interaction.followup.send(promo, ephemeral=True)

@client.tree.command(name="help", description="Displays a short manual to help you operate the bot!") # help command
async def help(interaction: discord.Interaction):
    commands = discord.Embed(
        title=f"<:am:1309893290921033818> {bot_name} Discord Bot {bot_vers} <:am:1309893290921033818>", description=f"This is **THE BEST** {bot_shde}, devoid of AI, micro-transactions for major features and corporate enshitification! \n Created by itsnotAZ (itisnotAZ : https://itsnotaz.github.io/website/) \n ᴵ ᵗʳʸ ᵗᵒ ᵏᵉᵉᵖ ᵗʰⁱˢ ᵇᵒᵗ ˡⁱᵍʰᵗʰᵉᵃʳᵗᵉᵈ ᵇᵘᵗ ˢⁱⁿᶜᵉ ᵗʰᵉ ᵇᵒᵗ ᵖᵘˡˡˢ ᵐᵉᵐᵉˢ ᵃⁿᵈ ʲᵒᵏᵉˢ ᶠʳᵒᵐ ᵗʰᵉ ⁱⁿᵗᵉʳⁿᵉᵗ ⁱᵗ'ˢ ⁱᵐᵖᵒˢˢⁱᵇˡᵉ ᵗᵒ ᵐᵃᵏᵉ ᵗʰᵃᵗ ᶜᵉʳᵗᵃⁱⁿ ˢᵒ ᵖˡᵉᵃˢᵉ ᵈᵒⁿ'ᵗ ʰᵉˢⁱᵗᵃᵗᵉ ᵗᵒ ᶜᵒⁿᵗᵃᶜᵗ ᵐᵉ ᶠᵒʳ ᵃⁿʸ ᶜᵒⁿᶜᵉʳⁿˢ", color=0x336EFF
                )
    commands.add_field(name=":rofl: */joke* command", value="Make the bot tell a random joke!", inline=False)
    commands.add_field(name=":thinking: */trivia* command", value="Make the bot give a random true/false question!", inline=False)
    commands.add_field(name="<:re:1311335608932896818> */redditmeme* command", value="Make the bot fetch a random command from reddit!", inline=False)
    commands.add_field(name=":sparkles: */memify* command", value=f"Turn an image url and a bit of input into a meme! \n\n\n", inline=False)
    commands.add_field(name=":grey_exclamation: **Some more things you should know:**", value="- *Attribution*: https://github.com/itsnotAZ/absolute-memer/blob/main/legal/ATRIBUTION.md\n- *Terms of Service*: https://github.com/itsnotAZ/absolute-memer/blob/main/legal/ToS.md\n- *Privacy Policy*: https://github.com/itsnotAZ/absolute-memer/blob/main/legal/PRIVACY%20POLICY.md\n- *Official Website*: https://github.com/itsnotAZ/absolute-memer\n\n\n **MAKE SURE TO UPVOTE ME:** https://top.gg/bot/1309201141912965191\n **LEAVE A REVIEW:** https://top.gg/bot/1309201141912965191#reviews", inline=False)
    await interaction.response.send_message(embed=commands)
    if ad_chance(chance=0.1):
        await interaction.followup.send(promo, ephemeral=True)

@client.tree.command(name="joke", description="Tells a joke!") # joke command
async def joke(interaction: discord.Interaction):
    api_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt"
    response = requests.get(api_url)
    if response.status_code == 200:
        joke = response.text
        await interaction.response.send_message(f":rofl: Here is what I found:\n\n||{joke}||")
    else:
        print(f"Failed to retrieve joke. HTTP Status Code: {response.status_code}")
        await interaction.response.send_message("Sorry, I couldn't retrieve a joke for you. :frowning:")
    if ad_chance(chance=0.1):
        await interaction.followup.send(promo, ephemeral=True)
     
@client.tree.command(name="trivia", description="Sends a random trivia question that can be answered!") # trivia command
async def trivia(interaction: discord.Interaction):
    api_url = "https://opentdb.com/api.php?amount=1&type=boolean"
    response = requests.get(api_url)
    if response.status_code != 200:
        await interaction.response.send_message("Sorry, I couldn't retrieve a trivia question. :frowning:")
        return
    data = response.json()
    if data["response_code"] != 0 or not data["results"]:
        await interaction.response.send_message("Sorry, couldn't find any trivia questions at the moment. :frowning:")
        return
    question = data["results"][0]
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    await interaction.response.send_message(f"**:thinking: Question**:\n{question_text}\n\n**Options**:\n1. True\n2. False\n\nReply with 1 or 2!")
    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel and m.content.isdigit()
    try:
        msg = await client.wait_for("message", check=check, timeout=30)
        user_choice = int(msg.content)
        user_answer = "True" if user_choice == 1 else "False" if user_choice == 2 else None
        if user_answer:
            if user_answer == correct_answer:
                await interaction.followup.send("Correct :tada:! Good Job!")
            else:
                await interaction.followup.send(f"Incorrect. The correct answer was: '{correct_answer}'! :x:")
        else:
            await interaction.followup.send("Invalid choice. Please choose either 1 for True or 2 for False.")
    except asyncio.TimeoutError:
        await interaction.followup.send(f"Time's up :alarm_clock:! The correct answer was: {correct_answer}")
    if ad_chance(chance=0.1):
        await interaction.followup.send(promo, ephemeral=True)
     
@client.tree.command(name="memify", description="Creates a meme using the given image URL and top/bottom text!") # meme maker command
@app_commands.describe(image_url="URL of the image", top_text="Text at the top of the meme", bottom_text="Text at the bottom of the meme", font="Available fonts: titilliumweb, notosans, kalam, impact, titilliumweb-thin, segoe, hgminchob")
async def mememify(interaction: discord.Interaction, image_url: str, top_text: str, bottom_text: str, font: str):
    top_text = top_text.replace(" ", "_")
    bottom_text = bottom_text.replace(" ", "_")
    api_url = f"https://api.memegen.link/images/custom/{top_text}/{bottom_text}.png?background={image_url}?font={image_url}"
    await interaction.response.send_message(api_url)
    if ad_chance(chance=0.1):
        await interaction.followup.send(promo, ephemeral=True)
     
@client.tree.command(name="redditmeme", description="Grabs a meme from reddit!") # random meme from reddit command
async def mememify(interaction: discord.Interaction):
    api_url = "https://meme-api.com/gimme"
    response = requests.get(api_url)
    data = response.json()
    link = data.get('postLink')
    await interaction.response.send_message(f":rofl: Here is what I found! {link}")
    if ad_chance(chance=0.1):
        await interaction.followup.send(promo, ephemeral=True)
     
# run the client

client.run(os.environ["TOKEN"]) # requires a TOKEN env variable that contains the bot token. You can also just pass the token directly as a string.
