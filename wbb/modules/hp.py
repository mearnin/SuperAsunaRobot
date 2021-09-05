import asyncio
import bs4
import requests
from pyrogram import filters
from wbb import app

                               
@app.on_message(filters.command("hp"))
async def hp_command(_, message):
    text = message.text.split(None, 1)[1]
    m = await message.reply_text("```Searching...```")
    page = requests.get("https://harrypotter.fandom.com/wiki/{text}")
    soup = bs4.BeautifulSoup(page.content, 'lxml', from_encoding='utf-8')

    effects = soup.findAll("div", "effect")
    side_effects = soup.findAll("div", "side-effects")
    characteris = soup.findAll("div", "characteristics")
    time = soup.findAll("div", "time")
    ing = soup.findAll("div", "ingredients")
    details = f"**{text}√**\n\n"
    details += f"Effects : {effects}\n"
    details += f"Side Effects : {side_effects}\n"
    details += f"Characteristics : {characteris}\n"
    details += f"Brewing Time : {time}\n"
    details += f"Ingredients : {ing}\n"
    await m.edit(details)
