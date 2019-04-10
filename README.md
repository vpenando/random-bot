## random-bot
My first Discord bot, written in Python 3 :)

---

#### How to use it
Just run the following command:

`cd src && python3 bot.py <TOKEN>`

---

#### How to add a command?
First of all, *the* question is: how to *create* a command?

It's very simple! Create a new file in `src/commands`, for example `my_cmd.py`:
```py
from discord import Client, Message
from .core import command

@command  # or @command('cmd_name')
def my_cmd(client: Client, message: Message, args: list) -> Message:
    msg = # your code here...
    return client.send_message(message.channel, msg)
```
Et voilà!


#### Todo list
- [x] [Autodetect-cmd](https://github.com/vpenando/random-bot/wiki/Autodetect-cmd)
