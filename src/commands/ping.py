from discord import Client, Message
from .command import command

@command("ping")
def ping(client: Client, message: Message):
    msg = "pong {0.author.mention}".format(message)
    return client.send_message(message.channel, msg)
