#!/usr/bin/env python3
# coding: utf-8
import datetime
import sys
from discord import Client, Message
from commands import command, commands

LOG_FILE = "bot.log"
client = Client()

def error(message: Message) -> Message:
    err_msg = "Error: invalid command '%s'" % message.content
    return client.send_message(message.channel, err_msg)

def log_call(user: str, cmd: str) -> None:                                       
    datestr = str(datetime.datetime.now()).split(".")[0]                         
    with open(LOG_FILE, "a") as f:                                               
        f.write("[%s] %s: %s\n" % (datestr, user, cmd)) 

@command
def history(client: Client, message: Message, args: list) -> Message:
    history_size = 10
    if len(args) > 0:
        try:
            history_size = int(args[0])
        except ValueError:
            client.send_message(message.channel,
                                "Invalid value '%s" % args[0])
    lines = []
    with open(LOG_FILE) as f:
        line = f.readline()
        lines.append(line)
    last_lines = lines[-history_size:]
    msg = "\n".join(last_lines)
    return client.send_message(message.channel, msg)

@client.event
async def on_message(message: Message) -> None:
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # we only accept commands starting with '!'
    if message.content[0] != "!":
        return
    cmd_with_args = message.content.split(" ")
    log_call(message.author.display_name, message.content)
    cmd = cmd_with_args[0][1:]
    args = [arg for arg in cmd_with_args[1:] if arg != ""]
    if cmd in commands:
        await commands[cmd](client, message, args)
    else:
        await error(message)

if __name__ == '__main__':
    token = sys.argv[1]
    client.run(token)
