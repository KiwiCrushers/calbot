import discord, os, json, requests
import Mods.calbot as calbot
import Mods.vision as vision

def check_food_for(item):
	with open('FOOD.txt', 'r') as food:
		if item in food:
			return True
		else:
			return False

with open("json/config.json") as h:
    config = json.load(h)
client = discord.Client()

@client.event
async def on_message(message):
    if type(message.channel).__name__ == "DMChannel":
        # If the message is a DM.
        for attachment in message.attachments:
            calbot.from_url(attachment.url, message.author.id)
			#For each attatchment after calbot do vision.detect_labels(path), which returns all labels for the images
			#For each label check if label is food


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("-------")

client.run(config["discord"]["token"])