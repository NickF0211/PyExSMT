# Copyright: see copyright.txt

from .symbolic_int import SymbolicInteger
from .symbolic_int import SymbolicObject

def getSymbolic(v):
    exported = [(int, SymbolicInteger)]
    for (t, s) in exported:
        if isinstance(v, t):
            return s
    return None
