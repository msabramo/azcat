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
                   }

    for k,v in interpreters.items():
        if interpreter.startswith(k):
            return v
    return ""


def pretty_print (src, s, out):
    """ `src' is a filepath to be formatted. `out' is a file object
        to be written. """
    f = os.path.basename(src)
    ext = os.path.splitext(src)[1]

    if ext == "json":
        s = json.dumps(json.loads(s), indent=2)
    elif ext == "":
        # is executable script?
        if os.access(f, os.X_OK) and s.startswith("#!"):
            # this is a script without extention. read shebang
            shebang = s.split("\n", 1)[0]
            try:
                interpreter = shebang.split("env ")[1]
            except IndexError:
                interpreter = os.path.basename(shebang[2:])
            ext = _interpreter2ext(interpreter)
            f += "." + ext

    # colorful!
    try:
      lexer = pygments.lexers.get_lexer_for_filename(f)
    except pygments.util.ClassNotFound:
      lexer = pygments.lexers.get_lexer_for_mimetype("text/plain")
    fmt = pygments.formatters.Terminal256Formatter(encoding="utf-8")
    pygments.highlight(s, lexer, fmt, out)
