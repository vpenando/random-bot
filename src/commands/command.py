from discord import Client, Message
from functools import wraps

def _error(client, message, command):
    msg = f"Error: invalid command {command}"
    return client.send_message(message.channel, msg)

def command(cmd):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(client: Client, message: Message):    
            return func(client, message)
        wrapped_function.cmd = cmd
        return wrapped_function
    return logging_decorator
