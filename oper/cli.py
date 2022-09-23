# This file is placed in the Public Domain.


from .evt import Event


def __dir__():
    return (
            "docmd",
           ) 


def docmd(clt, txt):
    cmd = Event()
    cmd.channel = ""
    cmd.orig = repr(clt)
    cmd.txt = txt
    clt.handle(cmd)
    cmd.wait()
    return cmd
