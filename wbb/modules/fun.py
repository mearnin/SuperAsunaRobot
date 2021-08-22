from wbb import app
import requests
import re
from pyrogram import filters

__MODULE__ = "Fun"
__HELP__ = """
To get a gif/image of
wink /wink
hug /hug
pat /pat
pikachu /pikachu"""


@app.on_message(filters.command("wink"))
async def wink_command(_, message):
    hmm_s = "https://some-random-api.ml/animu/wink"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()
    
@app.on_message(filters.command("hug"))
async def hug_command(_, message):
    hmm_s = "https://some-random-api.ml/animu/hug"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()
   
   
@app.on_message(filters.command("pat"))
async def pat_command(_, message):
    hmm_s = "https://some-random-api.ml/animu/pat"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()
        
@app.on_message(filters.command("pikachu"))
async def pikachu_command(_, message):
    hmm_s = "https://some-random-api.ml/img/pikachu"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    if image_s.endswith(".png"):
       await client.send_photo(message.chat.id, image_s)
       return
    if image_s.endswith(".jpg"):
       await client.send_photo(message.chat.id, image_s)
       return
    await message.delete()