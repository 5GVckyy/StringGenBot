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
**Halo** {},
━━━━━━━━━━━━━━━━━━━━━━━━
{} di buat untuk Membantu anda Untuk Mengambil String Session Telegram dengan Mudah dan AMAN
━━━━━━━━━━━━━━━━━━━━━━━━
Jika anda Tidak Mempercayai Bot ini:
1. Jangan dibaca Pesan ini
2. Hapus Pesan dan Blokir Bot ini
━━━━━━━━━━━━━━━━━━━━━━━━
**Managed With By:** @Ammuyeee
    """
