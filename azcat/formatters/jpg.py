import sys
import subprocess
import tempfile

def format_bytes (s):
    with tempfile.NamedTemporaryFile() as f:
        f.write(s)
        try:
            output = subprocess.check_output(["exiv2", f.name]).decode("utf-8")
        except FileNotFoundError:
            sys.exit("azcat: install exiv2 to print metadata of .jpg files")
    return "", str(output)
