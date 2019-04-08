# coding: utf-8
from discord import Client, Message
from .command import command

@command("ping")
def ping(client: Client, message: Message, args: list) -> Message:
    msg = "pong {0.author.mention}".format(message)
    return client.send_message(message.channel, msg)
