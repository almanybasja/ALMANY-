
import time
from pyrogram import Client, filters
from strings.filters import command
from AnonX import app
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatMemberStatus 

# النص الذي يتم إرساله في الرسالة
message_text = "تم إرسال رسالة تلقائية من خلال الكود الخاص بي!"

# المتغير الذي يمكننا استخدامه لتعطيل أو تفعيل الكود
enable_code = True

@app.on_message(command("تفعيل") & ~filters.group)


async def enable_code_fn(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:  
       global enable_code
       enable_code = True
       message.reply_text("تم تفعيل الكود بنجاح!")
    else:
        message.reply_text("لست مشرف")
@app.on_message(command("تعطيل") & ~filters.group)
async def disable_code_fn(client, message:Message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if not get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:  
       global enable_code
       enable_code = False
       message.reply_text("تم تعطيل الكود بنجاح!")
    else:
        message.reply_text("لست مشرف")      

@app.on_message(filters.group)
def send_message(client, message:Message):
    if enable_code:
        # إرسال الرسالة في المجموعة
        app.send_message(message.chat.id, message_text)

        # انتظار 5 دقائق قبل إرسال الرسالة التالية
        time.sleep(20)
