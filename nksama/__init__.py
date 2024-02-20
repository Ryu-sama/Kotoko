from pyrogram import filters, Client
from redis import Redis
import os
from pyrogram import *

help_message = []

# class bot(Client):
#     super().__init__(
#         'bot',
#                      api_id=os.environ.get('API_ID'),
#                      api_hash=os.environ['API_HASH'],
#                      bot_token=os.environ['BOT_TOKEN'],
#                      plugins=dict(root=f"{__name__}/plugins"))

#     def add_cmd(module, help):
#         help_message.append({"Module_Name": module})
#         help.update({f"{module}_help": help})



bot = Client(
    'Slave',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
bot.start()
