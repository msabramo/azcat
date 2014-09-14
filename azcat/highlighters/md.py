from subprocess import check_output
from colorama import Fore, Back

def highlight (out, s):
    # get the width of a terminal
    width = check_output(["stty", "size"]).decode("utf-8").split()[1]
    in_code_block = False

    for l in s.split("\n"):
         bs = bytes("{0}\n".format(l), "utf-8")
         # code block
         if in_code_block or l.lstrip().startswith("```"):
             out.write(bytes(Fore.CYAN, "utf-8"))
             out.write(bs)
             out.write(bytes(Fore.RESET, "utf-8"))
             if l.lstrip().startswith("```"):
                 in_code_block = False if in_code_block else True
         # headers
         elif l.lstrip().startswith("#"):
             out.write(bytes(Back.BLACK + Fore.WHITE, "utf-8"))
             out.write(bytes(("{0:<" + width + "}").format(l), "utf-8"))
             out.write(bytes(Fore.RESET + Back.RESET, "utf-8"))
         # quotation
         elif l.lstrip().startswith(">"):
             out.write(bytes(Fore.BLUE, "utf-8"))
             out.write(bs)
             out.write(bytes(Fore.RESET, "utf-8"))
         # un-ordered list
         elif l.lstrip().startswith("* ") or l.lstrip().startswith("-"):
             out.write(bytes(Fore.GREEN, "utf-8"))
             out.write(bs)
             out.write(bytes(Fore.RESET, "utf-8"))
         else:
             out.write(bs)
