# coding: utf-8
from discord import Client, Message
from .core import command

@command
def ping(client: Client, message: Message, args: list) -> Message:
    print('Command PING called by {0.author.mention}').format(message)
    msg = "pong {0.author.mention}".format(message)
    return client.send_message(message.channel, msg)
