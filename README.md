``` python

import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from sankihub import sankihub as papaSANKIXD
from SANKIXD import app

@app.on_message(filters.command("sankihub"))
async def sankihub(_, message):
    text = message.text[len("/sankihub") :]
    papaSANKIXD(f"{text}").save(f"sankihub_{message.from_user.id}.png")
    await message.reply_photo(f"sankihub_{message.from_user.id}.png")
    os.remove(f"sankihub_{message.from_user.id}.png")

```
``` python
 pip install sankihub

```




# sankihub 


![Project Image](https://github.com/SANKIXDTEAM/sankihub/blob/main/out.png)

