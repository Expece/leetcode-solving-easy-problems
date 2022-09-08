def lengthOfLastWord(s: str) -> int:
    idxSubstr = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            idxSubstr += 1
        if idxSubstr != 0 and s[i] == ' ':
            return idxSubstr
    return idxSubstr