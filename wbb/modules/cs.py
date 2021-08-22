"""
MIT License
Copyright (c) 2021 TheHamkerCat
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import aiohttp
from wbb import app
from bs4 import BeautifulSoup
from pyrogram import filters



__MODULE__ = "Cricket"
__HELP__ = """
To get the live cricket livescores haha
/cs
Will automatically give you latest cricket information."""


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
