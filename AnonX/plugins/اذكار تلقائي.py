import time
from pyrogram import Client, filters
from pyrogram.types import Message





message_text = [
    
]


enable_code = True

@app.on_message(command("تفعيل") & ~filters.group)
def enable_code_fn(client, message):
    global enable_code
    enable_code = True
    message.reply_text("تم تفعيل الكود بنجاح!")

@app.on_message(command("تعطيل") & ~filters.group)
def disable_code_fn(client: Client, message:Message):
    global enable_code
    enable_code = False
    message.reply_text("تم تعطيل الكود بنجاح!")

@app.on_message(filters.group)
def send_message(client: Client, message:Message):
    if enable_code:
       
        app.send_message(message.chat.id, message_text)

        
        time.sleep(5 * 60)
