# coding: utf-8
import datetime
from discord import Client, Message
from .core import command
from .log import write_to_log_file

@command
def ping(client: Client, message: Message, args: list) -> Message:
    now = datetime.datetime.now()
    write_to_log_file('[{0}] Command PING called by {1.author.name}'.format(now, message))
    msg = "pong {0.author.mention}".format(message)
    return client.send_message(message.channel, msg)
