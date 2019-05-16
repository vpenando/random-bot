# coding: utf-8
import datetime
from discord import Client, Message
from .core import command, commands
from .log import write_to_log_file

@command
def help(client: Client, message: Message, args: list) -> Message:
    now = datetime.datetime.now()
    write_to_log_file('[{0}] Command HELP called by {1.author.name}'.format(now, message))
    available_commands = "\n".join(map(lambda s: " - *!%s*" % s, commands))
    msg = "Available commands:\n%s" % available_commands
    return client.send_message(message.channel, msg)
