import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID
from pyrogram import filters

@app.on_message(command(["نداء","ن"]))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"ووين ككارس لنا واجد نرجو فيك 😾 {random_member_mention}",
        f"• يـا قمـري ❤️‍🔥 {random_member_mention}",
        f"حبي فوتك من الخاص وتعال 🤔 {random_member_mention}",
        f"• يـا راس السطل تعال {random_member_mention}",
        f"• انت ليش قمر هكي 🌚♥ {random_member_mention}"
    ])
    # client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')


