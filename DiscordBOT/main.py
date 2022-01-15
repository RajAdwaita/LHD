import discord
import os
from dotenv import load_dotenv
import pandas_datareader as pdr

#  TOKEN has been removed from the code for security reasons
# inclue your token in the .env file and run the code again

client = discord.Client()
# load_dotenv()


TOKEN = ""


def get_stock_price(ticker):
    data = pdr.DataReader(ticker, "yahoo")
    return data.iloc[-1]['Close']


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!bablu"):
        await message.channel.send("BABLU is watching!")
    if message.content == '$connect':
        await message.author.send("Glad To Meet You Dude!")

    if message.content.startswith("!stock"):
        if(len(message.content.split()) == 2):
            # await message.channel.send("Please provide a stock ticker")
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            await message.channel.send(f"The price of {ticker} is ${price}!")


@client.event
async def on_connect():
    print("BOT READY")

    # await channel.send("How is your day!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member}, welcome to the server!")
    # print(f'{member} has joined a server.')


client.run(TOKEN)
