import os
import sys
from subprocess import Popen, PIPE
from azcat.pretty_print import pretty_print

if sys.version[0] == "2":
    from __builtin__ import raw_input as input

def main (filepath):
    # abort if it is directory
    if os.path.isdir(filepath):
        sys.exit("azcat: '%s' is a directory. Aborted." % filepath)

    try:
        with open(filepath, "r") as f:
            s = f.read()
    except IOError as e:
        sys.exit("azcat: cannot open '%s': %s" % (f, str(e)))
    except UnicodeDecodeError:
        sys.exit("azcat: file seems a binary file. Aborted.")

    if s.find("\x00") != -1:
        sys.exit("azcat: file seems a binary file. Aborted.")

    # confirm if file size is larger than 1MB
    if os.path.getsize(filepath) > 1024*1024:
        if input("file size is big; do you continue? [Y/n]: ") == "n":
            sys.exit("aborted.")

    # if the number of lines is over 50, pipe to a pager
    if s.count("\n") > 50:
        p = Popen(["less", "-R", "-"], stdin=PIPE)
        try:
            out = p.stdin
            pretty_print(filepath, out)
            p.stdin = sys.stdin
            p.wait()
        except IOError: # this will raised after the pager existed
            pass
    else:
        out = sys.stdout.buffer
        pretty_print(filepath, out)
