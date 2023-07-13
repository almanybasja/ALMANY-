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

# أولًا، سنحتاج إلى API key من موقع prayer times المختص بجلب مواعيد الصلاة في ليبيا
api_key = "https://api.pray.zone/v2/times/today.json?city=tripoli&state=tripoli&country=libya"
@app.on_message(
    command(["توقيت الصلاه"])
)

def  get_prayer_times(country):
    url = f"https://api.pray.zone/v2/times/today.json?city={country}&school=8"
    response = requests.get(url)
    data = response.json()
    return data["results"]["datetime"][0]["times"]

# ننشئ client بواسطة API key



@app.on_message(filters.text)
def handle_message(client:Client, message:Message):
    chat_id = message.chat.id
    country = message.text

    prayer_times = get_prayer_times(country)
    reply = f"مواعيد الصلاة في {country}: \n"
    reply += f"الفجر: {prayer_times['Fajr']} \n"
    reply += f"الشروق: {prayer_times['Sunrise']} \n"
    reply += f"الظهر: {prayer_times['Dhuhr']} \n"
    reply += f"العصر: {prayer_times['Asr']} \n"
    reply += f"المغرب: {prayer_times['Maghrib']} \n"
    reply += f"العشاء: {prayer_times['Isha']} \n"

    client.send_message(chat_id, reply)

# لنبدأ تنفيذ البرنامج
with app:


