from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off
from pyrogram.types import Message

async def play_logs(Message, streamtype):
    if await is_on_off(LOG):
        if Message.chat.username:
            chatusername = f"@{Message.chat.username}"
        else:
            chatusername = "محادثه خاصه"
        logger_text = f"""
**{MUSIC_BOT_NAME} مسجل التشغيل**

**الدردشه:** {Message.chat.title} [`{Message.chat.id}`]
**المعرف:** @{Message.from_user.username}
**الايدي:** `{Message.from_user.id}`
**رابط الدردشه:** {chatusername}

**تم البحث بواسطة:** {Message.text}

**نوع المشغل:** {streamtype}"""
        if Message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
