from pyrogram import *
from redis import Redis
import os

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

API_ID = "14676558"
API_HASH = "b3c4bc0ba6a4fc123f4d748a8cc39981"
TOKEN = "6911807700:AAH6ibUG_0YVJmULoZlioMIZyzRcUFTXWK4"

bot = Client('kotoko',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=TOKEN,
             plugins=dict(root=f"{__name__}/plugins"))

