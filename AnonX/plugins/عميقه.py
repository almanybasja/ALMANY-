import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID, MUSIC_BOT_NAME
from pyrogram import filters

txt = [
f"- لـ{ message.from_user.mention} يجب أن تحاول ثلاث مرات قبل اليأس",
  f"- لـ{ message.from_user.mention} أعطي كل يوم فرصة لتصبح أفضل يوم في حياتك",
  f"- لـ{ message.from_user.mention} لحكمة هي معرفة متى تتجاهل",
  f"- لـ{ message.from_user.mention} الصبر هو المفتاح إلى كلَّ قفل غامض",
  f"- لـ{ message.from_user.mention} أنت مسؤول عن ماتشعر به، ولكنك لست مسؤولًا عن ما يفعله الآخرون",
  f"- لـ{ message.from_user.mention} حكمتي تقول: دع الغضب يقتلع من قلبك السعادة كما تقتل الفحم النار من طريقه",
  f"- لـ{ message.from_user.mention} إذا لم تكن تعيش بالطريقة التي تريدها، يجب عليك أن تغيرها",
  f"- لـ{ message.from_user.mention} الفائزون لا يقومون بممارسة الأسرار. إنهم يتوجهون نحو الأهداف الكبيرة",
  f"- لـ{ message.from_user.mention} ليس هناك شيء أفضل في الحياة من أن تكون في حالة حب وسعادة",
  f"- لـ{ message.from_user.mention} عندما يتغير الريح، يجب علينا أن نعدل اتجاه الشراع بدلاً من أن نتوقف عن السفر",
  f"- لـ{ message.from_user.mention} الحياة مثل الموج عليك فقط أن تجد توازنك حتى لا تسقط",
  f"- لـ{ message.from_user.mention} العلم يجري كالماء، ولا يتوقف أبدًا - لا على الجدران ولا على السور، لكنه يصب في نهاية المطاف في ثنايا الإنسان",
  f"- لـ{ message.from_user.mention} الشجرة التي لا تنحني عند الريح، هي التي تتحطم في الاعاصير",
  f"- لـ{ message.from_user.mention} امنيتي ان يكون فيها زوايا خطرة ، فلا شي يمكن ان ينمي من دون التحدي",
  f"- لـ{ message.from_user.mention} لا يمكنك تجاهل الظلام. يجب أن تنشئ شمعة",
  f"- لـ{ message.from_user.mention} إن للبُعدِ طعمً يُصدِرُه الألمْ، ولكنَّ مِن يُجيد العِشقَ يجفَل الأميال",
  f"- لـ{ message.from_user.mention} المرء لا يتشكل على أساس المواقف التي يمر بها بل على أساس الردود التي يمنحها لتلك المواقف",
  f"- لـ{ message.from_user.mention} أن تختار، في النهاية، طريقًا واحدًا، لم يكن في صالحك أن تترك طرقاً أخرى غير مستكشفة",
  f"- لـ{ message.from_user.mention} إن لم يكن عندك شيء جيد ليقال، فابقَ صامتًا",
  f"- لـ{ message.from_user.mention} النجاح هو القدرة على الذهاب من فشل إلى فشل بدون فقد أرزاقك الحماس",  
        ]


        


@app.on_message(command(["اقتباس","ق","اق","س]))


async def cutt(client: Client, message: Message):
 

         b = random.choice(txt)


         await message.reply(


         f"{b}")
   
