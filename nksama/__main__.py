from nksama import bot
import logging
from pyrogram import *

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)
idle()



