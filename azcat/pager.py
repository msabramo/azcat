import sys
from subprocess import Popen, PIPE

def pipe_to_pager (s):
    p = Popen(["less", "-R", "-"], stdin=PIPE)
    p.stdin.write(s.encode("ascii", "ignore"))
    p.stdin = sys.stdin
    try:
        p.wait()
    except IOError: # this will raised after the pager existed
        pass
