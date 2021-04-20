from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**aloo, {message.from_user.first_name}!</b>

Saya adalah bot musik yang dirancang khusus untuk menemani anda memutar musik melalui voice call grup

berikut ini adalah kontak owner dan gc nya hehe. 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "OWNER BOT", url="https://t.me/malekntll"
                  ],[
                    InlineKeyboardButton(
                        "GROUP 1", url="https://t.me/pemudapemuditersesatt"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/subsajeudahh"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "GROUP 2", url="https://t.me/teman_gabuttt"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**bot musik menyalaaa**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CHANNEL 2", url="https://t.me/joinsinicepett")
                ]
            ]
        )
   )


