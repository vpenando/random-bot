#!/usr/bin/env python3
# coding: utf-8
import datetime
import sys
from discord import Client, Message
from commands import commands, log

client = Client()

def error(message: Message) -> Message:
    err_msg = "Error: invalid command '%s'" % message.content
    return client.send_message(message.channel, err_msg)

@client.event
async def on_message(message: Message) -> None:
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # we only accept commands starting with '!'
    if message.content[0] != "!":
        return
    cmd_with_args = message.content.split(" ")
    cmd = cmd_with_args[0][1:]
    args = [arg for arg in cmd_with_args[1:] if arg != ""]
    if cmd in commands:
        await commands[cmd](client, message, args)
    else:
        await error(message)

if __name__ == '__main__':
    try:
        log.write_to_log_file('Bot started')
        token = sys.argv[1]
        client.run(token)
    except Exception as e:
        log.write_to_log_file(e)
