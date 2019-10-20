import discord
import os
import json
import requests
import Mods.calbot as calbot
import Mods.vision as vision
import Mods.calories as calories

def check_food_for(item):
	food = open("FOOD.txt").read()
	if item in food:
		return True
	else:
		return False


with open("json/config.json") as h:
	config = json.load(h)
client = discord.Client()
calories = calories.Client(config["wolfram"]["app_id"])


@client.event
async def on_message(message):
	if type(message.channel).__name__ == "DMChannel":
		# If the message is a DM.
		for attachment in message.attachments:
			filePath = calbot.from_url(
				attachment.url, message.author.id, attachment.id)
			calories_in_picture = 0
			# replace path with the storage
			for label in vision.detect_labels(filePath):
				label = label.description.lower()
				print(label)
				if check_food_for(label):
					cals = calories.ask(label)
					print(cals)
					calories_in_picture += int(cals)


@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("-------")

client.run(config["discord"]["token"])
