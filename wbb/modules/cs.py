import aiohttp
from wbb import app
from bs4 import BeautifulSoup
from pyrogram import filters



_MODULE_ = "Cricket"
_HELP_ = """To get the live cricket livescores
haha"""


@app.on_message(filters.command("cs"))
async def cs_command(_, message):
    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    async with aiohttp.ClientSession() as session:
      async with session.get(score_page) as resp:
          page = await resp.text()
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    Sed = "".join(match.get_text() + "\n\n" for match in result)
    await message.reply_text(
        f"<b><u>Match information Gathered Successfully</b></u>\n\n\n<code>{Sed}</code>",
        parse_mode="html",
    )
