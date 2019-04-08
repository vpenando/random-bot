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
@command("my_cmd")
def my_cmd(client: Client, message: Message, args: list) -> Message:
    msg = # your code here...
    return client.send_message(message.channel, msg)
```
Then, add your new command in `src/__init__.py` this way:
```py
add_cmd(my_cmd)
```
`my_cmd` can now be called from Discord: `!my_cmd`. 

---

#### Todo list
- [ ] [Autodetect-cmd](https://github.com/vpenando/random-bot/wiki/Autodetect-cmd)
