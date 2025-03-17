import math
import random
from pyrogram.types import InlineKeyboardButton
import config
from AnieXEricaMusic.utils.formatters import time_to_seconds
from AnieXEricaMusic import app

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons



def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        return "▰▱▱▱▱▱▱▱▱"
    elif 10 < umm <= 20:
        return "▰▰▱▱▱▱▱▱▱"
    elif 20 < umm <= 30:
        return "▰▰▰▱▱▱▱▱▱"
    elif 30 < umm <= 40:
        return "▰▰▰▰▱▱▱▱▱"
    elif 40 < umm <= 50:
        return "▰▰▰▰▰▱▱▱▱"
    elif 50 < umm <= 60:
        return "▰▰▰▰▰▰▱▱▱"
    elif 60 < umm <= 70:
        return "▰▰▰▰▰▰▰▱▱"
    elif 70 < umm <= 80:
        return "▰▰▰▰▰▰▰▰▱"
    elif 80 < umm <= 90:
        return "▰▰▰▰▰▰▰▰▰"
    elif 90 < umm <= 100:
        return "▰▰▰▰▰▰▰▰▰▰"
    else:
        return "▰▰▰▰▰▰▰▰▰▰"

def get_progress_bar2(percentage):
    umm = math.floor(percentage)
    
    progress_messages = [
        "  ✦ sᴘᴏᴛɪғʏ ᴘʀᴏɢʀᴇss ✦ ",
        "  🎶 ᴛʜɪs sᴏɴɢ ɪs ᴠᴇʀʏ ʙᴇᴀᴜᴛɪғᴜʟ 🎶 ",
        "  💿 ᴍᴇʟᴏᴅʏ ғʟᴏᴡs ᴛʜʀᴏᴜɢʜ 🎙️ ",
        "  🎧 ᴘʟᴀʏɪɴɢ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ 🎥 ",
        "  ✨ ᴛʜᴇ ᴠɪʙᴇs ᴀʀᴇ ʀᴇᴀʟ ✨ ",
        "  ⚕️ ᴇɴᴊᴏʏ ᴛʜᴇ sᴏᴜɴᴅs ⚕️ ",
        "  ✩ ʏᴏᴜʀ ᴍᴜsɪᴄ sᴇssɪᴏɴ ✩ ",
        "  ❤️ ғᴇᴇʟɪɴɢ ᴛʜᴇ ʙᴇᴀᴛs ❤️ ",
        "  🎧 ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ sᴘᴏᴛɪғʏ ᴍᴜsɪᴄ 🎧 ",
        "  ✩ ᴀʟᴍᴏsᴛ ᴅᴏɴᴇ ᴘʟᴀʏɪɴɢ ✩ ",
    ]
    
    if umm < 100:
        index = umm // 10
        return progress_messages[index % len(progress_messages)]
    else:
        return "𓆩🎵𓆪  ꜱοиg ɪѕ ᴀϐουτ ᴛο ᴇи∂ 𓆩🎶𓆪"

    buttons = [
        [
         InlineKeyboardButton(text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true",)
        ],
         [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
         InlineKeyboardButton(text="ᴇɴᴅ 🍁", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
         InlineKeyboardButton(text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true",)
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
         InlineKeyboardButton(text="ᴇɴᴅ 🍁", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AMBOTPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AMBOTPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
