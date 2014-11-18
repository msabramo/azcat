import os
import sys
from subprocess import Popen, PIPE, check_output, STDOUT
from azcat.pretty_print import pretty_print

if sys.version_info[0] == 2:
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
    # GNU global
    if args["t"] is not None:
        try:
            output = check_output(["global", "-x", args["t"]]).decode("utf-8")
            if output == "":
                sys.exit("azcat: symbol ``{0}'' not found".format(args["t"]))
            line, file = list(filter(lambda x: x != "", output.split(" ")))[1:3]
            line = int(line)
        except Exception as e:
            sys.exit("azcat: error occurred in global(1)")
    # normal
    else:
        file = args["file"]
        line = 1

    s = load_file(file)

    # get the height of a terminal
    try:
        height = int(check_output(["stty", "size"]).decode("utf-8").split()[0])
    except:
        height = 50 # failed to get the height so use 50 instead

    # if the number of lines is larger than height of the terminal, pipe to a pager
    if s.count("\n") > height:
        p = Popen(["less", "-R", "+{0}g".format(line)], stdin=PIPE)
        try:
            pretty_print(file, s, p.stdin, args["with_formatter"])
            p.stdin = sys.stdin
            p.wait()
        except IOError: # this will raised after the pager existed
            pass
    else:
        out = sys.stdout.buffer
        pretty_print(file, s, out, args["with_formatter"])
