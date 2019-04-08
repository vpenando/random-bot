# coding: utf-8
from discord import Client, Message
from functools import wraps

def command(cmd):
    def cmd_function_builder(func):
        @wraps(func)
        def wrapped_function(client: Client, message: Message, args:list):
            return func(client, message, args)
        wrapped_function.cmd = cmd
        return wrapped_function
    return cmd_function_builder
