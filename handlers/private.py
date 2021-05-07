from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEOycBglaXxgN1VWNe8UMwECeyPxxhkDQACzQEAAvFQKFSmX8Ai5gisyh8E")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Ihsan | StreamOxygen](https://t.me/RxyMX).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "IG OWNER", url="https://instagram.com/ihsan_rxymx")
                  ],[
                    InlineKeyboardButton(
                        "Group", url="https://t.me/animegrupindo"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/animechanelindo")
                ],[ 
                   InlineKeyboardButton(
                        "Bantuan", url="https://t.me/IhsanBio/62"
                    ),
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/AnimeSongRobot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/animechanelindo")
                ]
            ]
        )
   )


