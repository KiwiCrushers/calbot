import discord, os, json, requests
import Mods.calbot as calbot
import Mods.vision as vision
import Mods.calories as calories

wolfram = calories.Client(key)#Replace key with an actual key
foodFile = open('FOOD.txt', 'r')
food = foodFile.read()
def check_food_for(item):
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
            calbot.from_url(attachment.url)
			calories_in_picture = 0
			for label in vision.detect_labels(path): #replace path with the storage
				if check_food_for(label):
					cals = wolfram.ask('How many calories are in ' + label)
					calories_in_picture += int(cals.split(' ')[0])
			


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("-------")

client.run(config["discord"]["token"])