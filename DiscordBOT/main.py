import discord
import os
from dotenv import load_dotenv
import pandas_datareader as pdr

client = discord.Client()
# load_dotenv()

TOKEN = "OTMxNTI4ODQwMjU2MzExMzA3.YeFv1g.n2Qzzaf9fWVE3Lo1Py5x9rPSVs4"


def get_stock_price(ticker):
    data = pdr.DataReader(ticker, "yahoo")
    return data.iloc[-1]['Close']


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!bablu"):
        await message.channel.send("BABLU is watching")
    if message.content == '$connect':
        await message.author.send("Glad To Meet You Dude")

    if message.content.startswith("!stock"):
        if(len(message.content.split()) == 2):
            # await message.channel.send("Please provide a stock ticker")
            price = get_stock_price(message.content.split(" ")[1])


@client.event
async def on_connect():
    print("BOT READY")

    channel = client.get_channel(846143020637618207)
    # await channel.send("How is your day!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member}, welcome to the server!")
    # print(f'{member} has joined a server.')


client.run(TOKEN)
