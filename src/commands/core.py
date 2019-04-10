# coding: utf-8
from functools import wraps

commands = {}

def command(arg=None):
    if callable(arg):
        func = arg  # more explicit
        func.__cmd__ = func.__name__
        name = func.__cmd__ 
        commands.update({name: func})
        print("Command '%s' added" % name)
        return func
    else:
        def cmd_function_builder(func):
            cmd = arg  # more explicit

            @wraps(func)
            def wrapped_function(client, message, args):
                return func(client, message, args)
            cmd = cmd if cmd is not None else func.__name__
            wrapped_function.__cmd__ = cmd
            name = wrapped_function.__cmd__ 
            commands.update({name: func})
            print("Command '%s' added" % name)
            return wrapped_function
        return cmd_function_builder
