# coding: utf-8
import os
import datetime
from discord import Client, Message
from .core import command

LOG_FILE_PATH = os.getenv('HOME') + '/discord-bot.log'

def write_to_log_file(message: str) -> None:
    try:
        now = datetime.datetime.now()
        message = '[{0}] {1}\n'.format(now, message)
        with open(LOG_FILE_PATH, 'a+') as f:
            f.write(message)
    except:
        pass

@command
def log(client: Client, message: Message, args: list) -> Message:
  # not implemented yet
  pass
