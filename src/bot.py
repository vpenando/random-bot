import sys
from discord import Client, Message
from commands import commands

client = Client()

def error(message: Message) -> Message:
    err_msg = f"Error: invalid command '{message.content}''"
    return client.send_message(message.channel, err_msg)

@client.event
async def on_message(message: Message) -> None:
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # we only accept commands starting with '!'
    if message.content[0] != '!':
        return
    msg = message.content.split(' ')[0][1:]
    if f"{msg}" in commands:
        await commands[msg](client, message)
    else:
        await error(message)

token = sys.argv[1]
client.run(token)
