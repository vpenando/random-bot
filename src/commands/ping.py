# coding: utf-8
from discord import Client, Message
from .core import command
from .log import write_to_log_file

@command
def ping(client: Client, message: Message, args: list) -> Message:
    write_to_log_file('Command PING called by {}'.format(message.author.name))
    msg = "pong {0.author.mention}".format(message)
    return client.send_message(message.channel, msg)
