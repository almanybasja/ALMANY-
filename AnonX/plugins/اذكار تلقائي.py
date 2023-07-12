
import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus



# المعرف الخاص بالمجموعة المراد إرسال الرسالة فيها


# النص الذي يتم إرساله في الرسالة
message_text = []

# المتغير الذي يمكننا استخدامه لتعطيل أو تفعيل الكود
enable_code = True

iddof = []

@app.on_message(
     command(["قفل الاذكار","تعطيل الاذكار"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    global enable_code
    enable_code = True
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")    
     
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"يا {message.from_user.mention}\n الاذكار التلقائيه مقفله من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الاذكار التلقائيه بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")

@app.on_message(
    command(["فتح الاذكار","تفعيل الاذكار"])
    & filters.group
)
async def idljjopen(client, message):
    global enable_code
    enable_code = False
    dev = (OWNER_ID)
    haya = (6275847466,6195765774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")       
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\الاذكار التلقائيه معفل من قبل**")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم فتح امر الاذكار التلقائيه بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 
   


@app.on_message(command(["اذكار"])& filters.group)
def send_message(client:Client, message:Message):
    if enable_code:
        # إرسال الرسالة في المجموعة
        app.send_message(message.chat.id, message_text)

        # انتظار 5 دقائق قبل إرسال الرسالة التالية
        time.sleep(5 * 60)
