import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AnonX import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus
iddof = []

@app.on_message(
     command(["قفل زوجني","تعطيل زوجني"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"يا {message.from_user.mention}\n لعبة زوجني مقفله من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text(f"تم قفل لعبة زوجني بنجاح\n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا هنا")

@app.on_message(
    command(["فتح زوجني","تفعيل لعبة زوجني"])
    & filters.group
)
async def idljjopen(client:Client, message:Message):
    dev = (OWNER_ID)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"يا {message.from_user.mention}\nلعبة زوجني معفله من قبل")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"تم فتح لعبة زوجني بنجاح\n\n من قبل ←{message.from_user.mention}")
 
    
@app.on_message(command(['زوجني','ز']))
def iddd(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"• اخترت لك هذا الشخص {random_member_mention} \n 🙈♥️",
        f"• اخترت لك هذا الشخص \n {random_member_mention} \n **"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
