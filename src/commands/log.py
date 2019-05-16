# coding: utf-8
import os
from discord import Client, Message
from .core import command

LOG_FILE_PATH = os.getenv('HOME') + '/discord-bot.log'

@command
def log(client: Client, message: Message, args: list) -> Message:
  # not implemented yet
  pass
