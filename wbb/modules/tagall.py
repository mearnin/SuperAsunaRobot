from pyrogram import filters

from wbb.core.decorators.permissions import adminsOnly
from wbb import app


__MODULE__ = "Tag All"
__HELP__ = """To tag members in a chat
/tagall - just type this in the chat; you want to tag all."""

@app.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
@adminsOnly
async def tagall(_, message):
    await message.reply("`Processing.....`")
    sh = message.text.split(None, 1)[1]
    if not sh:
        sh = "Hi!"
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await app.send_message(message.chat.id, j, parse_mode="html")

