import os
import re
import sys
import ffmpeg
import asyncio
import subprocess
from asyncio import sleep
from pyrogram import filters
from pyrogram.types import Message
from sample_config import AUDIO_CALL, VIDEO_CALL
from wbb.modules.video import ydl, group_call
from helpers.decorators import authorized_users_only, sudo_users_only
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from wbb import app


__MODULE__ = "Video Play"
__HELP__ = """
**Voice chat video/audio music player๐ธ**
Thanks @AsmSafone for this โค๏ธ

Add @ManuSath to your group and start a video chat then vollia enjoy!!!๐
**Commands==>**
๐งAudio play

-/play reply to an audio file or a youtube link or a m3u8 link

๐ฝ๏ธVideo play

-/stream reply to a video file or a youtube link or a m3u8 link
-/pause pause video or audio
-/resume resume play
-/endstream end streaming audio/ video

๐ต๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐ ๐ฐ๐ฎ๐ป ๐ฏ๐ฒ ๐๐๐ผ๐ฝ๐ฝ๐ฒ๐ฑ ๐ฎ๐ ๐ฎ๐ป๐ ๐๐ถ๐บ๐ฒ"""

USERNAME = "SuperAsunaRoBot"

@app.on_callback_query(filters.regex("pause_callback"))
async def pause_callbacc(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"โธ Paused !"
        await AUDIO_CALL[chat_id].set_audio_pause(True)
    elif chat_id in VIDEO_CALL:
        text = f"โธ Paused !"
        await VIDEO_CALL[chat_id].set_video_pause(True)
    else:
        text = f"โ Nothing is Playing !"
    await app.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )

@app.on_callback_query(filters.regex("resume_callback"))
async def resume_callbacc(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"โถ๏ธ Resumed !"
        await AUDIO_CALL[chat_id].set_audio_pause(False)
    elif chat_id in VIDEO_CALL:
        text = f"โถ๏ธ Resumed !"
        await VIDEO_CALL[chat_id].set_video_pause(False)
    else:
        text = f"โ Nothing is Playing !"
    await app.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )


@app.on_callback_query(filters.regex("end_callback"))
async def end_callbacc(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"โน๏ธ Stopped !"
        await AUDIO_CALL[chat_id].stop()
        AUDIO_CALL.pop(chat_id)
    elif chat_id in VIDEO_CALL:
        text = f"โน๏ธ Stopped !"
        await VIDEO_CALL[chat_id].stop()
        VIDEO_CALL.pop(chat_id)
    else:
        text = f"โ Nothing is Playing !"
    await app.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )
    await app.send_message(
        chat_id=CallbackQuery.message.chat.id,
        text=f"โ **Streaming Stopped & Left The Video Chat !**"
    )
    await CallbackQuery.message.delete()



@app.on_message(filters.command(["play", f"play@{USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def play(_, m: Message):
    msg = await m.reply_text("๐ `Processing ...`")
    chat_id = m.chat.id
    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await msg.edit("โ __Send Me An Live Radio Link / YouTube Video Link / Reply To An Audio To Start Audio Streaming!__")

    elif ' ' in m.text:
        text = m.text.split(' ', 1)
        query = text[1]
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, query)
        if match:
            await msg.edit("๐ `Starting YouTube Audio Stream ...`")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get('formats', [meta])
                for f in formats:
                    ytstreamlink = f['url']
                link = ytstreamlink
            except Exception as e:
                await msg.edit(f"โ **YouTube Download Error !** \n\n`{e}`")
                print(e)
                return
        else:
            await msg.edit("๐ `Starting Live Audio Stream ...`")
            link = query

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_audio(link, repeat=False)
            AUDIO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_photo(
               photo=thumb, 
               caption=f"โถ๏ธ **Started [Video Streaming]({query}) In {m.chat.title} !**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="โธ",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="โถ๏ธ",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="โน๏ธ",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f"โ **An Error Occoured !** \n\nError: `{e}`")

    elif media.audio or media.document:
        await msg.edit("๐ `Downloading ...`")
        audio = await client.download_media(media)

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_audio(audio, repeat=False)
            AUDIO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_text( 
               text=f"โถ๏ธ **Started [Video Streaming](https://t.me/superasunasupport) In {m.chat.title} !**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="โธ",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="โถ๏ธ",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="โน๏ธ",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f"โ **An Error Occoured !** \n\nError: `{e}`")

    else:
        await msg.edit(
            "๐๐ปโโ๏ธ Do you want to search for a YouTube song?",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No โ", callback_data="close"
                    )
                ]
            ]
        )
    )


@app.on_message(filters.command(["restart", f"restart@{USERNAME}"]))
@sudo_users_only
async def restart(client, m: Message):
    k = await m.reply_text("๐ `Restarting ...`")
    await sleep(3)
    os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        await k.edit("โ **Restarted Successfully! \nJoin @AsmSafone For More!**")
    except:
        pass

