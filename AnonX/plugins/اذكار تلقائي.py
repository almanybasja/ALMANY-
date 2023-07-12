import time
from pyrogram import Client, filters

app = Client("my_account")

# المعرف الخاص بالمجموعة المراد إرسال الرسالة فيها
group_id = -100123456789


message_text = "تم إرسال رسالة تلقائية من خلال الكود الخاص بي!"

# المتغير الذي يمكننا استخدامه لتعطيل أو تفعيل الكود
enable_code = True

@app.on_message(filters.command("تفعيل", prefixes="/") & ~filters.private)
def enable_code_fn(client, message):
    global enable_code
    enable_code = True
    message.reply_text("تم تفعيل الكود بنجاح!")

@app.on_message(filters.command("تعطيل", prefixes="/") & ~filters.private)
def disable_code_fn(client, message):
    global enable_code
    enable_code = False
    message.reply_text("تم تعطيل الكود بنجاح!")

@app.on_message(filters.private)
def send_message(client, message):
    if enable_code:
        # إرسال الرسالة في المجموعة
        app.send_message(group_id, message_text)

        # انتظار 5 دقائق قبل إرسال الرسالة التالية
        time.sleep(5 * 60)
