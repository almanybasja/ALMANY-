from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from config import BANNED_USERS
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import set_loop
from AnonX.utils.decorators import AdminRightsCheck
from AnonX.utils.inline.play import close_keyboard

# Commands
STOP_COMMAND = get_command("STOP_COMMAND_chh")


@app.on_message(
    command(STOP_COMMAND)
    & filters.channel
    & ~filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    await Anon.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.chat.first_name),
        reply_markup=close_keyboard,
    )
