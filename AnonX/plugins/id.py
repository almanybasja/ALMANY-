import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus 





klb = []

@app.on_message(command("رفع كلب"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in klb:
    klb.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n كلب من قبل {message.from_user.mention}😂♥️")


@app.on_message(command("ت كلب"))
async def tnzelnmla(client, message:Message):
  if message.reply_to_message.from_user.mention in klb:
    klb.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة الكلاب 😂♥️")


@app.on_message(command("المرفوعين كلاب"))
async def nml(client, message):
  kq = ""
  for n in klb:
      kq += n + "\n"
  await message.reply_text(f"**المرفوعين كلاب \n\n{kq}**")
  if not klb in kq:
     await message.reply_text("**لم يتم رفع كلاب بعد**")

zoj = []


@app.on_message(command("رفع زوجي"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in zoj:
    zoj.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  زوج لـ {message.from_user.mention}😂♥️**")


@app.on_message(command("ت زوجي"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in zoj:
    zoj.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة المتزوجين رد عزابي 😂♥️**")


@app.on_message(command("المرفوعين المتزوجين"))
async def nml(client, message):
  zq = ""
  for n in zoj:
      zq += n + "\n"
  await message.reply_text(zq)
  if not zoj in zq:
     await message.reply_text("**لم يتم رفع متزوجين بعد**")

hth =[]


@app.on_message(command("رفع حثاله"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in hth:
    hth.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  حثاله من قبل {message.from_user.mention}😂♥️**")


@app.on_message(command("ت حثاله"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in hth:
    hth.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة الحثاله 😂♥️**")


@app.on_message(command("المرفوعين حثاله"))
async def nml(client, message):
  hq = ""
  for n in hth:
      hq += n + "\n"
  await message.reply_text(hq)
  if not hth in hq:
     await message.reply_text("**لم يتم رفع حثالات بعد**")


zog =[]


@app.on_message(command("رفع زوجتي"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in zog:
    zog.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  مبرووكك قعدتي مراته {message.from_user.mention}😂♥️ \n خلفو دنقات**")


@app.on_message(command("ت زوجتي"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in zog:
    zog.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة المتزوجات 😂♥️**")


@app.on_message(command("المرفوعين متزوجات"))
async def nml(client, message):
  zzq = ""
  for n in hth:
      hq += n + "\n"
  await message.reply_text(hq)
  if not zog in zzq:
     await message.reply_text("**لم يتم رفع متزوجات بعد**")









