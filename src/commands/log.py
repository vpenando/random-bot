# coding: utf-8
import os
from discord import Client, Message
from .core import command

LOG_FILE_PATH = os.getenv('HOME') + '/discord-bot.log'

def write_to_log_file(msg: str) -> None:
    try:
        with open(LOG_FILE_PATH, 'a+') as f:
            f.write('%s\n' % msg)
    except:
        pass

@command
def log(client: Client, message: Message, args: list) -> Message:
  # not implemented yet
  pass
