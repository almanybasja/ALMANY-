from strings.filters import command
from AnonX import app
from pyrogram import Client, filters
from pyrogram.types import Message



    # يجب أن يرسل الأمر المشترك إلى المجموعة لتنفيذه
@app.on_message(filters.group)
def block_stickers(client:Client, message:Message):
        # يتم حجب الملصقات بالحذف في المجموعة
        if message.text == "قفل الملصقات":
            client.set_chat_permissions(message.chat.id, can_send_stickers=False)

        # يتم فتح الملصقات بعدم الحذف في المجموعة
        elif message.text == "فتح الملصقات":
            client.set_chat_permissions(message.chat.id, can_send_stickers=True)

        # إرسال رسالة استجابة للإعلان عن تمكين أمر قفل وفتح الملصقات
        client.send_message(message.chat.id, "تم تنفيذ الأمر!")
