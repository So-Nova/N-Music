"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""⌯ مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})\n
⌯ انا بوت نوفا ميوزك لتشغيل الاغاني في المجموعات

⌯ Ch : [Source Nova](http://t.me/TmNova)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اضفني الي مجموعتك", url=f"https://t.me/{me_bot.username}?startgroup=true")
                ],[
                    InlineKeyboardButton("طريقه التشغيل", callback_data="user_guide")
                ],[
                    InlineKeyboardButton("اوامر البوت", callback_data="command_list"),
                    InlineKeyboardButton("مطور البوت", url=f"https://t.me/{OWNER_USERNAME}")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""⌯ طريقه التشغيل

⌯ أولا ، أضفني الى مجموعتك
⌯ بعد ذالك قم برفعي مشرف واعطائي صلاحيات زي بقيت البشر
⌯ بعد ذالك اكتب ( تحديث ) لتحديث ملفات البوت
⌯ لدعوه الحساب  المساعد اكتب ( انضم ) 
⌯ اذ لم تستطيع اضافة المساعد تحدث مع مطور البوت 

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("رجوع", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("command_list")
    await query.edit_message_text(
        f"""
⌯ اهلا بك انت الان في قائمه الاوامر 
⌯ لـ استخدام الاوامر عليك التحكم بالقائمه بالاسفل ↡
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر البوت", callback_data="user_command"),
                ],[             
                    InlineKeyboardButton("رجوع", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    await query.answer("user_command")
    await query.edit_message_text(
        f"""⌯ تابع الاوامر في الاسفل ↡

⌯ ( شغل ) بالرد على ملف صوتي 
⌯ ( اطلع ) لفتح المكالمه الصوتيه
⌯ ( انزل ) لقفل المكالمه الصوتيه
⌯ ( تخطي ) لتخطي الاغنيه الحاليا
⌯ ( انهاء ) لايقاف تشغيل جميع الاغاني
⌯ ( اسكت ) لايقاف الاغنيه مؤقت
⌯ ( كمل ) لتشغيل الاغنيه الي وقفه
⌯ ( الصوت ) لضبط صوت حساب المساعد
⌯ ( فيد ) بالرد على مقطع فيديو 
⌯ ( الانتظار ) لرؤية قائمة الانتضار التشغيل
⌯ ( فيديو ) لبحث عن فيديو من اليوتيوب
⌯ ( بحث ) لتحميل اغنية من اليوتيوب
⌯ ( كتم ) لكتم صوت المساعد
⌯ ( بنج ) لإضهار سرعه البوت
⌯ ( انضم ) لدعوه حساب المساعد
⌯ ( غادر  ) لمغادره الحساب المساعد

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("رجوع", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⌯ بطل تبعبص بقا يعم انت ، محدش يقدر يدوس هنا غير الي معه رول", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("⌯ تم فتح لوحة التحكم")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("⌯ مفيش حاجه شغله اصلا ...", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⌯ بطل تبعبص بقا يعم انت ، محدش يقدر يدوس هنا غير الي معه رول", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⌯ بطل تبعبص بقا يعم انت ، محدش يقدر يدوس هنا غير الي معه رول", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
