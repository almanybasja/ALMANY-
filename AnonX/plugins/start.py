import asyncio
import time
from pyrogram.types import *
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from pyrogram.enums import ChatType, ParseMode
import config
import requests

from pyrogram.errors import PeerIdInvalid
from config import (OWNER_ID ,
		     USER_OWNER,
	         MUSIC_BOT_NAME,
	         SUPPORT_CHANNEL,
	         BOT_TOKEN,
	         BANNED_USERS)
from strings import get_command, get_string
from AnonX import Telegram, YouTube, app
from AnonX.misc import SUDOERS, _boot_
from AnonX.plugins.playlist import del_plist_msg
from AnonX.plugins.sudoers import sudoers_list
from AnonX.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from AnonX.utils.decorators.language import LanguageStart
from AnonX.utils.formatters import get_readable_time
from AnonX.utils.inline import (help_pannel, private_panel,
                                     start_pannel)
import redis, re
from pyrogram.enums import ParseMode, ChatMemberStatus 
r = redis.Redis(
    host="127.0.0.1",
    port=6379,)

token = (BOT_TOKEN)
loop = asyncio.get_running_loop()
owner = (OWNER_ID) 
bot_id = token.split(":")[0]

@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            dev = (OWNER_ID)
          
		
            keyboard = help_pannel(_)
            Owneruser = ReplyKeyboardMarkup([
[("الاوامر"),("السورس")],[("المطور"),("مبرمج السورس"),("/مساعده")],
[("غنيلي"),("كت"),("صور")],
[("اذكار"),("مميزات"),("ذكاء اصتناعي")],
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)
  
					
            if message.from_user.id in dev:
		           
                   await message.reply(f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",reply_markup=OwnerM)
                        
 
            else:  
                   await message.reply_text(f"**اهلا عزيزي {message.from_user.mention}\n\n في بوت الميوزك {MUSIC_BOT_NAME} الخاص بي @{USER_OWNER} \n\n هذا بوت تشغيل اغاني وبه الكثير من المميزات الجميله \n\n ارفع البوت مشرف وهايرفعك مالك ويرفع المشرفين تلقائي**",reply_markup=Owneruser)
                   return await message.reply_photo(
                       photo=config.START_IMG_URL,
                       caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )

            

        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        
        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 يتم جلب الاحصائيات الخاصه لـ {config.MUSIC_BOT_NAME} sᴇʀᴠᴇʀ."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[قناة السورس](https://t.me/HL_BG) ** ᴩʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ضغط ستارت على البوت <code>دخل على قائمة المطورين</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name == "verify":
            await message.reply_text(f"ʜᴇʏ {message.from_user.first_name},\nشكرا لوثوقك في انا  {config.MUSIC_BOT_NAME}, تم تخزين بياناتك اللازمه يمكنك التشغيل الان")
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention}ضغط ستارت على البوت <code>تحقق من نفسه</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("دقيقه يقلبي وحانجيب البيانات")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
😲**جلب المعلومات**😲
 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼
📌 **العنوان:** {title}

⏳ **المده:** {duration} دقيقه
👀 **المشاهدات:** `{views}`
⏰ **نشرت في:** {published}
🎥 **القناه:** {channel}
📎 **رابط القناه:** [عرض القناه]({channellink})
🔗 **الرابط:** [مشاهده في اليوتيوب]({link})
 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼
💖 بحث بواسطة {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• ʏᴏᴜᴛᴜʙᴇ •", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="• قناة السورس •", url="https://t.me/HL_BG"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention}ضغط ستارت على البوت<code>جلب المعلومات</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                dev = (owner)

                Owneruser = ReplyKeyboardMarkup([
[("الاوامر"),("السورس")],[("المطور"),("مبرمج السورس"),("/مساعده")],
[("غنيلي"),("كت"),("صور")],
[("اذكار"),("مميزات"),("ذكاء اصتناعي")],
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)		    
            
                if message.from_user.id in dev:
                   await message.reply_text(f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",reply_markup=OwnerM)
                else:  
                   await message.reply_text(f"**اهلا عزيزي {message.from_user.mention}\n\n في بوت الميوزك {MUSIC_BOT_NAME} الخاص بي @{USER_OWNER} \n\n هذا بوت تشغيل اغاني وبه الكثير من المميزات الجميله \n\n ارفع البوت مشرف وهايرفعك مالك ويرفع المشرفين تلقائي**",reply_markup=Owneruser)
                   return await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )

            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ضغط ستارت في البوت.\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
            )
        

@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**بوت ميوزك خاص**\n\فقط الدردشات المصرح بها بواسطة المطور."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                OWNER = OWNER_ID[0]
                out = start_pannel(_, app.username, OWNER)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
OwnerM = ReplyKeyboardMarkup([
    [("اخفاء الكيبورد")],
    [("الاحصائيات")],
    [("تفعيل التواصل"), ("تعطيل التواصل")],
    [("• اوامر الاذاعة للخاص •")],
    [("اذاعة بالتثبيت"),("اذاعة"),("اذاعة بالتوجيه")],
    [("• اوامر الاذاعة بالجروبات •")],
    [("اذاعة بالمجموعات"),("اذاعة بالتثبيت بالمجموعات")],
    [("تفعيل الاشتراك"), ("تعطيل الاشتراك")],
    [("ضع قناة الاشتراك"),("حذف قناة الاشتراك")],
    [("قناة الاشتراك")],
    [("رفع ادمن"),("تنزيل ادمن")],
    [("قائمه الأدمنيه")],
    [("المستخدمين"),("الأدمنية"),("الجروبات")],
    [("نقل ملكية البوت")],
    [("الغاء")]
  ],
  resize_keyboard=True
)

def is_user(id):
	result = False
	file = open(f"Users{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def is_dev(id):
	result = False
	file = open(f"sudo{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def del_all_sudo():
	open(f"sudo{bot_id}.json","w")

def del_all_main():
	open(f"maindevs{bot_id}.json","w")

def del_all_mainVII():
	open(f"maindevsVII{bot_id}.json","w") 
	
def del_all_ban():
	open(f"band{bot_id}.json","w")

def is_main_dev(id):
	result = False
	file = open(f"maindevs{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_main_devVII(id):
	result = False
	file = open(f"maindevsVII{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_band(id):
	result = False
	file = open(f"band{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return  result
	
def is_group(id):
	result = False
	file = open(f"groups{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def add_user(id):
	file = open(f"Users{bot_id}.json","a")
	file.write("{}\n".format(id))

def show_channel() -> str:
	with open(f"channel{bot_id}.json","r") as file:
		return file.readline()

def add_channel(chat_id):
	with open(f"channel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_channel():
	open(f"channel{bot_id}.json","w")

def get_bot_owner() -> int:
	with open("owner{bot_id}.json","r") as file:
		return file.readline()
		
def set_bot_owner(user_id:int):
	with open(f"owner{bot_id}.json","w") as file:
		file.write(str(user_id))

def show_devchannel() -> str:
	with open(f"devchannel{bot_id}.json","r") as file:
		return file.readline()

def add_devchannel(chat_id):
	with open(f"devchannel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devchannel():
	open(f"devchannel{bot_id}.json","w")


def show_devuser() -> str:
	with open(f"devuser{bot_id}.json","r") as file:
		return file.readline()

def add_devuser(chat_id):
	with open(f"devuser{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devuser():
	open(f"devuser{bot_id}.json","w")



@app.on_message(
    filters.command(["start"])
    & filters.private
)
async def for_users (app,m:Message):
   if not check(m.from_user.id):
     await check_sub(app, m)
   if not is_user(m.from_user.id):
     add_user(m.from_user.id)
     text = '➕ شخص جديد دخل الى البوت !\n\n'
     text += f'👤 الأسم: {m.from_user.first_name}\n'
     text += f'🔗 رابط حسابه: {m.from_user.mention}\n'
     text += f'🆔 الايدي: {m.from_user.id}\n\n'
     text += f'🌀 اصبح عدد المستخدمين: {len(get_users())}'
     reply_markup=InlineKeyboardMarkup (
      [[
        InlineKeyboardButton (m.from_user.first_name, user_id=m.from_user.id)
      ]]
     )
     if len(get_admins()) > 0:
        list = get_admins()
        for admin in list:
          await app.send_message(int(admin), text, reply_markup=reply_markup)
        await app.send_message(int(r.get(f"bot_owner{bot_id}")), text, reply_markup=reply_markup)
     else:
        await app.send_message(int(r.get(f"bot_owner{bot_id}")), text, reply_markup=reply_markup)
     
        
     
   

admins_commands = [
   'الاحصائيات', 'تفعيل التواصل',
   'تعطيل التواصل', 'اذاعة بالتثبيت', 'اذاعة',
   'اذاعة بالتوجيه', 'تفعيل الاشتراك', 'تعطيل الاشتراك',
   'ضع قناة الاشتراك', 'حذف قناة الاشتراك', 'قناة الاشتراك','قائمه الأدمنيه',
   'المستخدمين', 'الأدمنية', 'الجروبات',
   'اذاعة بالمجموعات','اذاعة بالتثبيت بالمجموعات', 'اخفاء الكيبورد'
   ]
   
owner_commands = [
   'نقل ملكية البوت', 'رفع ادمن', 'تنزيل ادمن'
]

@app.on_message(filters.text & filters.private, group=2)
async def keyboard_for_admins(app, m):
  if m.text in admins_commands:
    if not check(m.from_user.id):
      return await m.reply('🌀 هذا الأمر لا يخصك', quote=True)
    else:
    
      if m.text == 'الاحصائيات':
        text = f'**👤 عدد المستخدمين: {len(get_users())}\n'
        text += f'📊 عدد المجموعات: {len(get_groups())}\n'
        text += f'🌀 عدد المشرفين: {len(get_admins())}**'
        await m.reply(text, quote=True)
        
      if m.text == 'تفعيل التواصل':
        if r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تفعيل التواصل مسبقاً", quote=True)
          
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل التواصل بنجاح**', quote=True)
        r.set(f'enable_twasol{bot_id}', 1)
      
      if m.text == 'تعطيل التواصل':
        if not r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تعطيل التواصل مسبقاً", quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل التواصل بنجاح**', quote=True)
        r.delete(f'enable_twasol{bot_id}')
      
      if m.text == 'المستخدمين':
        await m.reply_document(get_users_backup(), quote=True)
      
      if m.text == 'الأدمنية':
        await m.reply_document(get_admins_backup(), quote=True)
      
      if m.text == 'الجروبات':
        await m.reply_document(get_groups_backup(), quote=True)
      
      if m.text == 'تفعيل الاشتراك':
        if r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تفعيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل الاشتراك بنجاح**', quote=True) 
        r.set(f"enable_force_subscribe{bot_id}", 1)
      
      if m.text == 'تعطيل الاشتراك':
        if not r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تعطيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل الاشتراك بنجاح**', quote=True) 
        r.delete(f"enable_force_subscribe{bot_id}")
      
      if m.text == 'ضع قناة الاشتراك':
        await m.reply("• ارسل معرف القناة العام مثال @Y88F8", quote=True)
        r.set(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
      
      if m.text == 'حذف قناة الاشتراك':
        if not r.get(f'force_channel{bot_id}'):
          return await m.reply("• لا توجد قناة اشتراك معينة", quote=True)
        await m.reply("• تم حذف قناة الاشتراك بنجاح", quote=True)
        r.delete(f'force_channel{bot_id}')
      
      if m.text == 'قناة الاشتراك':
        if not r.get(f'force_channel{bot_id}'):
          await m.reply('• لاتوجد قناة مضافة', quote=True)
        else:
          channel = r.get(f'force_channel{bot_id}').decode('utf-8')
          await m.reply(f"https://t.me/{channel}", quote=True)
      
      if m.text == 'قائمه الأدمنيه':
        if len(get_admins()) == 0:
          await m.reply("• لايوجد آدمنية", quote=True)
        else:
          text = '• قائمة الأدمنية\n'
          for admin in get_admins():
            try:
              get = await app.get_chat(int(admin))
              text += f'• [{get.first_name}](tg://user?id={admin})\n'
            except:
              text += f'• [@Y88F8](tg://user?id={admin})\n'
          await m.reply(text, quote=True)
          
      if m.text == 'اذاعة':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اذاعة بالتثبيت':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
        
      if m.text == 'اذاعة بالتوجيه':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اذاعة بالمجموعات':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اذاعة بالتثبيت بالمجموعات':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اخفاء الكيبورد':
        await m.reply("• تم اخفاء لوحة التحكم لاظهارها مجدداً ارسل /start",
        quote=True, reply_markup=ReplyKeyboardRemove (selective=True))


@app.on_message(filters.text & filters.private, group=3)
async def for_owner(app,m):
  text = m.text
  if text in owner_commands:
   if not m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
      return await m.reply("• هذا الأمر يخص المطور الأساسي فقط", quote=True)
   
   if text == 'نقل ملكية البوت':
     await m.reply("• ارسل ايدي المالك الجديد الآن", quote=True)
     r.set(f"{m.from_user.id}transfer{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   if text == 'رفع ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   
   if text == 'تنزيل ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}", 1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")

@app.on_message(filters.text & filters.private, group=4)
async def response_for_commands(app,m):
   text = m.text
   
   if text in admins_commands:
     return

   if text in owner_commands:
     return 
     
   if check(m.from_user.id):
     if text == 'الغاء':
       await m.reply("• تم الغاء كل شيء", quote=True)
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       
     
     if r.get(f"{m.from_user.id}transfer{m.chat.id}{bot_id}"):
       try:
         get = await app.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       txt = '• تم نقل ملكية البوت بنجاح إلى :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       r.set(f"bot_owner{bot_id}", get.id)
       await m.reply(txt, quote=True)
       return
     
     if r.get(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}"):
       try:
         get = await app.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)
         
       if is_admin(int(text)):
         r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
         return await m.reply(f"• المستخدم [{get.first_name}]({get.id}) ادمن من قبل")
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       txt = '• تم رفع المستخدم ادمن بنجاح :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       add_admin(int(text))
       await m.reply(txt, quote=True)
       return 
     
     if r.get(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}"):
      try: 
       if not is_admin(int(text)):
         r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
         return await m.reply("• المستخدم مو ادمن من قبل")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       del_admin(int(text))
       await m.reply("• تم تنزيل المستخدم ادمن بنجاح", quote=True)
       return 
      except:
       return await m.reply("• الآيدي خطأ")
     
     if r.get(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}"):
       channel = text.replace("@","")
       r.set(f"force_channel{bot_id}", channel)
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       await m.reply("• تم تعيين القناة بنجاح ", quote=True)
       
     
     
@app.on_message(filters.regex("^المطور$"), group=5)
async def get_dev_about(app,m):
   id = int(r.get(f"bot_owner{bot_id}"))
   get = await app.get_chat(id)
   text = f'• Name -» [{get.first_name}](tg://user?id={get.id})\n'
   reply_markup= InlineKeyboardMarkup (
     [[
       InlineKeyboardButton (get.first_name, user_id=get.id)
     ]]
   )
   if get.bio:
     text += f'• Bio -» {get.bio}'
   if get.photo:
     async for photo in app.get_chat_photos(id, limit=1):
       await m.reply_photo(photo.file_id, caption=text, reply_markup=reply_markup,quote=True)
   
   else:
     await m.reply(text, quote=True, disable_web_page_preview=True,
     reply_markup=reply_markup)
       
@app.on_message(filters.new_chat_members, group=6)
async def add_group(app,m):
  get = await app.get_me()
  for mm in m.new_chat_members:
    if mm.id == get.id:
      if not is_group(m.chat.id):
        add_group(m.chat.id)
        text = '• تم اضافة البوت الى مجموعة جديدة\n'
        text += f'• اسم المجموعه: {m.chat.title}\n'
        if m.chat.username:
          text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الي ضافني :\n'
        text += f'• اسمه : {m.from_user.mention}\n'
        text += f'• الايدي : {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups())}'
        if len(get_admins()) > 0:
          list = get_admins()
          for admin in list:
            await app.send_message(int(admin), text,
            disable_web_page_preview=True)
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)
        else:
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)

@app.on_raw_update(group=7)
async def kick_from_group(app: Client, m: Update, _, __):
   try:
     name = re.search(r"first_name='([^']+)'", str(_)).group(1)
     title = re.search(r"title='([^']+)'", str(__)).group(1)
     if m.new_participant:
      get = await app.get_me()
      if m.new_participant.peer.user_id == get.id:
        print("🌀")
      else:  return 
      if m.new_participant.kicked_by:
        print("🌀")
      del_group(int(f'-100{m.channel_id}'))
      text = '• تم طرد البوت من مجموعة:\n\n'
      text += f'• اسم الي طردني : [{name}](tg://user?id={m.new_participant.kicked_by})\n'
      text += f'• ايدي الي طردني : {m.new_participant.kicked_by}\n'
      text += f'\n• معلومات المجموعة: \n'
      text += f'\n• ايدي المجموعة: `-100{m.channel_id}`'
      text += f'\n• اسم المجموعه: {title}'
      text += '\n• تم مسح جميع بيانات الجروب'
      if len(get_admins()) > 0:
          list = get_admins()
          for admin in list:
            await app.send_message(int(admin), text,
            disable_web_page_preview=True)
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)
      else:
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)
   except:
     pass
      

@app.on_message(filters.private, group=8)
async def forbroacasts(app,m):
   if m.text:
      if m.text in admins_commands:  return
      if m.text in owner_commands:  return 
   if m.from_user:
     if r.get(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            await m.copy(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            a = await m.copy(int(user))
            await a.pin(disable_notification=False,both_sides=True)
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception as e:
            print(e)
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            await m.forward(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups():
          try:
            await m.copy(int(group))
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
       
     
     if r.get(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups():
          try:
            a = await m.copy(int(group))
            await a.pin(disable_notification=False)
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")

@app.on_message(filters.private, group=9)
async def twasol__(app,m):
   if not check(m.from_user.id):
     if r.get(f'enable_twasol{bot_id}'):
       await m.forward(int(r.get(f"bot_owner{bot_id}")))
   
   if m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
      if m.reply_to_message:
        if m.reply_to_message.forward_from:
          await m.reply(f"• تم إرسال رسالتك إلى {m.reply_to_message.forward_from.first_name} بنجاح", quote=True)
          try:
            await m.copy(m.reply_to_message.forward_from.id)
          except:
            pass
      

@app.on_message(filters.text & filters.group , group=10)
async def for_admins_in_group(app,m):
   if not m.reply_to_message:
      return
   if not m.reply_to_message.from_user:
      return
      
   if m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
     text = m.text
     user_id = m.reply_to_message.from_user.id
     if text == 'رفع ادمن':
       if is_admin(user_id):
          return await m.reply("• المستخدم آدمن من قبل")
       else:
          add_admin(user_id)
          await m.reply("• تم رفعه ادمن بنجاح")
     
     if text == 'تنزيل ادمن':
      if not is_admin(user_id):
          return await m.reply("• المستخدم مو آدمن من قبل")
      else:
          del_admin(user_id)
          await m.reply("• تم تنزيله ادمن بنجاح")

def add_user(user_id: int):
	if is_user(user_id):
		return
	r.sadd(f"botusers{bot_id}", user_id)
	
def is_user(user_id: int):
  try:
    a= get_users()
    if user_id in a:
      return True
    return False
  except:
    return False

def del_user(user_id: int):
	if not is_user(user_id):
		return False
	r.srem(f"botusers{bot_id}", user_id)
	return True

def get_users():
   try:
     list = []
     for a in r.smembers(f"botusers{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_users_backup() -> str:
	text = ''
	for user in r.smembers(f"botusers{bot_id}"):
		text += user.decode('utf-8')+'\n'
	with open('users.txt', 'w+') as f:
		f.write(text)
	return 'users.txt'
	
def add_admin(user_id: int):
    if is_admin(user_id):  return 
    r.sadd(f"botadmins{bot_id}", user_id)

def is_admin(user_id: int):
  try:
    a = get_admins()
    if user_id in a:
      return True
    return False
  except:
    return False

def del_admin(user_id: int):
	if not is_admin(user_id):
		return False
	r.srem(f"botadmins{bot_id}", user_id)
	
def get_admins():
   try:
     list = []
     for a in r.smembers(f"botadmins{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_admins_backup() -> str:
	text = ''
	for admin in r.smembers(f"botadmins{bot_id}"):
		text += admin.decode('utf-8')+'\n'
	with open('admins.txt', 'w+') as f:
		f.write(text)
	return 'admins.txt'
	

def check(id):
    if is_admin(id):
      return True
    if id == int(r.get(f"bot_owner{bot_id}")):
      return True
    else:
      return False

async def check_sub(c,m):
    if not r.get(f"enable_force_subscribe{bot_id}"):
      return
    else:
      if not r.get(f"force_channel{bot_id}"):
        return 
      else:
        channel = r.get(f"force_channel{bot_id}").decode('utf-8')
        text = f'✖️ عذراً عليك الاشتراك بقناة البوت أولاً لتتمكن من استخدامه !\n\nhttps://t.me/{channel}\n- /start'
        try:
           get = await c.get_chat_member(r.get(f"force_channel{bot_id}").decode('utf-8'), m.from_user.id)
           if get.status in [ChatMemberStatus.LEFT, ChatMemberStatus.BANNED]:
             return await m.reply(text, quote=True, disable_web_page_preview=True)
        except:
           return await m.reply(text, quote=True, disable_web_page_preview=True)

def add_group(chat_id: int):
    if is_group(chat_id):  return 
    r.sadd(f"botgroups{bot_id}", chat_id)

def is_group(chat_id: int):
  try:
    a = get_groups()
    if chat_id in a:
      return True 
    return False 
  except:
    return False

def del_group(chat_id: int):
	if not is_group(chat_id):
		return False
	r.srem(f"botgroups{bot_id}", chat_id)

def get_groups():
   try:
     list = []
     for a in r.smembers(f"botgroups{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_groups_backup() -> str:
	text = ''
	for group in r.smembers(f"botgroups{bot_id}"):
		text += group.decode('utf-8')+'\n'
	with open('groups.txt', 'w+') as f:
		f.write(text)
	return 'groups.txt'

if not r.get(f"bot_owner{bot_id}"):
      owner = (owner)
      r.set(f"bot_owner{bot_id}", owner)
   
