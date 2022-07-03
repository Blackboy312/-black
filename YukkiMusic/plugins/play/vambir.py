import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","بلاك","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e3d2d281ff324c6d5eb3.jpg",
caption=f"""• الزرار الاول -> قناه السورس \n• الزرار الثاني -> هو مبرمج السورس""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "((𝙲𝙷𝙰𝙽𝙽𝙴𝙻))", url=f"https://t.me/Joker197432"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "ᯓ 𓆩 ˹ 𝐁𝑳𝐀𝐂𝐊 ˼ 𓆪 𓆃", url=f"https://t.me/Blackkig1"),
                ],
            ]
        ),
    )
