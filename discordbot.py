import discord
import os
import json
import requests
import Mods.calbot as calbot
import Mods.vision as vision
import Mods.calories as calories

with open("json/config.json") as h:
	config = json.load(h)
client = discord.Client()

@client.event
async def on_message(message):
	if type(message.channel).__name__ == "DMChannel":
		# If the message is a DM.
		for attachment in message.attachments:
			await message.channel.trigger_typing()
			food = calbot.calories_from_url(
				attachment.url, message.author.id, attachment.id)
			foodEmbed = discord.Embed(title="New Food Added")
			foodEmbed.add_field(name="Name", value=food["name"], inline=True)
			foodEmbed.add_field(name="Calories", value=food["calories"], inline=True)
			await message.channel.send(embed=foodEmbed)


@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("-------")

client.run(config["discord"]["token"])
