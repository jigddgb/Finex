from pyrogram.types import Message
from pyrogram import Client, filters

from env import OWNER_ID
from StringGenBot.db import SESSION
from StringGenBot.db.users_sql import Users, num_users


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    await msg.reply(f"😎 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝚂𝚃𝙰𝚃𝙸𝙲𝚂  𝙾𝙵 𝚂𝚃𝚁𝙸𝙽𝙶 𝙼𝙰𝙺𝙴𝚁 𝙱𝙾𝚃 :\n\n {users} 𝚄𝚂𝙴𝚁𝚂 😎", quote=True)
