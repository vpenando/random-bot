from commands.ping import ping, command
from discord import Client, Message

commands = {}

@command("help")
def help(client: Client, message: Message, args: list) -> Message:
    available_commands = "\n".join(map(lambda s: ' - *!%s*' % s, commands))
    msg = "Available commands:\n%s" % available_commands
    return client.send_message(message.channel, msg)

def add_cmd(func):
    name = func.cmd
    commands.update({name: func})

add_cmd(help)
add_cmd(ping)

# logs each available command
for cmd in commands:
    print("Command '%s' added" % cmd)
