from typing import Union
import random
from AnonX import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import redis, re
from config import OWNER_ID
from pyrogram.errors import PeerIdInvalid
dev = (OWNER_ID)
def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="**الـاوامر**",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="**الـاوامر**", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="لتنصيب بوت", url=f"https://t.me/bp_bp"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼", url=f"https://t.me/HL_BG"
            )
        ],
      
     ]

r = redis.from_url('redis://')

Keyboard = InlineKeyboardMarkup(
  [
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
 
)

@app.on_message(command("start") & filters.private)
async def for_users (app,m):
   if m.from_user.id not in dev:
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
        await app.send_message(int(r.get(f"bot_owner{OWNER_ID}")), text, reply_markup=reply_markup)
     else:
        await app.send_message(int(r.get(f"bot_owner{OWNER_ID}")), text, reply_markup=reply_markup)
     
        
     
   
@app.on_message(command("start") & filters.private, group=1)
async def keyboard_show(app,m):
    if m.from_user.id in dev:
       await m.reply(f"• أهلا بك {m.from_user.mention} .\n• اليك لوحة التحكم الخاصة", reply_markup=Keyboard, quote=True)

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
        if r.get(f'enable_twasol{OWNER_ID}'):
          return await m.reply("• تم تفعيل التواصل مسبقاً", quote=True)
          
        await m.reply(f'• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل التواصل بنجاح', quote=True)
        r.set(f'enable_twasol{OWNER_ID}', 1)
      
      if m.text == 'تعطيل التواصل':
        if not r.get(f'enable_twasol{OWNER_ID}'):
          return await m.reply("• تم تعطيل التواصل مسبقاً", quote=True)
        await m.reply(f'• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل التواصل بنجاح', quote=True)
        r.delete(f'enable_twasol{OWNER_ID}')
      
      if m.text == 'المستخدمين':
        await m.reply_document(get_users_backup(), quote=True)
      
      if m.text == 'الأدمنية':
        await m.reply_document(get_admins_backup(), quote=True)
      
      if m.text == 'الجروبات':
        await m.reply_document(get_groups_backup(), quote=True)
      
      if m.text == 'تفعيل الاشتراك':


        if r.get(f"enable_force_subscribe{OWNER_ID}"):
          return await m.reply('• تم تفعيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل الاشتراك بنجاح', quote=True) 
        r.set(f"enable_force_subscribe{OWNER_ID}", 1)
      
      if m.text == 'تعطيل الاشتراك':
        if not r.get(f"enable_force_subscribe{OWNER_ID}"):
          return await m.reply('• تم تعطيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل الاشتراك بنجاح', quote=True) 
        r.delete(f"enable_force_subscribe{OWNER_ID}")
      
      if m.text == 'ضع قناة الاشتراك':
        await m.reply("• ارسل معرف القناة العام مثال @Y88F8", quote=True)
        r.set(f"{m.from_user.id}addchannel{m.chat.id}{OWNER_ID}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{OWNER_ID}")
      
      if m.text == 'حذف قناة الاشتراك':
        if not r.get(f'force_channel{OWNER_ID}'):
          return await m.reply("• لا توجد قناة اشتراك معينة", quote=True)
        await m.reply("• تم حذف قناة الاشتراك بنجاح", quote=True)
        r.delete(f'force_channel{OWNER_ID}')
      
      if m.text == 'قناة الاشتراك':
        if not r.get(f'force_channel{OWNER_ID}'):
          await m.reply('• لاتوجد قناة مضافة', quote=True)
        else:
          channel = r.get(f'force_channel{OWNER_ID}').decode('utf-8')
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
        r.set(f"{m.from_user.id}broadcast{m.chat.id}{OWNER_ID}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{OWNER_ID}")
      
      if m.text == 'اذاعة بالتثبيت':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastpin{m.chat.id}{OWNER_ID}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{OWNER_ID}")


        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{OWNER_ID}")
        
      if m.text == 'اذاعة بالتوجيه':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastfor{m.chat.id}{OWNER_ID}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{OWNER_ID}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{OWNER_ID}")
     
    
    return buttons
