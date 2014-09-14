import os
import json

import pygments
import pygments.lexers
import pygments.formatters


def _interpreter2ext (interpreter):
    interpreters = {
                     "python": "py",
                     "ruby":   "rb",
                     "perl":   "pl",
                     "php":    "php",
                     "bash":   "sh",
                     "zsh":    "sh",
                     "sh":     "sh",
                   }

    for k,v in interpreters.items():
        if interpreter.startswith(k):
            return v
    return ""


def load_formatter (name):
    return getattr(getattr(__import__("azcat.formatters." + name), "formatters"), name)


def pretty_print (src, s, out, with_formatter):
    """ `src' is a filepath to be formatted. `out' is a file object
        to be written."""

    f = os.path.basename(src)
    ext = os.path.splitext(src)[1].replace(".", "")

    # file with no extension (ex. file contents from stdin)
    if ext == "" and s.startswith("#!"):
        # this is a script without extention. read shebang
        shebang = s.split("\n", 1)[0]
        try:
            interpreter = shebang.split("env ")[1]
        except IndexError:
            interpreter = os.path.basename(shebang[2:])
        ext = _interpreter2ext(interpreter)

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
