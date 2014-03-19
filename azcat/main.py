import os
import sys
import azcat.pretty_print

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
        sys.exit("azcar: file seems a binary file. Aborted.")

    # confirm if file size is larger than 1MB
    if os.path.getsize(filepath) > 1024*1024:
        if input("file size is big; do you continue? [Y/n]: ") == "n":
            sys.exit("aborted.")

    azcat.pretty_print.pretty_print(filepath, s)
