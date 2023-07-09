from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonX import app, Telegram
from config import *

# تعيين القناة الخاصة وزر الاشتراك

subscribe_button = InlineKeyboardButton("اشترك في القناة", url="https://t.me/{CHANNEL_DEV}")

# دالة لمعالجة الأمر /start
@Client.on_message(filters.command("start"))
async def start(client, message):
    # الرد على الامر /start بالأزرار المطلوبة
    if message.from_user.id == int(OWNER_ID):
        await message.reply("مرحباً بك! اليك الأزرار المطلوبة",
                            reply_markup=InlineKeyboardMarkup([[subscribe_button]]))
    else:
        await message.reply("أنت لست مطور البوت")


