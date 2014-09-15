import os
import mimetypes
import magic

def guess_ext_by_filename (filename):
    FILENAMES = {
                  "Makefile":  "mak",
                }

    ext = os.path.splitext(filename)[1].lstrip(".")
    if ext == "":
        for k,v in FILENAMES.items():
            if filename.startswith(k):
                return v
        return ""
    else:
        return ext


def guess_ext_by_contents (s):
    INTERPRETERS = {
                     "python": "py",
                     "ruby":   "rb",
                     "perl":   "pl",
                     "php":    "php",
                     "bash":   "sh",
                     "zsh":    "sh",
                     "sh":     "sh",
                   }

    # guess by shebang
    if s.startswith("#!"):
        shebang = s.split("\n", 1)[0]
        try:
            interpreter = shebang.split("env ")[1] #!/usr/bin/env python
        except IndexError:
            interpreter = os.path.basename(shebang[2:]) #!/usr/bin/python

        for k,v in INTERPRETERS.items():
            if interpreter.startswith(k):
                return v

    # guess by libmagic
    else:
        mime = str(magic.from_buffer(bytes(s, "utf-8"), mime=True), "utf-8")
        ext  = mimetypes.guess_extension(mime).rstrip(".")
        return ext

    return ""
