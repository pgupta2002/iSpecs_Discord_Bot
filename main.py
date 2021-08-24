import os
import discord
import requests
import json
import random
import schedule
from datetime import datetime
import pytz



t = pytz.timezone('Asia/Kolkata') 
datetime_ = datetime.now(t)
time_asia = str(datetime_.strftime("%H:%M:%S"))
print("Time:", datetime_.strftime("%H:%M:%S"))

client = discord.Client()

def get_status():
  response = requests.get("https://newsdata.io/api/1/news?apikey=pub_945b0592bd95f2e62ce96252aef8381f054&language=en&q=macbook%20OR%20iphone%20OR%20ipad")
  json_data = json.loads(response.text)
  res = json_data["results"]
  return res

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$status'):
    data = get_status()
    embed = discord.Embed(title="Apple Daily", description="Your daily source of Apple tech")
    for i in range(3):
        string = ""
        for x in data[i]["description"]:
            if(x == '.'):
                break
            else:
                string += x
        embed.add_field(name=data[i]["title"], value= "[" +  string  + "](" + data[i]["link"] + ")", inline=False)
    await message.channel.send(embed=embed)

def on_time():
    data = get_status()
    embed = discord.Embed(title="Apple Daily", description="Your daily source of Apple tech")
    for i in range(3):
        string = ""
        for x in data[i]["description"]:
            if(x == '.'):
                break
            else:
                string += x
        embed.add_field(name=data[i]["title"], value= "[" +  string  + "](" + data[i]["link"] + ")", inline=False)
    print(embed)

schedule.every().day.at("23:45:00").do(on_time)

my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))

