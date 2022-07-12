""" Alive module from https://github.com/AnonymousR1025/FallenRobot/blob/55c53a2f37f4062c63265375a7ca19b9a507afcd/FallenRobot/modules/alive.py"""

import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from MissKaur.events import register
from MissKaur import telethn as tbot
from MissKaur import SUPPORT_CHAT


PHOTO = [
    "https://telegra.ph/file/315d78ebea36b0a1b3435.jpg",
    "https://telegra.ph/file/7bd111132fce009e4605e.jpg",
    "https://telegra.ph/file/804a5f9a3c32bac1ae15c.jpg",
    "https://telegra.ph/file/43edaa8914b7ce8998336.jpg",
    "https://telegra.ph/file/abed92d9b3ff409793324.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ MissKaur~**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [Team MissKaur](https://t.me/TeamMissKaur)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/MissKaurXbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

__help__ = """
/repo - Get repo
/alive - Alive status
"""

__mod_name__ = "Alive"
