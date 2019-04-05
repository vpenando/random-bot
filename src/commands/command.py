from discord import Client, Message
from functools import wraps

def command(cmd):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(client: Client, message: Message, args:list):
            return func(client, message, args)
        wrapped_function.cmd = cmd
        return wrapped_function
    return logging_decorator
