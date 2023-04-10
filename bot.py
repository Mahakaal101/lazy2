import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6257817586:AAHiHfYz_Ykn_n1QHgE7o1aRdOn5Gxg6M4U")

API_ID = int(os.environ.get("API_ID", "26305247"))

API_HASH = os.environ.get("API_HASH", "20ca7e6687c281e11782856c7efd0ff7")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
