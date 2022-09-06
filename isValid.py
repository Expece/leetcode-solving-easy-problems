def isValid(s: str) -> bool:
    if len(s) <= 1:
        return False
    opnBrk = '({['
    clsBrk = ')}]'
    opnBuff = []
    clsBuff = []
    for i in s:
        if i in opnBrk:
            opnBuff.append(i)
        elif len(opnBuff) != 0:
            clsBuff.append(i)
            if clsBrk.index(clsBuff[-1]) != opnBrk.index(opnBuff[-1]):
                return False
            else:
                clsBuff.pop()
                opnBuff.pop()
        else:
            return False
    if len(opnBuff) != len(clsBuff):
        return False
    return True