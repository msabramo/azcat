import os
import json

import pygments
import pygments.lexers
import pygments.formatters

from azcat.guess_ext import guess_ext_by_contents, guess_ext_by_filename

def load_formatter (name):
    return getattr(getattr(__import__("azcat.formatters." + name), "formatters"), name)


def pretty_print (src, s, out, with_formatter):
    """ `src' is a filepath to be formatted. `out' is a file object
        to be written."""

    if src == "":
        # file contents from stdin or executable files
        ext = guess_ext_by_contents(s)
    else:
        ext = guess_ext_by_filename(src)

    # format
    if with_formatter:
        try:
            f = load_formatter(ext)
        except ImportError:
            pass
        else:
            ext,s = f.format(s)

    # colorful!
    try:
      lexer = pygments.lexers.get_lexer_by_name(ext)
    except pygments.util.ClassNotFound:
      lexer = pygments.lexers.get_lexer_for_mimetype("text/plain")
    fmt = pygments.formatters.Terminal256Formatter(encoding="utf-8")
    pygments.highlight(s, lexer, fmt, out)
