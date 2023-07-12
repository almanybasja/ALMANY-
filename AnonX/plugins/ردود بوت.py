import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID
from pyrogram import filters

txt = [

            "؏ـيوٍڼ حـيآهہ😻🫶",


             "ﻧ؏ـ۾ 🥺❤",
            

            "هہذآ آڛـﻤــي 🫶😻",
            
            
            "ضـوꪆ حـيـاﮪ،💗🧸!َ''))",
            
            
            "نعٓم يـﺣـبـعـﻣـري،🥺🧡🌸!َ''))",
            
            
             "ﺷِﻧڻ تـبـي🙂😒",
            
            
 
            
            

        ]
txt1 = [

            "**؏ـيوٍڼ 😻🫶 البوت يا مطوريي**",


             "**ااحسنن مطوور فالدنياا كلههاا**",
            

            "**اطلق من يصيحح بووت**",
            
            
           
            
            
 
            
            

        ]



        


@app.on_message(command([{MUSIC_BOT_NAME}]))


async def cutt(client: Client, message: Message):
     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(


         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       
     
        
