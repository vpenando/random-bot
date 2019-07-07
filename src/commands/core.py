# coding: utf-8
import datetime
from functools import wraps

commands = {}

def command(arg=None):
    if callable(arg):
        func = arg  # more explicit
        name = func.__name__
        commands.update({name: func})
        now = datetime.datetime.now()
        print("[{}] Command '{}' added".format(now, name))
        return func
    else:
        def cmd_function_builder(func):
            cmd = arg  # more explicit

            @wraps(func)
            def wrapped_function(client, message, args):
                return func(client, message, args)
            cmd = cmd if cmd is not None else func.__name__
            name = cmd
            commands.update({name: func})
            print("Command '%s' added" % name)
            return wrapped_function
        return cmd_function_builder
