from wbb import app
from wbb import app2
from pyrogram import filters
import bs4
import aiohttp
import requests

_MODULE_ = "Apps"
_HELP_ = """To search an app on playstore"""
    
    
@app.on_message(filters.command("ply"))
async def ply_command(_, message):        
        text = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching...")
        app_name = '+'.join(text.split(' '))
        page = requests.get(f"https://play.google.com/store/search?q={app_name}&c=apps")
        soup = bs4.BeautifulSoup(page.content, 'lxml', from_encoding='utf-8')
        results = soup.findAll("div", "ZmHEEd")

        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext(
            'div', 'pf5lIe'
        ).find('div')['aria-label'].replace("Rated ", "⭐️ ").replace(
            " out of ", "/"
        ).replace(" stars", "", 1).replace(" stars", "⭐️").replace("five", "5")
        app_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        support = "@countdraculasupport"
        app_details = f"[📲]({app_icon}) **{app_name}**\n\n"
        app_details += f"`Developer :` [{app_dev}]({app_dev_link})\n"
        app_details += f"`Rating :` {app_rating}\n"
        app_details += f"`Features :` [View in Play Store]({app_link})"
        app_details += f"\n\n===> {support} <==="
        await m.edit(app_details, disable_web_page_preview=False) 
