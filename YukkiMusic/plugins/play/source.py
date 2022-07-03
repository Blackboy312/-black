import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس بلاك","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e3d2d281ff324c6d5eb3.jpg",
        caption=f"""[✨ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝚄𝚂𝙸𝙲 𝙱𝙻𝙰𝙲𝙺 🎀](https://t.me/Joker197432)\n\n[✨ 𝙳𝙴𝚅 𝚂𝙾𝚄𝚁𝙲𝙴 𝙱𝙻𝙰𝙲𝙺 🎀](https://t.me/Blackkig1)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "((𝙲𝙷𝙰𝙽𝙽𝙴𝙻))", url=f"https://t.me/Joker197432"), 
                ],[
                    InlineKeyboardButton(
                        "ᯓ 𓆩 ˹ 𝐁𝑳𝐀𝐂𝐊 ˼ 𓆪 𓆃", url=f"https://t.me/Blackkig1"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتك 🌐", url=f"https://t.me/Bot_JABWA_Bot?startgroup=true"),
                ],

            ]

        ),

    )
