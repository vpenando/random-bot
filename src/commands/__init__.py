from commands.ping import ping

commands = {}

def add_cmd(func):
    name = func.cmd
    commands.update({name: func})

add_cmd(ping)

# logs each available command
for cmd in commands:
    print(f"Command '{cmd}' added")
