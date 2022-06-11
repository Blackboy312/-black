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
    command(["سورس جابوا","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1de02fae526da7a3dfe67.jpg",
        caption=f"""[⌁ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝚄𝚂𝙸𝙲 𝚂𝙰𝙸𝙳𝙸 🎸](https://t.me/S_a_i_d_i)\n\n[⌁ 𝙳𝙴𝚅 𝚂𝙾𝚄𝚁𝙲𝙴 𝙹𝙰𝙱𝚆𝙰 🎸](https://t.me/JABWA)\n\n[⌁ 𝙳𝙴𝚅 𝚂𝙾𝚄𝚁𝙲𝙴 𝙹𝙴𝙺𝙰 🎸](https://t.me/DevJeka)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "˹ٰ𝗦ِٰٰٰٰٰٰٰٰ𝗢ِٰ𝗨ِٰ𝗥ِٰ𝗖ِٰ𝗘ٰٰٰٰٰٰٰٰٰٰٰٰٰ ٰ𝗦ِٰ𝗔ِٰ𝗜ِٰ𝗗ِٰ𝗜ٰ˼", url=f"https://t.me/S_a_i_d_i"), 
                ],[
                    InlineKeyboardButton(
                        "･ َِᥴُ ِِِꪋَٖ ꪶَِٰ ِꪑَٖ ☕️َِٖ🌿.", url=f"https://t.me/UUJEA"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك 𖣳", url=f"https://t.me/Bot_JABWA_Bot?startgroup=true"),
                ],

            ]

        ),

    )
