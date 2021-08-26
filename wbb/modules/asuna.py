import os
import logging
import asyncio
import random

from pyrogram import filters
from wbb import app

REPLY = (
"Hi! How are you?",
"Heared my name! What do you want to do?",
"Hi! How can I help you?",
"Don't tell its me😡, I know nothing on that topic even",
"Please leave me alone😒",
"Don't get fun with my name!!! I don't like it🤬",
"Don't forget to recommend me to your friends❤️😎")

@app.on_message(filters.text('m', "Asuna"))
async def Asuna(_, message):
    if message.chat.type != "private":
      await message.reply_text(random.choice(REPLY))

@app.on_message(filters.text('m', "asuna"))
async def asuna(_, message):
    if message.chat.type != "private":
      await message.reply_text(random.choice(REPLY))

@app.on_message(filters.text("AsunaRobot"))
async def AsunaRobot(_, message):
    if message.chat.type != "private":
      await message.reply_text(random.choice(REPLY))
