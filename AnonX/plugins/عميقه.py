
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
    command(["قفل الاقتباسات","تعطيل الاقتباسات"])
    & filters.group
)
async def lllock(client, message):
    dev = (OWNER_ID)
    haya = (6275847466)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\n الاقتباسات مقفلها من قبل**")
      iddof.append(message.chat.id)
      return await message.reply_text(f"**تم قفل امر الاقتباسات بالمنشن بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")

@app.on_message(
    command(["فتح الاقتباسات","تفعيل الاقتباسات"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (6275847466)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
    
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"يا {message.from_user.mention}\n الاقتباسات مقفلها من قبل")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم تفعيل الاقتباسات بالمنشن بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 



@app.on_message(
    command(["ق","اقتباس"])
    & filters.group
)
async def idjjdd(client, message):

    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    i =     random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
         f"- لـ{random_member_mention}\n يجب أن تحاول ثلاث مرات قبل اليأس ",
         f"- لـ{random_member_mention}\n أ عطي كل يوم فرصة لتصبح أفضل يوم في حياتك",
         f"- لـ{random_member_mention}\n لحكمة هي معرفة متى تتجاهل ",
         f"- لـ{random_member_mention}\n الصبر هو المفتاح إلى كلَّ قفل غامض ",
         f"- لـ{random_member_mention}\n أنت مسؤول عن ماتشعر به، ولكنك لست مسؤولًا عن ما يفعله الآخرون ",
         f"- لـ{random_member_mention}\n حكمتي تقول: دع الغضب يقتلع من قلبك السعادة كما تقتل الفحم النار من طريقه ",
         f"- لـ{random_member_mention}\n إذا لم تكن تعيش بالطريقة التي تريدها، يجب عليك أن تغيرها ",
         f"- لـ{random_member_mention}\n الفائزون لا يقومون بممارسة الأسرار. إنهم يتوجهون نحو الأهداف الكبيرة ",
         f"- لـ{random_member_mention}\n ليس هناك شيء أفضل في الحياة من أن تكون في حالة حب وسعادة ",
         f"- لـ{random_member_mention}\n عندما يتغير الريح، يجب علينا أن نعدل اتجاه الشراع بدلاً من أن نتوقف عن السفر ",
         f"- لـ{random_member_mention}\n الحياة مثل الموج عليك فقط أن تجد توازنك حتى لا تسقط",
         f"- لـ{random_member_mention}\n ا لعلم يجري كالماء، ولا يتوقف أبدًا - لا على الجدران ولا على السور، لكنه يصب في نهاية المطاف في ثنايا الإنسان",
         f"- لـ{random_member_mention}\n الشجرة التي لا تنحني عند الريح، هي التي تتحطم في الاعاصير ",
         f"- لـ{random_member_mention}\n امنيتي ان يكون فيها زوايا خطرة ، فلا شي يمكن ان ينمي من دون التحدي ",
         f"- لـ{random_member_mention}\n لا يمكنك تجاهل الظلام. يجب أن تنشئ شمعة ",
         f"- لـ{random_member_mention}\n إن للبُعدِ طعمً يُصدِرُه الألمْ، ولكنَّ مِن يُجيد العِشقَ يجفَل الأميال ",
         f"- لـ{random_member_mention}\n المرء لا يتشكل على أساس المواقف التي يمر بها بل على أساس الردود التي يمنحها لتلك المواقف ",
         f"- لـ{random_member_mention}\n أن تختار، في النهاية، طريقًا واحدًا، لم يكن في صالحك أن تترك طرقاً أخرى غير مستكشفة ",
         f"- لـ{random_member_mention}\n إن لم يكن عندك شيء جيد ليقال، فابقَ صامتًا",
         f"- لـ{random_member_mention}\n النجاح هو القدرة على الذهاب من فشل إلى فشل بدون فقد أرزاقك الحماس ", 
    ])

    ik = random.choice(i)
    await message.reply_text(f"**اليــك اقتبــاس اليــم ❤️\n│ \n└ʙʏ: {ik}**")
