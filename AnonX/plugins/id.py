##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]

import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus

#       #             #  #####  #####      ####
#        #  كود الرتبه الوهميه برمجة ##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]         #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #

import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus 

iddof = []

@app.on_message(
     command(["قفل الرفع","تعطيل الرفع"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    haya = (6275847466,6195765774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوس"
    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن" 
    
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")    
     
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"يا {message.from_user.mention}\n الرفع مقفله من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الرفع بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")

@app.on_message(
    command(["فتح الرفع","تفعيل الرفع"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (6275847466,6195765774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي" 
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")       
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\الرفع معفل من قبل**")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم فتح امر الرفع بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 
   




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

zoj = []


@app.on_message(command("رفع زوجي"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in zoj:
    zoj.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  زوج لـ {message.from_user.mention}😂♥️")


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

hth =[]


@app.on_message(command("رفع حثاله"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in hth:
    hth.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  حثاله من قبل {message.from_user.mention}😂♥️")


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






@app.on_message(
    command(["id","ايدي","ا"])
    & filters.group
)

async def iddd(client, message):# البريميوم الوهمي كتابة ##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
    txt = ["مــلآگ ونآزل مــن آلســمــآ♥️🥺","وويليييي يااا طرف انتتتتتت","مافيككشش جوو","نععليييي منككككك",]
    xtxk = random.choice(txt)
    botdev= (OWNER_ID)
    haya = (6275847466,6195765774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
    elif message.from_user.id in botdev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــــن"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    else: 
        rotba= "عضو جميل"
    
    if message.from_user.id in haya:
       prim= "بريميوم لفل ماكس"
    elif message.from_user.id in botdev:
       prim = "بريميوم"
    else: 
       prim= "عادي"
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""**✧ ¦ {xtxk}\n\n✧ ¦ آســمــڪ ← {message.from_user.mention}\n✧ ¦ يـوزرڪ ← @{message.from_user.username}\n✧ ¦ آيـديــڪ ← `{message.from_user.id}`\n✧ ¦ بـآيـو ← {usr.bio}\n✧ ¦ ࢪتبـتڪ ← {rotba} \n✧ ¦ نوع الحساب ← {prim}**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/openmessage?user_id")
                ],
            ]
        ),
    )

iddof = []
@app.on_message(
    command(["قفل صورتي","تعطيل صورتي"])
    & filters.group
)
async def lllock(client, message):
    dev = (OWNER_ID)
    haya = (6275847466,6195765774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي" 
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\n صورتي مقفلها من قبل**")
      iddof.append(message.chat.id)
      return await message.reply_text(f"**تم قفل امر صورتي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")

@app.on_message(
    command(["فتح صورتي","تفعيل صورتي"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (6275847466,6195765774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي" 
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"يا {message.from_user.mention} صورتي مقفلها من قبل")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم تفعيل امر صورتي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 



@app.on_message(
    command(["صورتي"])
    & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا طرف انت \n│ \n└ʙʏ: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
@app.on_message(
    command(["رتبتي"])
    & filters.group
)
async def rotba(client, message:Message):
    dev = (OWNER_ID)
    haya = (6275847466,6195765774)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
    else:
         rotba = "عضــو جميل"
    if message.chat.id in iddof:
      return
    await message.reply_text(f"**رتبتك في هذه المجموعه \nهي ← «{rotba}»**")
       
