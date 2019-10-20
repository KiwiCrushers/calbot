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
	if("today" in message.content.lower()):
		# Return food eaten today.
		meals = calbot.food_today(message.author.id)
		listEmbed = discord.Embed(title="Food Eaten Today", color=0x049be0)
		print(meals)
		for meal in meals["list"]:
			listEmbed.add_field(name=meal[2], value=str(meal[3]) + " Calories", inline=False)
		listEmbed.set_footer(text="Total Calories: " + str(meals["total"]))
		await message.channel.send(embed=listEmbed)

	if type(message.channel).__name__ == "DMChannel":
		# If the message is a DM.
		async with message.channel.typing():
			for attachment in message.attachments:
				await message.channel.trigger_typing()
				food = calbot.calories_from_url(
					attachment.url, message.author.id, attachment.id)
				foodEmbed = discord.Embed(title="New Food Added", color=0x368c36)
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
