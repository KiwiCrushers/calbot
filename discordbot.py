import discord, os, json, requests
import Mods.calbot as calbot

with open("json/config.json") as h:
    config = json.load(h)
client = discord.Client()

@client.event
async def on_message(message):
    if type(message.channel).__name__ == "DMChannel":
        # If the message is a DM.
        for attachment in message.attachments:
            calbot.from_url(attachment.url)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("-------")

client.run(config["discord"]["token"])