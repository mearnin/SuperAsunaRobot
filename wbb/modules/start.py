from wbb import app
from pyrogram import filters

@app.on_message(filters.command("ystart"))
async def ystart_command(_, message):
     await message.reply_text("Hi I'm Yumiko and I'm already up")
