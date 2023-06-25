
from config import OWNER_ID,  API_ID,  BOT_TOKEN,  API_HASH
import asyncio 
from AnonX import app
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from datetime import date
from pyrogram.errors import FloodWait
from strings.filters import command 
token =(BOT_TOKEN) 
ownerID =(OWNER_ID) 
bot = Client(
  'bot'+token.split(":")[0],
  API_ID, 
  API_HASH,
  bot_token=token, in_memory=True
)



STARTKEY = InlineKeyboardMarkup(
       [
         [
           InlineKeyboardButton("≈ إذاعة للمستخدمين ≈", callback_data="broadcast")
         ],
         [
           InlineKeyboardButton("≈ الاحصائيات ≈", callback_data="stats"),
           InlineKeyboardButton("≈ الأدمنية ≈", callback_data="adminstats"),
           InlineKeyboardButton("≈ المحظورين ≈", callback_data="bannedstats"),
         ],
         [
           InlineKeyboardButton("≈ كشف مستخدم ≈",callback_data="whois"),
           InlineKeyboardButton("≈ حظر مستخدم ≈",callback_data="ban"),
         ],
         [
           InlineKeyboardButton("≈ الغاء حظر مستخدم ≈",callback_data="unban"),
         ],
         [
           InlineKeyboardButton("≈ رفع ادمن ≈",callback_data="addadmin"),
           InlineKeyboardButton("≈ تنزيل ادمن ≈",callback_data="remadmin"),
         ]
       ]
     )
