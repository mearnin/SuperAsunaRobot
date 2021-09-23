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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from wbb import app


__MODULE__ = "Video Play"
__HELP__ = """
**Voice chat video/audio music player🎸**
Thanks @AsmSafone for this ❤️

Add @ManuSath to your group and start a video chat then vollia enjoy!!!😃
**Commands==>**
🎧Audio play

-/play reply to an audio file or a youtube link or a m3u8 link

📽️Video play

-/stream reply to a video file or a youtube link or a m3u8 link
-/pause pause video or audio
-/resume resume play
-/endstream end streaming audio/ video

𝑵𝒐𝒕𝒆 𝒕𝒉𝒂𝒕 𝒕𝒉𝒊𝒔 𝒔𝒆𝒓𝒗𝒊𝒄𝒆 𝒊𝒔 𝒖𝒏𝒔𝒕𝒂𝒃𝒍𝒆 𝒂𝒏𝒅 𝗰𝗮𝗻 𝗯𝗲 𝘀𝘁𝗼𝗽𝗽𝗲𝗱 𝗮𝘁 𝗮𝗻𝘆 𝘁𝗶𝗺𝗲"""

USERNAME = "SuperAsunaRoBot"
@app.on_message(filters.command(["play", f"play@{USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def play(_, m: Message):
    msg = await m.reply_text("🔄 `Processing ...`")
    chat_id = m.chat.id
    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await msg.edit("❗ __Send Me An Live Radio Link / YouTube Video Link / Reply To An Audio To Start Audio Streaming!__")

    elif ' ' in m.text:
        text = m.text.split(' ', 1)
        query = text[1]
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, query)
        if match:
            await msg.edit("🔄 `Starting YouTube Audio Stream ...`")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get('formats', [meta])
                for f in formats:
                    ytstreamlink = f['url']
                link = ytstreamlink
            except Exception as e:
                await msg.edit(f"❌ **YouTube Download Error !** \n\n`{e}`")
                print(e)
                return
        else:
            await msg.edit("🔄 `Starting Live Audio Stream ...`")
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
            await msg.edit(f"▶️ **Started [Audio Streaming]({query}) In {m.chat.title} !**", disable_web_page_preview=True)
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured !** \n\nError: `{e}`")

    elif media.audio or media.document:
        await msg.edit("🔄 `Downloading ...`")
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
            await msg.edit(f"▶️ **Started [Audio Streaming](https://t.me/AsmSafone) In {m.chat.title} !**", disable_web_page_preview=True)
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured !** \n\nError: `{e}`")

    else:
        await msg.edit(
            "💁🏻‍♂️ Do you want to search for a YouTube song?",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@app.on_message(filters.command(["restart", f"restart@{USERNAME}"]))
@sudo_users_only
async def restart(client, m: Message):
    k = await m.reply_text("🔄 `Restarting ...`")
    await sleep(3)
    os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        await k.edit("✅ **Restarted Successfully! \nJoin @AsmSafone For More!**")
    except:
        pass

