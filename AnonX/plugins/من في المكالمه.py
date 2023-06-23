from pyrogram import filters, Client
from AnonX import app
import asyncio
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonX.core.call import Anon
from AnonX.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)

@app.on_message(filters.regex("^مم في المكالمه$"))
async def strcall(client, message):
    assistant = await group_assistant(Anon,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./AnonX/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="الناس القاعده في المكالمه تكذب:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يرغوي "
            else:
                mut="ساكت "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"المكالمه مش مفتوحه اصلا")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام")
    except AlreadyJoinedError:
        text="االناس القاعده في المكالمه تكذب:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يرغوي"
            else:
                mut="ساكت "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"** - تم انهاء مكالمة الفيديو مدتها {da} ثواني وصكرها {message.from_user.first_name}**")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقه {message.from_user.first_name}**")
        elif 2 <= ma[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقتين {message.from_user.first_name}**")
        elif 3 <= ma[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ma[0]} دقايق {message.from_user.first_name}**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ma[0]} دقيقه {message.from_user.first_name}**")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعه {message.from_user.first_name}**")
        elif 2 <= ho[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعتين {message.from_user.first_name}**")
        elif 3 <= ho[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ho[0]} ساعات {message.from_user.first_name}**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ho[0]} ساعة {message.from_user.first_name}**")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يوم {message.from_user.first_name}**")
        elif 2 <= day[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يومين {message.from_user.first_name}**")
        elif 3 <= day[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {day[0]} ايام {message.from_user.first_name}**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {day[0]} يوم {message.from_user.first_name}**")
