import asyncio
import os
import time
import requests
import aiohttp
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from asyncio import gather
from pyrogram.errors import FloodWait
import pyrogram
from pyrogram import Client, filters
import requests


from pyrogram import Client
from pyrogram.api import functions


is_active = True 

def toggle_code_active():
    global is_active
    is_active = not is_active



@app.on_message()
async def get_prayer_times(client, message):

        if message.text == "مواعيد الصلاه ":
            await client.send_message(message.chat.id, "مرحبًا! للحصول على مواعيد الصلاة في ليبيا، ارسل لي '/prayer'.")

        elif message.text == "/prayer":
            if is_active:
                prayer_times = await app.send(functions.messages.GetDialogs(offset_date=0, offset_id=0, offset_peer=None, limit=1, hash=0))
                await client.send_message(message.chat.id, prayer_times)
            else:
                await client.send_message(message.chat.id, "تم تعطيل كود مواعيد الصلاة.")

        elif message.text == "تفعيل التوقيت":
            toggle_code_active()
            await client.send_message(message.chat.id, f"تم تغيير حالة تفعيل الكود: {is_active}")

    
