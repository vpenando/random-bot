# coding: utf-8
import datetime
from discord import Client, Message
from .core import command

@command
def ping(client: Client, message: Message, args: list) -> Message:
    now = datetime.datetime.now()
    print('[{}] Command PING called by {1.author.name}'.format(now, message))
    msg = "pong {0.author.mention}".format(message)
    return client.send_message(message.channel, msg)
