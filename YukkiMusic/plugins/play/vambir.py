import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","جابو","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/8c00ae97a8446f27be7d0.jpg",
caption=f"""✧ الزرار الاول -> قناه السورس \n✧ الزرار الثاني -> هو مبرمج السورس""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "𓂄𓆩sᴏᴜʀᴄᴇ sᴀɪᴅɪ𓆪𓂁", url=f"https://t.me/S_a_i_d_i"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "𓄼⦁ 𝗝ٰٖ𝗔ٰٖ𝗕ٰٖ𝗪ٰٖ𝗔ٰٖ ➪🇳🇱⦁𓄹", url=f"https://t.me/JABWA"),
                ],
            ]
        ),
    )
