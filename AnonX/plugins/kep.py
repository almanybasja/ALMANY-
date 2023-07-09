
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

app = Client("my_account")

@app.on_message(filters.command(["start"]))
def start(client, message):
    channel_username = "your_channel_username"  # استبدل بمعرف قناتك هنا

    bot_button = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("زيارة القناة", url=f"https://t.me/{channel_username}"),
            InlineKeyboardButton("تحقق من الاشتراك", callback_data="check_subscription")
        ]]
    )

    message.reply_text("مرحبًا بك! اضغط على أحد الأزرار بالأسفل للاشتراك.", reply_markup=bot_button)

@app.on_callback_query()
def callback_handler(client, callback):
    if callback.data == "check_subscription":
        channel_id = -1001234567890  # استبدل بمعرف قناتك هنا

        if client.get_chat_member(chat_id=channel_id, user_id=callback.from_user.id).status == "member":
            callback.answer("تم التحقق من الاشتراك! مستخدم صالح.", show_alert=True)
        else:
            callback.answer("المرجو الاشتراك في القناة أولاً.", show_alert=True)

app.run()
