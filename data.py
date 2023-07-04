from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Support", url="https://t.me/SharingUserbot"),
         InlineKeyboardButton("Owner", url="https://t.me/Ammuyeee"),
        ],
    ]

    START = """
**Hey** {},

**This is** {},
**Bot untuk Mengambil String Session!**

**Made With By:** [Piki](https://t.me/Ammuyeee)
    """
