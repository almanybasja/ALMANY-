import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #

iddof = []

@app.on_message(
     command(["قفل ايدي","تعطيل ايدي"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"يا {message.from_user.mention} الايدي مقفله من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الايدي \n\n من قبل ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")

@app.on_message(
    command(["فتح الايدي","تفعيل الايدي"])
     & filters.group
   
   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in iddof:
           return await message.reply_text(f"**تم فتح الايدي \n\n من قبل ←{message.from_user.mention}**")
        iddof.remove(message.chat.id)
    return await message.reply_text(f"يا {message.from_user.mention} الايدي فاتحه من قبل")
    
   



@app.on_message(
    command(["id","ايدي","ا"])
    & filters.group
)

async def iddd(client, message):
    txt = ["مــلآگ ونآزل مــن آلســمــآ♥️🥺","وويليييي يااا طرف انتتتتتت","مافيككشش جوو","نععليييي منككككك",]
    xtxk = random.choice(txt)
    botdev= (OWNER_ID)
    haya = (6275847466,6195765774)
    if message.from_user.id in haya:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
    elif message.from_user.id in botdev:
        rotba = "مطور اساسي"
    else: 
       rotba= "عضو"
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""{xtxk}\n✧ ¦آســمــگڪ :{message.from_user.mention}\n✧ ¦يـوزرڪ :@{message.from_user.username}\n✧ ¦آيـديــڪ :`{message.from_user.id}`\n✧ ¦بـآيـو :{usr.bio}\n✧ ¦ࢪتبتگ: {rotba}""",
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
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"**تم قفل امر صورتي \n\n من قبل ←{message.from_user.mention}**")
      iddof.append(message.chat.id)
    return await message.reply_text(f"يا {message.from_user.mention} صورتي مقفلها من قبل")

@app.on_message(
    command(["فتح صورتي","تفعيل صورتي"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"**تم قفل امر صورتي \n\n من قبل ←{message.from_user.mention}**")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"يا {message.from_user.mention} صورتي مقفلها من قبل")
 



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
       

