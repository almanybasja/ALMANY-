import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين ALMANY","المطورين","مطورين","مطورين الالماني"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1cf2e8eb817735b1c384b.jpg",
        caption=f"""*𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين الالماني ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺ALMANY", url=f"https://t.me/K_F_P"), 
                 ],[
                    
                
                
                ],[
                    
                
                    InlineKeyboardButton(
                        "★𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔⚡", url=f"https://t.me/AL515AT"),
                
                     ]
                ],

            ]

        ),

    )









@app.on_message(
    command(["شيكاغو تعال","عبادي","شيكاغو"])
 
)
async def yas(client, message):
    
    usr = await client.get_chat("T_N_T_RB")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔\nمعلومات مطور السورس2 \n↜︙Dev 𝗡𝗔𝗠𝗘 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :`{usr.id}`\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio} \n\n **𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
   command(["مبرمج السورس","مطور السورس"])
   
)
async def yas(client, message):
    usr = await client.get_chat("K_F_P")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔\nمعلومات مبرمج السورس \n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],  [
                    InlineKeyboardButton(
                        "استدعاء المبرمج", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )


@app.on_message(
  command(["المطور"])
  
)
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔 \nمعلومات المطور الاساسي\n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "استدعاء المطور", url=f"https://t.me/{usr.username}"),                        
                 ],
                      [
                    InlineKeyboardButton(
                        "قناة المطور", url=f"https://t.me/{SUPPORT_CHANNEL}"),                        
                 ],
            ]
        ),
    )
@app.on_message(
   command(["قناة المطور"])
   
)
async def yas(client, message):
    usr = await client.get_chat(SUPPORT_CHANNEL)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**قناة المطور \nاشترك فالقناه فضلا وليس امرا من الازرار في الاسفل \n\n رابط القناه: : https://t.me/{usr.username}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ], 
            ]
        ),
    )



@app.on_message(
   command(["ذكاء اصتناعي"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1cf2e8eb817735b1c384b.jpg",
        caption=f"""**𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس الالماني\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n سؤال + السؤال بالاسفل 👇\n**𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺ALMANY", url=f"https://t.me/k_f_p"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔⚡", url=f"https://t.me/HL_BG"),
                ],

            ]

        ),

    )



@app.on_message(
   command(["قرأن"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1cf2e8eb817735b1c384b.jpg",
        caption=f"""**𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس الالماني\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𝘼𝙇𝙈𝘼𝙉𝙔 ˹َّّ", url=f"https://t.me/K_F_P"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙈𝘼𝙉𝙔⚡", url=f"https://t.me/AL515AT"),
                ],

            ]

        ),

    )

    
