import os
import sys
from subprocess import Popen, PIPE
from azcat.pretty_print import pretty_print

if sys.version[0] == "2":
    from __builtin__ import raw_input as input

def load_file (filepath):
    try:
        with open(filepath, "r") as f:
            s = f.read()
    except IOError as e:
        sys.exit("azcat: cannot open '%s': %s" % (filepath, str(e)))
    except UnicodeDecodeError:
        sys.exit("azcat: file seems a binary file.")

    if s.find("\x00") != -1 or s.find("\x1b") != -1:
        sys.exit("azcat: file seems a binary file.")

    # confirm if file size is larger than 1MB
    if os.path.getsize(filepath) > 1024*1024:
        if input("file size is big; do you continue? [Y/n]: ") == "n":
            sys.exit()
    return s


def main (args):
    s = load_file(args["file"])

    # if the number of lines is over 50, pipe to a pager
    if s.count("\n") > 50:
        p = Popen(["less", "-R", "-"], stdin=PIPE)
        try:
            pretty_print(args["file"], s, p.stdin, args["with_formatter"])
            p.stdin = sys.stdin
            p.wait()
        except IOError: # this will raised after the pager existed
            pass
    else:
        out = sys.stdout.buffer
        pretty_print(args["file"], s, out, args["with_formatter"])
