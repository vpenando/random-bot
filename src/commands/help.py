# coding: utf-8
from discord import Client, Message
from .core import command, commands

@command("help")
def help(client: Client, message: Message, args: list) -> Message:
    available_commands = "\n".join(map(lambda s: " - *!%s*" % s, commands))
    msg = "Available commands:\n%s" % available_commands
    return client.send_message(message.channel, msg)
