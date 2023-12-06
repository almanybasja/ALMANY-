import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "تعاال يامطووري عاوزينك @K_F_P 🦅",


             "هذا مطوري @K_F_P 🖤🦅",
            

             "عاوزينننك @K_F_P 🦅😒",
            
           
 
            
            

        ]


        


@app.on_message(command(["الالماني","الماني","احمد"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
