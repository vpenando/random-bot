# coding: utf-8
from discord import Client, Message
from .core import command, commands
from .log import write_to_log_file

@command
def help(client: Client, message: Message, args: list) -> Message:
    write_to_log_file('Command HELP called by {}'.format(message.author.name))
    available_commands = "\n".join(map(lambda s: " - *!%s*" % s, commands))
    msg = "Available commands:\n%s" % available_commands
    return client.send_message(message.channel, msg)
